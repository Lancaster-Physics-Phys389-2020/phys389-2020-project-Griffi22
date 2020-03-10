import numpy as np
import math
import copy
import scipy.constants
from Fields import fields
import timeit
class Field_effect:
    #    def __init__(self, P_state_pos, P_state_vel, P_state_charge, P_state_mass, E_plate_index,testing,TestParameters):
        def __init__(self, Simulation_state, Testing_OnOff, Testing_state):
            if Testing_OnOff == False:
                self.P_pos=Simulation_state[0]
                self.P_vel=Simulation_state[1]
                self.P_charge=Simulation_state[2]
                self.P_mass=Simulation_state[3]
                self.E_plate_index=Simulation_state[4]
                self.E_prop_list=fields.E_prop_list()
            if Testing_OnOff == True:
                self.P_pos=Testing_state[0]
                self.P_vel=Testing_state[1]
                self.P_charge=Testing_state[2]
                self.P_mass=Testing_state[3]
                self.E_plate_index=Testing_state[4]
                self.E_prop_list=Testing_state[5]

        #resultant effect of local electric source plates
        def E_effect(self):
            #timing used for testing optimisation
#            start_0=timeit.default_timer()
            E=0
            #calculate the angluar position of particle in accelerator
            Phi_p=np.angle(self.P_pos[0]+1j*self.P_pos[1], deg=True)%360
            i=self.E_plate_index
            
#            i=0
            #loop over E plates
            while i<len(self.E_prop_list[0])-1:
#                calculate the angular position of plate (i) and next plate (i+1) in the accelerator path
                 Phi_E_i1=round(np.angle(self.E_prop_list[0][i+1][0]+self.E_prop_list[0][i+1][1]*1j, deg=True)%360)
                 Phi_E_i0=round(np.angle(self.E_prop_list[0][i][0]+self.E_prop_list[0][i][1]*1j, deg=True)%360)
#                 if the angular position of the particle lies between the two plates then calculate the feild produced by the plates
                 if Phi_E_i1>=Phi_p>=Phi_E_i0 or i==len(self.E_prop_list[0])-2: #i==len(fields...) is added for a looping as final plate at 360 degrees=0 degrees
                     for Index in range(i,i+2):
                         #oscillation of the charge of the plates such that plates ahead attract and plates behind repel
                         sign=(-1)**(Index-i)
#                         print('particle angle',Phi_p,'E before angle',Phi_E_i0,'E after angle',Phi_E_i1)
                         #plate to particle position vector
                         P_to_Es_Distance=self.P_pos-np.array(self.E_prop_list[0][Index], dtype=float)
                         #calculating E from plate (Index) using a finite charged 2D dis formula
                         E_index=sign*(self.E_prop_list[1][Index]/(2*scipy.constants.epsilon_0)*(1-(np.linalg.norm(P_to_Es_Distance))/((np.linalg.norm(P_to_Es_Distance)**2+self.E_prop_list[2]**2)**0.5))*(P_to_Es_Distance)/(np.linalg.norm(P_to_Es_Distance)))
                         E += E_index
#                     print(i)
#                     print('index',   i)# self.E_plate_index)
                     self.E_plate_index=i%(len(self.E_prop_list[0])-2)
                     return(E,self.E_plate_index)
                 
                 i+=1
                 #modulo addition allows for loop (i) resetting when particle passes 360 degrees
                 i=i%(len(self.E_prop_list[0])-1)

        def M_effect(self, Testing_OnOff,Testing_state):
            if Testing_OnOff == False:
                bz=-(self.P_mass*np.linalg.norm(self.P_vel)/((self.P_charge)*self.E_prop_list[3]))
                B=np.array([0.0,0.0,bz], dtype=float)
            if Testing_OnOff == True:
                bz=-(Testing_state[0]*np.linalg.norm(Testing_state[1])/((Testing_state[2])*Testing_state[3]))
                B=np.array([0.0,0.0,bz], dtype=float)

            return(B)


class Field_effect_derivitives(Field_effect):
    def __init__(self, Simulation_state, Testing_OnOff, Testing_state, P_state_acc,P_state_acc_dt1):
        super().__init__(Simulation_state, Testing_OnOff, Testing_state)
        self.P_acc=P_state_acc
        self.P_acc_dt1=P_state_acc_dt1
    def E_effect_dt1(self):
        i=self.E_plate_index
        E_dt1=0
        for Index in range(i,i+2):
            sign=(-1)**(Index-i)
            P_to_Es_Distance=self.P_pos-np.array(self.E_prop_list[0][Index], dtype=float)
            E_index_dt1 = sign*(self.E_prop_list[1][Index]/(2*scipy.constants.epsilon_0))*(self.E_prop_list[2]**2*np.linalg.norm(self.P_vel))/((np.linalg.norm(P_to_Es_Distance)**2+self.E_prop_list[2]**2)**(3/2))*(P_to_Es_Distance)/(np.linalg.norm(P_to_Es_Distance))
            E_dt1+= E_index_dt1
        return(E_dt1)
    
    def E_effect_dt2(self):
        i=self.E_plate_index
        E_dt2=0
        for Index in range(i,i+2):
            sign=(-1)**(Index-i)
            P_to_Es_Distance=self.P_pos-np.array(self.E_prop_list[0][Index], dtype=float)
            E_index_dt2 = sign*(self.E_prop_list[1][Index]/(2*scipy.constants.epsilon_0))*((self.E_prop_list[2]**2*np.linalg.norm(self.P_acc))/((np.linalg.norm(P_to_Es_Distance)**2+self.E_prop_list[2]**2)**(3/2))+(3*self.E_prop_list[2]**2*np.linalg.norm(P_to_Es_Distance)*np.linalg.norm(self.P_vel)**2/(np.linalg.norm(P_to_Es_Distance)**2+self.E_prop_list[2]**2)**5/3))*(P_to_Es_Distance)/(np.linalg.norm(P_to_Es_Distance))
            E_dt2+= E_index_dt2
        return(E_dt2)
    
    
    
    def M_effect_dt1(self):
        bz_dt1=-(self.P_mass*np.linalg.norm(self.P_acc)/((self.P_charge)*self.E_prop_list[3]))
        B_dt1=np.array([0.0,0.0,bz_dt1], dtype=float)
        return(B_dt1)
    
    def M_effect_dt2(self):
        bz_dt2=-(self.P_mass*np.linalg.norm(self.P_acc_dt1)/((self.P_charge)*self.E_prop_list[3]))
        B_dt2=np.array([0.0,0.0,bz_dt2], dtype=float)
        return(B_dt2)
    