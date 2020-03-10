import numpy as np
import math
import copy
import scipy.constants as const
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d
import timeit
import pandas as pd
from Fields import fields
#from Field_effect import Field_effect
from P_state_update import Update
from Particle_list import Particle_data_list as PDL



"All values are in SI units throughout the model."



class Simulation:
    "starting a program run timer"
    start = timeit.default_timer()
    "inital class variables"
    #time variables
        #start time
    T_i=0
        #end time (adjusted so timestep is accounted for)
    T_f=round(0.1/PDL.DeltaT)
    
#    Particle selection
    print("Particle list: Proton, Electron, Positron, Pion+, Pion-, Koan+, Kaon-")
#    particle_input=input("Enter particle to simulate: ")
    
#For speed of development (delete for final)
    particle_input="Proton"

    #calling the selected particle
    
    Particle_state=PDL.Particle_list[particle_input]

    #creating the empty the dataframe
    data_np=pd.DataFrame([{'Time': [], 'Pos': [],'Vel': [],'Acc': [],'KE': []}])
#    running simulation over timesteps
    
    for t in range(T_i,T_f):
#        pos,vel,acc dat for a selected particle being updated
        Particle_state.update()
#        KE of particle being updated
        Particle_state.KineticEnergy()
#       adding updated particle state variables to the datalist
        data_np=data_np.append([{'Time': t, 'Pos': list(Particle_state.pos), 'Vel': list(Particle_state.vel),'Acc': list(Particle_state.acc),'Acc_dt1': list(Particle_state.Acc_dt1),'KE': Particle_state.KE}],ignore_index=True)
#    Dev feature to look at values
    print(data_np['Time'],data_np['Pos'],data_np['Vel'],data_np['Acc'])

#    creating a dataframe to hold Electric feild position data
    E_prop_list=fields.E_prop_list()
    E_pos_list=pd.DataFrame([{'E_pos': list(E_prop_list[0][0])}])
    for i in range(1,len(E_prop_list[0])):
        E_pos_list=E_pos_list.append([{'E_pos': list(E_prop_list[0][i])}],ignore_index=True)

    
#    Plotting the position of the particle and the feild sources
    threedee = plt.figure(0).gca(projection='3d')
    plt.title("Particle path")
#    plotting the specific entry lists (e.g the x comp of the position etc) from the dataframes
    threedee.plot(data_np['Pos'].str[0], data_np['Pos'].str[1],data_np['Pos'].str[2])
    threedee.plot(E_pos_list['E_pos'].str[0],E_pos_list['E_pos'].str[1],E_pos_list['E_pos'].str[2], 'o',markersize=0.2)
    #Setting the axes properties
    threedee.set_xlabel('Pos x')
    threedee.set_ylabel('Pos y')
    threedee.set_zlabel('Pos z')
    
    lota_plota=False
    if lota_plota==True:
        plt.figure(1)
        plt.title("Particle Vel Y")
    #    plotting the specific entry lists (e.g the x comp of the position etc) from the dataframes
        plt.plot(data_np['Vel'].str[0],data_np['Vel'].str[1])
        
        plt.figure(2)
        plt.title("Particle Acc Y")
    #    plotting the specific entry lists (e.g the x comp of the position etc) from the dataframes
        plt.plot(data_np['Acc'].str[0],data_np['Acc'].str[1])
        
        plt.figure(3)
        plt.title("Particle Acc_dt1 Y")
    #    plotting the specific entry lists (e.g the x comp of the position etc) from the dataframes
        plt.plot(data_np['Acc_dt1'].str[0],data_np['Acc_dt1'].str[1])
#        plt.yscale("log")
#        plt.ylim(10**1,10**9)
        
    animate=True
    if animate==True:
    
#    Plotting an animation of the particles path
        fig = plt.figure(4)
        ax =  mpl_toolkits.mplot3d.axes3d.Axes3D(fig)
        
#    creating an empty list for the particle position data and then additing the data enrty by entry.
        gen_=[]
        i=1
        while i < len(data_np):
            gen_.append(np.array([data_np['Pos'].str[0][i],data_np['Pos'].str[1][i],data_np['Pos'].str[2][i]]))
            i += 1
    #        sets animation line to follow the particle position data
        def update(num, data, line):
            line.set_data(data[:2, :num])
            line.set_3d_properties(data[2, :num])
        
        data = np.array(list(gen_)).T
        line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1]) #nope, no error here.
        
        #Setting the axes properties
        ax.set_xlim3d([10000, -10000])
        ax.set_xlabel('X')
        
        ax.set_ylim3d([-10000, 10000])
        ax.set_ylabel('Y')
        
        ax.set_zlim3d([-2, 2])
        ax.set_zlabel('Z')
    #    animation command to create the animation
        ani = animation.FuncAnimation(fig, update, len(data_np), fargs=(data, line), interval=1, blit=False)
    stop = timeit.default_timer()
    print('Run Time: ', stop - start)  
    

    plt.show()
    

    
