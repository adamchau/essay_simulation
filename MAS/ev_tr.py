# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 22:22:11 2014

@author: ydzhao
"""

from mas_class import *
import copy as cp

if __name__=="__main__":
    L=np.matrix([[1,-1,0,0],[-1,3,-1,-1],[0,-1,2,-1],[0,-1,-1,2]])
    topology=create_graph_from_laplacian(L)
    agent1=mas_agent(0,1,1,0,1)
    agent2=mas_agent(0,1,1,0,2)
    agent3=mas_agent(0,1,1,0,3)
    agent4=mas_agent(0,1,1,0,4)
    agent_list=[agent1,agent2,agent3,agent4]
    MAS1=mas_sys(agent_list,topology)
    for N in range(4000):
        MAS1.mas_pro_applied(0.01)

    agent1=mas_agent(0,1,1,0,1)
    agent2=mas_agent(0,1,1,0,2)
    agent3=mas_agent(0,1,1,0,3)
    agent4=mas_agent(0,1,1,0,4)  
    agent_list=[agent1,agent2,agent3,agent4]
    ev_MAS1= event_triggered_mas_sys(agent_list,topology,0.99)    
    for N in range(4000):
        ev_MAS1.mas_pro_applied(0.01)