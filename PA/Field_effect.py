import numpy as np
import math
import copy
import scipy.constants
from Fields import fields


class Field_effect:
        def __init__(self, P_state_pos, P_state_charge, P_state_vel):
            self.P_pos=P_state_pos
            self.P_vel=P_state_vel
            self.P_charge=P_state_charge
            
        def E_effect(P_pos,P_vel,P_charge):
            E=0
            Phi_p= math.atan(P_pos[1]/P_pos[0])
            print(P_pos[1]/P_pos[0], '  y/x')
#            j=0
##            print(len(fields.E_prop_list()[0])-1)
#            while j<len(fields.E_prop_list()[0])-1:
#                Phi_E_f=math.atan(fields.E_prop_list()[0][j+1][1]/fields.E_prop_list()[0][j+1][0])
#                Phi_E_b=math.atan(fields.E_prop_list()[0][j][1]/(fields.E_prop_list()[0][j][0]+scipy.constants.hbar))
#                print('j, phiP, PhiEf, PhiEb   ',j,Phi_p,Phi_E_f,Phi_E_b)
#                
#                
#                
#                if Phi_E_f>Phi_p and Phi_p>Phi_E_b:
            for i in range(0,len(fields.E_prop_list()[0])):
                            #print('P_pos: ',P_pos,'E_pos',np.array(fields.E_prop_list()[0][i],dtype=float))
#                            sign=(-1)**(i-j)
                            
                P_to_Es_Distance=P_pos-np.array(fields.E_prop_list()[0][i], dtype=float)
                            
                            #E_i=(1/(4*scipy.constants.pi*scipy.constants.epsilon_0))*fields.E_prop_list()[1][i]*P_to_Es_Distance/(np.linalg.norm(P_to_Es_Distance))**3
                            #print((np.linalg.norm(P_to_Es_Distance)))
                E_i=(fields.E_prop_list()[1][i]/(2*scipy.constants.epsilon_0)*(1-(np.linalg.norm(P_to_Es_Distance))/((np.linalg.norm(P_to_Es_Distance)**2+fields.E_prop_list()[2]**2)**0.5))*(P_to_Es_Distance)/(np.linalg.norm(P_to_Es_Distance)))
                E += E_i  
#                j=j+1
#                print('loop ended, E= ',E)
                
#                print('E=: ',E)
            return(E)
        def M_effect(P_pos,P_vel,P_mass,P_charge,KE):
#            theta=math.atan(P_pos[0]/P_pos[1])
#            B_0=KE/(scipy.constants.elementary_charge*scipy.constants.speed_of_light*50)
#            B=fields.M_prop_list(theta,B_0)
            
#            bz=-(1.67*10**-27)*1000/((1.602*10**-19)*1000)
#            print(bz)
            bz=-(P_mass*np.linalg.norm(P_vel)/((P_charge)*fields.E_prop_list()[3]))
#            print(bz)
            B=np.array([0.0,0.0,bz], dtype=float)

#            print(B,' B')
#            print(B_0,' B_0')
            return(B)