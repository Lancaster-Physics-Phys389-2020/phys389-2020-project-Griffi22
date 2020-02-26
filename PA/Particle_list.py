import numpy as np
import math
import copy
import scipy.constants as const
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from P_state_update import Update


#Entryformat= ([initPos], [initVel], [initAcc], [Name], [Mass],[Charge], [deltaT])
class Particle_data_list:
#    DeltaT=float(input("deltaT: "))
#    automatic setting deltaT for speed of dev delete later
    DeltaT=0.1
#    defining the list of particles and their inital properties for simlation
    Particle_list={'Proton':Update([100,0.0001,0],[0,10,0],[0,0,0],'Proton',const.m_p,const.elementary_charge,0, DeltaT),
                   'Electron':Update([0,0,0],[0,0,0],[0,0,0],'Electron',1,-1,0, DeltaT),
                   'Positron':Update([0,0,0],[0,0,0],[0,0,0],'Positron',1,1,0, DeltaT),
                   'Pion+':Update([0,0,0],[0,0,0],[0,0,0],'Pion+',1,1,0, DeltaT),
                   'Pion-':Update([0,0,0],[0,0,0],[0,0,0],'Pion-',1,-1,0, DeltaT),
                   'Kaon+':Update([0,0,0],[0,0,0],[0,0,0],'Kaon+',1,1,0, DeltaT),
                   'Kaon-':Update([0,0,0],[0,0,0],[0,0,0],'Kaon-',1,-1,0, DeltaT)}