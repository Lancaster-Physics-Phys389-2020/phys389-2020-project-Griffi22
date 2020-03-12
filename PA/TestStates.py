import pytest
import numpy as np
import scipy.constants as const
from Field_effect import Field_effect

class E_Teststates():
    def Teststate_1():
        "creating a test enviroment with calculated analitical solutions"
        "field of a single charged disk at some point"
        "test particle properties"
        T1_state_pos = np.array([1.1,0,0],dtype=float)
        T1_state_vel = np.array([1.1,0,0],dtype=float)
        T1_state_charge = 1
        T1_state_mass = 1
        T1E_plate_index= 0

        "E_source properties"
        T1_E_source_pos_list = [[1,0,0],[2,0,0]]
        #In order to loop the list in the same way the actual E source list works. should not effect calculation as this looped value's charge will be set to 0 for testing
        T1_E_source_pos_list.append(T1_E_source_pos_list[0])
        T1_E_source_chargedensity_list = [1,0]
        T1_E_source_chargedensity_list.append(0)
        
        T1_E_plate_radius = 1
        T1_Path_rad = 1
        T1_num_E_source =2


        Testing_state=[T1_state_pos, T1_state_vel, T1_state_charge,T1_state_mass, T1E_plate_index, [T1_E_source_pos_list, T1_E_source_chargedensity_list, T1_E_plate_radius, T1_Path_rad, T1_num_E_source]]
        Expected_solution=[5.0851478114*10**10,0,0]
        return(Testing_state,Expected_solution)

class M_Teststates():
    def Teststate_1():
        T1_mass = 1
        T1_Vel = np.array([1,0,0], dtype=float)
        T1_charge = 1
        T1_PathRad = 10

        Testing_state=[T1_mass,T1_Vel,T1_charge,T1_PathRad]
        Expected_solution=[0,0,-0.1]
        return(Testing_state,Expected_solution)

class Kin_Teststates():
    def Teststate_1():
        "Tregetory of a ball"
        T1_Pos =[0,0,0]
        T1_Vel = [10,0,40]
        T1_Acc = [0,0,-9.81]
        T1_Mass = 1
        T1_Charge = 0
        T1_Acc_dt1 = [0,0,0.01]
        T1_Acc_dt2 = [0,0,0.01]
        Name='Ball'
        T1_DeltaT = 0.01
        T1_Time = 10
        E_plate_index = 0
        KE=0
        #Entryformat= ([initPos], [initVel], [initAcc],[Accdt1],[Accdt2], [Name], [Mass],[Charge],KE, [deltaT],E_plate_index)
        Testing_state=[[T1_Pos, T1_Vel, T1_Acc, T1_Acc_dt1, T1_Acc_dt2, Name, T1_Mass, T1_Charge,KE, T1_DeltaT, E_plate_index],T1_Time]
        Expected_solution=[(np.array(T1_Pos))+(np.array(T1_Vel)*T1_Time)+0.5*(np.array(T1_Acc)*T1_Time**2)+(np.array(T1_Acc_dt1)*T1_Time**3)/6+((np.array(T1_Acc_dt2)*T1_Time**4))/24]
        #print(Expected_solution[0][2])
        return(Testing_state,Expected_solution)
    Teststate_1()