import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt
from Fields import fields
from Field_effect import Field_effect
class Update:
    """
    Class to model a massive particle in a gravitational field.
    It will make use of numpy arrays to store the pos vel etc.
    Working directly from past exercises...

    mass in kg
    pos and vel in m
    """

    #G=6.67408E-11
    G=scipy.constants.G

    def __init__(self, initPos, initVel, initAcc, Name, Mass,Charge,KE, deltaT):
        self.Name = Name
        self.pos = np.array(initPos,dtype=float)
        self.vel = np.array(initVel,dtype=float)
        self.acc = np.array(initAcc,dtype=float)
        self.mass = Mass
        self.charge=Charge
        self.DeltaT=deltaT
        self.KE=KE

    def __repr__(self):
        return('Particle: {0}, Mass: {1:12.3e}, pos: {2}, vel: {3}, acc: {4}'.format(self.Name,self.mass,self.pos, self.vel,self.acc))

        #print('Particle: {0}, Mass: {1:12.3e}, pos: {2}, vel: {3}, acc: {4}'.format(self.Name,self.mass,self.pos, self.vel,self.acc))

    def KineticEnergy(self):
        self.KE=0.5*self.mass*np.linalg.norm(self.vel)**2
#        print('vel: ',self.vel)
#        print('Vel: ',np.linalg.norm(self.vel))
        return 0.5*self.mass*np.vdot(self.vel,self.vel)

    def momentum(self):
        return self.mass*np.array(self.vel,dtype=float)
    
    def update(self):
        self.pos +=  self.vel*self.DeltaT
        self.vel +=  self.acc*self.DeltaT
        self.E=Field_effect.E_effect(self.pos,self.vel,self.charge)
        self.acc = (self.charge/self.mass)*((self.E)+np.cross(self.vel,Field_effect.M_effect(self.pos,self.vel,self.mass,self.charge,self.KE)))