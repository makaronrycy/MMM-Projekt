import numpy as np
from enum import Enum

class InputSignal(Enum):
    SQUARE = 1
    SINUS = 2

class Config:
    def __init__(self):
        #współczynniki
        self.a1 = 1
        self.a0 = 1
        self.b2 = 1
        self.b1 = 1
        self.b0 = 1
        self.c2 = 1
        self.c1 = 1
        self.c0 = 1
        self.d2 = 1
        self.d1 = 1
        self.d0 = 1
        self.h =0.001   #krok obliczeń
        self.L = 2.5    #liczba okresów sygnału sinus w przedziale T
        self.T = 10     #czas symulacji
        self.M = 1      #amplituda
        self.input = InputSignal.SQUARE
    def getNumberOfSamples(self):
        return int((1.0*self.T/self.h)+1)
    def getFrequency(self):
        return 2.0*np.pi*self.L/self.T
