import datetime
from Tracker import *
from pyactor.context import interval
from random import choice
from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, serve_forever

llargada_paraula = 0

class Peer(object):
    _tell = ['attach', 'announce_peer', 'seed_fitxer', 'init_start', 'donar_lletra', 'push', 'demanar_lletra']
    _ask = ['pull']
    _ref = ['attach', 'init_start', 'push']

    def __init__(self):
        self.paraula = {}
        self.torrent_hash = "peli.txt"

    def attach(self, tracker, printer):
        self.tracker = tracker
        self.printer = printer

    def announce_peer(self):
        self.tracker.announce(self.torrent_hash, self)

    def seed_fitxer(self):
        with open(self.torrent_hash) as f:
            for idx, ch in enumerate(f.readline()):
                self.paraula[idx] = ch
        global llargada_paraula
        llargada_paraula = len(self.paraula)

    def init_start(self, opcio):
        self.interval = interval(self.host, 3, self.proxy, 'announce_peer')
        if (opcio == 1 or opcio == 3):
            self.interval1 = interval(self.host, 1, self.proxy, 'demanar_lletra')
        if (opcio == 2 or opcio == 3):
            self.interval2 = interval(self.host, 1, self.proxy, 'donar_lletra')

    def donar_lletra(self):
        for peer in self.tracker.get_peers(self.torrent_hash):
            try:
                lletra = choice(self.paraula.items())
                peer.push(lletra[0], lletra[1])
            except:
                pass

    def push(self, pos, lletra):
        self.paraula[pos] = lletra
        self.printer.printer(str(self.id)+str(self.paraula))

    def demanar_lletra(self):
        for peer in self.tracker.get_peers(self.torrent_hash):
            for i in range(llargada_paraula):
                if (i not in self.paraula.keys()):
                    try:
                        self.paraula[i] = peer.pull(i)
                        self.printer.printer(str(self.id)+str(self.paraula))
                    except:
                        pass
                    break

    def pull(self, i):
        return self.paraula[i]
