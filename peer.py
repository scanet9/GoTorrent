import datetime
from tracker import *
from pyactor.context import interval
import random

class Peer(object):

    def __init__(self):
        self.paraula = {}
        self.torrentHash="file.txt"

    def init_start(self):
        self.interval = interval(self.host, 3, self.proxy, 'announce_peer')
        later(5, self.proxy, 'stop_interval')

        intervals de temps
        announce

        self.interval = interval(self.host, 3, self.proxy, 'announce_peer') //cridar annunce tracker
        if push pull hybrid

    def seedFitxer(self):
        id=0
        with open("file.txt") as f:
            for line in f:
                for ch in line:
                    self.paraula[id] = ch
                    id=id+1
        self.llargadaParaula = id+1

    def recive_data(self):

    def push(self):
        llistaPeers = self.tracker.getPeers(self.torrentHash)
        for peer in llistaPeers:
            self.paraula.choice()
            peer.recive_data()
            enviar posicio i lletra

    def demanar_lletra(self):

    def pull(self):

        for i in self.llargadaParaula:
            if (i not in self.paraula.keys()):
                demanar lletra

    def hybrid(self):

    def attach(self, tracker):
        self.tracker=tracker




