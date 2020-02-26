import numpy as np
import math
import copy
import scipy.constants as const
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from Fields import fields
#from Field_effect import Field_effect
from P_state_update import Update
from Particle_list import Particle_data_list as PDL



'My file for ideas and workings:       ignore this file'


#iniial input particle=(pos,vel,acc,name,mass,charge)
#a=np.array([1,1,1])
#b=np.array([2,2,2])
#print(a)
#print(b)
#List=[a,b]
#print(List[0])
#
#print(fields.E_prop_list()[0])
#E=np.array(fields.E_prop_list()[0])
#print(np.linalg.norm(E),'newshiz')
#
#
#N=[[0,0,0],[1,1,1]]
#df=pd.DataFrame([{'Ns': list(N)}])
#print(df)
#print(df['Ns'])
#print(df['Ns'][0])
#print(df['Ns'][0][1])
#print(df['Ns'][0][1][2])
#
##
#print(const.epsilon_0)
#
#cir_x=(100**2-y^**2)**0.5
#B=[[pos/dx],[pos/dy],[pos/dz]]