from pyactor.context import set_context, create_host, serve_forever
from peer import *
from tracker import *
from Print import *

if __name__ == "__main__":
    set_context()
    h = create_host()

    tracker = h.spawn("tracker", Tracker)
    printer = h.spawn("printer", Print)

    seed = h.spawn("Seed", Peer)
    josep = h.spawn("Josep", Peer)
    sergi = h.spawn("Sergi", Peer)
    pedro = h.spawn("Pedro", Peer)
    andrea = h.spawn("Andrea", Peer)
    trump = h.spawn("Trump", Peer)

    seed.attach(tracker, printer)
    josep.attach(tracker, printer)
    sergi.attach(tracker, printer)
    pedro.attach(tracker, printer)
    andrea.attach(tracker, printer)
    trump.attach(tracker, printer)

    seed.seed_fitxer()
    seed.init_start(3)
    josep.init_start(3)
    sergi.init_start(3)
    pedro.init_start(3)
    andrea.init_start(3)
    trump.init_start(3)

    serve_forever()

