from datetime import datetime


class Tracker(object):
    # llistaPeers= {}
    _tell = ['announce']
    _ask = ['getPeers']
    _ref = ['announce', 'getPeers']

    def __init__(self):
        self.tracker = {}  # Dicionari [key=hashTorrent, dicionari[idPeer,ttl]]

    def announce(self, torrentHash, idPeer):
        try:
            self.tracker[torrentHash][idPeer] = datetime.now()
        except:
            self.tracker[torrentHash] = {idPeer: datetime.now()}

    def getPeers(self, torrentHash):
        if (torrentHash in self.tracker):
            llista = set()
            for i in range(3):
                # falta comprovar si es aleatori i que no es repeteix
                llista.add(self.tracker[torrentHash].choice())
            return llista
        else:
            return []

    def calculTime(self):  # al lio
        for h in self.tracker:
            timeNow = datetime.now()
            for p, ttl in self.tracker.items():
                resta = timeNow - ttl
                if (resta.second > 10):
                    h[p].pop()
