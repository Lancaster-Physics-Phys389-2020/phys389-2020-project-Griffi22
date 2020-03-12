import pytest
import numpy as np
import scipy.constants as const
import TestStates
from Field_effect import Field_effect
from P_state_update import Update
class test_master():

    def test_E_fields():
        "creating a test enviroment with calculated analitical solutions"
        Test_state=TestStates.E_Teststates.Teststate_1()

        Testing_state=Test_state[0]
        Expected_solution=Test_state[1]

        Function_solution=Field_effect(None, True, Testing_state)
        np.testing.assert_allclose(Function_solution.E_effect()[0], Expected_solution, rtol=0.00001) 
        print(100*(Expected_solution[0]-Function_solution.E_effect()[0][0])/(Expected_solution[0])," % ", "difference from expected value")


    def test_M_fields():
        Test_state=TestStates.M_Teststates.Teststate_1()

        Testing_state=Test_state[0]
        Expected_solution=Test_state[1]
        Function_solution=Field_effect.M_effect(None,True,Testing_state)

        np.testing.assert_allclose(Function_solution, Expected_solution, rtol=0.00001) 
        print(100*(Expected_solution[2]-Function_solution[2])/(Expected_solution[2])," % ", "difference from expected value")
    
    def test_kinimatic_updater():
        Test_state=TestStates.Kin_Teststates.Teststate_1()
        #print(Test_state[0][0])
        Testing_state=Update(Test_state[0][0])
        Expected_solution=Test_state[1]

        for Time_i in range(0,round(Test_state[0][1]/Test_state[0][0][9])):
            Testing_state.update(True)
        Function_solution=Testing_state.pos
        np.testing.assert_allclose(Function_solution, Expected_solution[0], rtol=0.00001)
    test_kinimatic_updater()