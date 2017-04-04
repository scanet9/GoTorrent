import peer
import tracker
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever

if __name__ == "__main__":

    set_context()

    h = create_host()

    t = h.spawn("Tracker", tracker)

    seed = h.spawn("Seed", peer)
    josep = h.spawn("Josep", peer)
    sergi = h.spawn("Sergi", peer)
    pedro = h.spawn("Pedro", peer)
    andrea = h.spawn("Andrea", peer)
    trump = h.spawn("Trump", peer)

    seed.seedFitxer()

    seed.attach_tracker(tracker)
    josep.attach_tracker(tracker)
    sergi.attach_tracker(tracker)
    pedro.attach_tracker(tracker)
    andrea.attach_tracker(tracker)
    trump.attach_tracker(tracker)

    tracker.init_start()

    seed.init_start()
    josep.init_start()
    sergi.init_start()
    pedro.init_start()
    andrea.init_start()
    trump.init_start()

    josep.calculTime()
    sergi.calculTime()
    pedro.calculTime()
    andrea.calculTime()
    trump.calculTime()
    seed.calculTime()

    serve_forever()
