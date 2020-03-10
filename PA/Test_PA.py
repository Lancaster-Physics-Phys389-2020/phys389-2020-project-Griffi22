import pytest
import numpy as np
import scipy.constants as const
import Test_states
from Field_effect import Field_effect
from P_state_update import Update
class test_master():

    def test_E_fields(TestState_n):
        "creating a test enviroment with calculated analitical solutions"
        Test_state=Test_states.E_Teststates.Teststate_1()

        Testing_state=Test_state[0]
        Expected_solution=Test_state[1]

        Function_solution=Field_effect(None, True, Testing_state)
        np.testing.assert_allclose(Function_solution.E_effect()[0], Expected_solution, rtol=0.00001) 
        print(100*(Expected_solution[0]-Function_solution.E_effect()[0][0])/(Expected_solution[0])," % ", "difference from expected value")


    def test_M_fields(TestState_n):
        Test_state=Test_states.M_Teststates.Teststate_1()

        Testing_state=Test_state[0]
        Expected_solution=Test_state[1]
        Function_solution=Field_effect.M_effect(None,True,Testing_state)

        np.testing.assert_allclose(Function_solution, Expected_solution, rtol=0.00001) 
        print(100*(Expected_solution[2]-Function_solution[2])/(Expected_solution[2])," % ", "difference from expected value")
    
    def test_kinimatic_updater(Teststate_n):
        Test_state=Test_states.Kin_Teststates.Teststate_1()
        Testing_state=Test_state[0]
        Expected_solution=Test_state[1]
        for Time_i in range(0,Test_state[0][8]):
            Current_state=Update.update(None,True,Testing_state)
            Testing_state=Current_state
        Function_solution=Current_state[0]

        np.testing.assert_allclose(Function_solution, Expected_solution, rtol=0.00001)
        print(100*(Expected_solution[2]-Function_solution[2])/(Expected_solution[2])," % ", "difference from expected value")
