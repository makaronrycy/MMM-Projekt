import numpy as np
import matplotlib.pyplot as plt
from config import Config as conf
from config import InputSignal
plt.style.use('_mpl-gallery')
class controlSystem:
    def __init__(self,cfg):
        self.cfg = cfg
        a = cfg.a1*cfg.c2
        b = cfg.a1*cfg.c1 + cfg.a0*cfg.c2
        c = cfg.a1*cfg.c0 + cfg.a0*cfg.c1
        d = cfg.a0*cfg.c0
        e = cfg.b2*cfg.d2
        f = cfg.b2*cfg.d1 + cfg.b1*cfg.d2
        g = cfg.b2*cfg.d0 + cfg.b1*cfg.d1 + cfg.b0*cfg.d2
        h = cfg.b1*cfg.d0 + cfg.b0*cfg.d1
        i = cfg.b0*cfg.d0
        self.a0 = (d + i) / e
        self.a1 = (c + h) / e
        self.a2 = (b + g) / e
        self.a3 = (a + f) / e
        self.b0 = d / e
        self.b1 = c / e
        self.b2 = b / e
        self.b3 = a / e

        us = []
        uf = []
        ut = []
        w = cfg.getFrequency()
        total = cfg.getNumberOfSamples()
        self.u = []
        for i in range(0, total):
            us.append(cfg.M * np.sin(w * i * cfg.h)) #sinus
            uf.append(cfg.M if us[i] > 0 else 0) #square
            ut.append(4*self.cfg.M/cfg.L*np.abs(((i*cfg.h-(self.cfg.L/4))%self.cfg.L)-self.cfg.L/2) - self.cfg.M)
        if(cfg.input == InputSignal.SQUARE): self.u = uf
        elif(cfg.input == InputSignal.SINUS): self.u = us
        elif (cfg.input == InputSignal.TRIANGLE): self.u = ut
        self.output = []



    def checkStability(self):
        if self.a3 > 0 and self.a2 > 0 and self.a1 >0 and self.a0 > 0 and self.a3*self.a2*self.a1 - (self.a3**2) * self.a0 - self.a1**2 >0:
            return True
        else: return False
    def eulerMethod(self):
        t = [None] * len(self.u)
        A = [[0,1,0,0],
             [0,0,1,0],
             [0,0,0,1],
             [-self.a0,-self.a1, -self.a2, -self.a3]]
        B = [[0],[0],[0],[1]]
        C = [self.b0,self.b1,self.b2,self.b3]
        D = [0]
        #warunki początkowe
        xi_1 = [[0],[0],[0],[0]]
        max_y = 0
        min_y = 0
        total = self.cfg.getNumberOfSamples()
        for i in range(0, total):
            t[i] = i*self.cfg.h;
            Ax = np.dot(A,xi_1)
            Bu = np.multiply(B,self.u[i])
            Cx = np.dot(C,xi_1)
            Du = np.multiply(D,self.u[i])
            xi = Ax+Bu
            xi = xi*self.cfg.h
            xi = xi_1+xi
            xi_1 = xi
            self.output.append(Cx+Du)
            if(self.output[i] > max_y): max_y = self.output[i]
            elif(self.output[i] < min_y): min_y = self.output[i]
        #plot
        fig, ax = plt.subplots()

        ax.plot(t, self.u,'r', linewidth=1.0)
        ax.plot(t, self.output, linewidth=1.0)
        ax.set_xlabel("t")
        ax.set_ylabel("y(t)")
        ax.set(xlim=(0, self.cfg.T), xticks=np.arange(0, self.cfg.T),
               ylim=(np.round(min_y)-1, np.ceil(max_y)+1), yticks=np.arange(np.round(min_y), np.ceil(max_y)))
        plt.get_current_fig_manager().window.state('zoomed')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

        plt.show()