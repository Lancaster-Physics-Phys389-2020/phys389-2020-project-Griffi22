import numpy as np
import math
import copy
import scipy.constants
from Fields import fields
import timeit

class Field_effect:
        def __init__(self, P_state_pos, P_state_charge, P_state_vel):
            self.P_pos=P_state_pos
            self.P_vel=P_state_vel
            self.P_charge=P_state_charge
            #resultant effect of local electric source plates
        def E_effect(P_pos,P_vel,P_charge):
            #timing used for testing optimisation
#            start_0=timeit.default_timer()
            E=0
            #calculate the angluar position of particle in accelerator
            Phi_p=np.angle(P_pos[0]+1j*P_pos[1], deg=True)%360
            i=0
            #loop over E plates
            while i<len(fields.E_prop_list()[0])-1:
#                calculate the angular position of plate (i) and next plate (i+1) in the accelerator path
                 Phi_E_i1=round(np.angle(fields.E_prop_list()[0][i+1][0]+fields.E_prop_list()[0][i+1][1]*1j, deg=True)%360)
                 Phi_E_i0=round(np.angle(fields.E_prop_list()[0][i][0]+fields.E_prop_list()[0][i][1]*1j, deg=True)%360)
#                 if the angular position of the particle lies between the two plates then calculate the feild produced by the plates
                 if Phi_E_i1>=Phi_p>=Phi_E_i0 or i==len(fields.E_prop_list()[0])-2: #i==len(fields...) is added for a looping as final plate at 360 degrees=0 degrees
                     for Index in range(i,i+2):
                         #oscillation of the charge of the plates such that plates ahead attract and plates behind repel
                         sign=(-1)**(Index-i)
                         #plate to particle position vector
                         P_to_Es_Distance=P_pos-np.array(fields.E_prop_list()[0][Index], dtype=float)
                         #calculating E from plate (Index) using a finite charged 2D dis formula
                         E_index=sign*(fields.E_prop_list()[1][Index]/(2*scipy.constants.epsilon_0)*(1-(np.linalg.norm(P_to_Es_Distance))/((np.linalg.norm(P_to_Es_Distance)**2+fields.E_prop_list()[2]**2)**0.5))*(P_to_Es_Distance)/(np.linalg.norm(P_to_Es_Distance)))
                         E += E_index
                     return(E)
                     "cashe i for future optimisation"
                     break
                 
                 i+=1
                 #modulo addition allows for loop (i) resetting when particle passes 360 degrees
                 i=i%(len(fields.E_prop_list()[0])-1)

        def M_effect(P_pos,P_vel,P_mass,P_charge,KE):
            bz=-(P_mass*np.linalg.norm(P_vel)/((P_charge)*fields.E_prop_list()[3]))
            B=np.array([0.0,0.0,bz], dtype=float)
            return(B)