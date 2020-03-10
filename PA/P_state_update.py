import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt
import timeit
from Field_effect import Field_effect
from Field_effect import Field_effect_derivitives
class Update:
    """
    Class to model a massive particle in a gravitational field.
    It will make use of numpy arrays to store the pos vel etc.
    Working directly from past exercises...

    mass in kg
    pos and vel in m
    """

    """Change to SR motion EQn's split acceleration into subclass"""
    
#    initialising the program with the required particle state properties
    def __init__(self, initPos, initVel, initAcc,Acc_dt1,Acc_dt2, Name, Mass,Charge,KE, deltaT,E_plate_index):
        self.Name = Name
        self.pos = np.array(initPos,dtype=float)
        self.vel = np.array(initVel,dtype=float)
        self.acc = np.array(initAcc,dtype=float)
        self.mass = Mass
        self.charge=Charge
        self.DeltaT=deltaT
        self.KE=KE
        self.E_plate_index=E_plate_index
        self.Acc_dt1= np.array(Acc_dt1,dtype=float)
        self.Acc_dt2= np.array(Acc_dt2,dtype=float)
    def __repr__(self):
        return('Particle: {0}, Mass: {1:12.3e}, pos: {2}, vel: {3}, acc: {4}'.format(self.Name,self.mass,self.pos, self.vel,self.acc))
#   updating KE
    def KineticEnergy(self):
        self.KE=0.5*self.mass*np.linalg.norm(self.vel)**2
        return 0.5*self.mass*np.vdot(self.vel,self.vel)
# updating mom
    def momentum(self):
        return self.mass*np.array(self.vel,dtype=float)
#updating pos, vel, acc
    def update(self, Testing_OnOff, Testing_state):
        start = timeit.default_timer()
        print('Vel:  ', np.linalg.norm(self.vel)*self.DeltaT)
        print('Pos:  ', self.pos)
        print('Acc:  ', self.acc)#*self.DeltaT)
        print('Acc_dt1:  ', np.linalg.norm(self.Acc_dt1)*self.DeltaT)
        Particle_state=[self.pos,self.vel,self.charge,self.mass, self.E_plate_index]
        fields=Field_effect(Particle_state, False, None)
        B=fields.M_effect(False,None)
        E_eff_result_list=fields.E_effect()
        E=E_eff_result_list[0]
        self.E_plate_index=E_eff_result_list[1]
        fields_dt=Field_effect_derivitives(Particle_state, False, None, self.acc, self.Acc_dt1)
        E_dt1=fields_dt.E_effect_dt1()
        B_dt1=fields_dt.M_effect_dt1()
        E_dt2=fields_dt.E_effect_dt2()
        B_dt2=fields_dt.M_effect_dt2()
        self.Acc_dt2 = (self.charge/self.mass)*(E_dt2+np.cross(self.Acc_dt1,B)+np.cross(self.acc,B_dt1)+np.cross(self.acc,B_dt1)+np.cross(self.vel,B_dt2))
        self.Acc_dt1 = (self.charge/self.mass)*(E_dt1+(np.cross(self.acc,B)+np.cross(self.vel,B_dt1)))
        self.acc = (self.charge/self.mass)*(E+np.cross(self.vel,B))
        self.vel +=  (self.acc*self.DeltaT)+(self.Acc_dt1*self.DeltaT**2)/2+(self.Acc_dt2*self.DeltaT**3)/6
        self.pos +=  (self.vel*self.DeltaT)+(self.acc*self.DeltaT**2)/2+(self.Acc_dt1*self.DeltaT**3)/6+(self.Acc_dt2*self.DeltaT**4)/24
#        self.vel +=  (self.acc*self.DeltaT)+(self.Acc_dt1*self.DeltaT**2)/2
#        self.acc = (self.charge/self.mass)*(E+np.cross(self.vel,B))
#        self.Acc_dt1 = (self.charge/self.mass)*(E_dt1+(np.cross(self.acc,B)+np.cross(self.vel,B_dt1)))
#        self.Acc_dt2 = (self.charge/self.mass)*(E_dt2+np.cross(self.Acc_dt1,B)+np.cross(self.acc,B_dt1)+np.cross(self.acc,B_dt1)+np.cross(self.vel,B_dt2))
#        fields=Field_effect(self.pos,self.vel,self.charge,self.mass, self.E_plate_index)
#        B=fields.M_effect()
#        E=fields.E_effect()[0]
#        self.E_plate_index=fields.E_effect()[1]
#        fields_dt1=Field_effect_derivitives(self.pos,self.vel,self.charge,self.mass, self.E_plate_index,self.acc)
#        E_dt1=fields_dt1.E_effect_dt1()
#        B_dt1=fields_dt1.M_effect_dt1()
#        self.acc = (self.charge/self.mass)*(E+np.cross(self.vel,B))
#        self.Acc_dt1 = (self.charge/self.mass)*(E_dt1+(np.cross(self.acc,B)+np.cross(self.vel,B_dt1)))
#    
        stop = timeit.default_timer()
        print('update time', stop-start)
        
        
        
        
        