import numpy as np
import math
import copy
import scipy.constants

class fields:
    def E_prop_list():
#        setting the variables needed:
#        E_plte_radius:radius of the virtual charged plates,
        E_plate_radius=20
#        list for allocation of plate position
        E_source_pos_list=[]
#        number of source plates to generate
        num_E_source=200
#        defining the accelerator radius
        Path_rad=10000

#        generating the sources equally spaced across the accelerator path
        for i in range(0,num_E_source):
            phi=i*2*math.pi/num_E_source
            E_source_pos_list.append([Path_rad*math.cos(phi),Path_rad*math.sin(phi),0.00])
#        Setting the charge density of each source plate
        E_source_chargedensity_list=[]
        for i in range(0,len(E_source_pos_list)):
            E_source_chargedensity_list.append(1*10**-11)
#        making the E lists circular by linking the last and first entry
        E_source_pos_list.append(E_source_pos_list[0])
        E_source_chargedensity_list.append(E_source_chargedensity_list[0])
#        returning variables to be used elsewhere
        return(E_source_pos_list,E_source_chargedensity_list,E_plate_radius,Path_rad,num_E_source)

    def M_prop_list(self,P_vel):
#        setting the strength of the B feild such that the path radius remains constant over ranging velocities
#        bz=-(scipy.constants.proton_mass*P_vel/((scipy.constants.elementary_charge)*fields.E_prop_list()[3]))
        B=np.array([0.0,0.0,0], dtype=float)
        return(B)



