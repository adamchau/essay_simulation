# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/ydzhao/.spyder2/.temp.py
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import control as control


A,B,C,D=0,1,1,0        
agent_model=control.ss(A,B,C,D)
    
    
    

x0=0
x_init=x0

data_u=control.step(agent_model, T=None, X0=x_init, input=0, output=None)
x_init=data_u[0][-1]
t_init=data_u[1][-1]
data_u=control.step(agent_model, T=None, X0=x_init, input=0, output=None)

u=1
T, yout, xout=control.forced_response(agent_model, T=array([0,0.01]), U=1, X0=1)


plt.plot(data_u[1],data_u[0])
plt.show()