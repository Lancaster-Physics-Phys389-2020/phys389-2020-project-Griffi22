import numpy as np
import math
import copy
import scipy.constants as const
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
import pandas as pd
from Fields import fields
#from Field_effect import Field_effect
from P_state_update import Update
from Particle_list import Particle_data_list as PDL
from c1 import C1

class C0:
    objacked=C1(0)
    for i in range(0,5):
        objacked.updater()
        print(objacked.objacked_value)




















#Epos=[[0,0],[1,0],[1,1]]
#Epos_loop=cycle(Epos)
##for Epos_i in Epos_loop:
##print(Epos_loop[12])
#i=0
#print(len(fields.E_prop_list()[0]))
#while i<len(fields.E_prop_list()[0])+2:
#    print(i)
#    Phi_E_i1=round(np.angle(fields.E_prop_list()[0][i+1][0]+fields.E_prop_list()[0][i+1][1]*1j, deg=True)%360)
#    Phi_E_i0=round(np.angle(fields.E_prop_list()[0][i][0]+fields.E_prop_list()[0][i][1]*1j, deg=True)%360)
#    if Phi_E_i1>Phi_E_i0 or i==len(fields.E_prop_list()[0])-2:
#        print('big money')
#    i+=1
#    i=i%(len(fields.E_prop_list()[0])-1)
#    print(Phi_E_i0,Phi_E_i1)

'My file for ideas and workings:       ignore this file'
#y=[100,50,0,-50,-100,-50,0,50,100]
#x=[0,50,100,50,0,-50,-100,-50,0]
#pos_r=np.array([1,1], dtype=float)
#pos_I=pos_r[0]+1j*pos_r[1]
#print(pos_I)
#print(np.angle(pos_r[0]+1j*pos_r[1], deg=True)%360) 


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