from datetime import datetime
from pyactor.context import interval
from random import sample


class Tracker(object):
    _tell = ['announce', 'calcul_time', 'init_intervals']
    _ask = ['get_peers']
    _ref = ['announce', 'get_peers']

    def __init__(self):
        self.tracker = {}  # Dicionari [key=hashTorrent, dicionari[idPeer,ttl]]

    def init_intervals(self):
        self.interval = interval(self.host, 1, self.proxy, "calcul_time")   # cada 1s mira calcul_time

    def announce(self, torrentHash, idPeer):
        try:
            self.tracker[torrentHash][idPeer] = datetime.now()
        except KeyError:
            self.tracker[torrentHash] = {idPeer: datetime.now()}    # en cas que sigui el primer announce

    def get_peers(self, torrentHash):
        try:
            llista = set(self.tracker[torrentHash].keys())
            if(len(llista)>3):
                return sample(llista,3)
            else:
                return llista
        except:
            return []

    def calcul_time(self):
        timeNow = datetime.now()
        for swarm in self.tracker.values():
            for p, ttl in self.tracker.items():
                resta = timeNow - ttl
                if (resta.total_seconds() > 10):
                    swarm[p].pop()
