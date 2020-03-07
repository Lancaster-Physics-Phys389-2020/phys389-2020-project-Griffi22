import pytest
import numpy as np
import scipy.constants as const
from Field_effect import Field_effect

def test_E_fields():
    "creating a test enviroment with calculated analitical solutions"

    "test particle properties"
    T1_state_pos=np.array([1.1,0,0],dtype=float)
    T1_state_vel=np.array([1.1,0,0],dtype=float)

    T1_state_charge, T1_state_mass, T1E_plate_index= 1, 1, 0


    "E_source properties"
    T1_E_source_pos_list=[[1,0,0],[2,0,0]]
    #In order to loop the list in the same way the actual E source list works. should not effect calculation as this looped value's charge will be set to 0 for testing
    T1_E_source_pos_list.append(T1_E_source_pos_list[0])
    T1_E_source_chargedensity_list=[1,0]
    T1_E_source_chargedensity_list.append(0)
    
    T1_E_plate_radius, T1_Path_rad, T1_num_E_source = 1, 1, 2


    Testing_state=[T1_state_pos, T1_state_vel, T1_state_charge,T1_state_mass, T1E_plate_index, [T1_E_source_pos_list, T1_E_source_chargedensity_list, T1_E_plate_radius, T1_Path_rad, T1_num_E_source]]
    Field_effect_test=Field_effect(None, True, Testing_state)

    T1_E_effect_solution=[5.0851478114*10**10,0,0]
    np.testing.assert_allclose(Field_effect_test.E_effect()[0], T1_E_effect_solution, rtol=0.00001) 
    print(100*(T1_E_effect_solution[0]-Field_effect_test.E_effect()[0][0])/(T1_E_effect_solution[0])," % ", "difference from expected value")

