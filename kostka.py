#!/usr/bin/env python3
#barbora

import random

class Kostka:

    def __init__(self, steny = 6):
        self.pocet_sten = steny

    def __str__(self):
        return f'Kostka s {self.pocet_sten} stenami.'

    def hod(self) :
        return random.randint(1,self.pocet_sten)

    def getPocetSten(self):
        return self.pocet_sten
k1 = Kostka()
print(f'Kostka s {k1.pocet_sten} stenami.')
print(k1.getPocetSten()+10)
print(k1.hod())
k2 = Kostka()
print(k2)
