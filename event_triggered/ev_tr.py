# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 22:22:11 2014

@author: ydzhao
"""

from mas_class import *

if __name__=="__main__":
    L=np.matrix([[1,-1,0,0],[-1,3,-1,-1],[0,-1,2,-1],[0,-1,-1,2]])
    topology=create_graph_from_laplacian(L)
    sim_times=800
    '''
           mas topology
    '''  
    nx.draw_networkx(topology)
    sim_type=3    
   
    def sim_mas():
        agent1=mas_agent(0,1,1,0,1)
        agent2=mas_agent(0,1,1,0,2)
        agent3=mas_agent(0,1,1,0,3)
        agent4=mas_agent(0,1,1,0,4)
        agent_list=[agent1,agent2,agent3,agent4]
        global MAS1
        MAS1=mas_sys(agent_list,topology)
        for N in range(sim_times):
            MAS1.mas_pro_applied(0.01)
    
    def sim_ev_mas_cen():        
        agent1=mas_agent(0,1,1,0,1)
        agent2=mas_agent(0,1,1,0,2)
        agent3=mas_agent(0,1,1,0,3)
        agent4=mas_agent(0,1,1,0,4)  
        agent_list=[agent1,agent2,agent3,agent4]
        global ev_MAS1
        ev_MAS1= event_triggered_mas_sys_centralized(agent_list,topology,0.99)    
        for N in range(sim_times):
            ev_MAS1.mas_pro_applied(0.01)        
    
    def sim_ev_mas_dis():    
        agent1=mas_agent(0,1,1,0,1)
        agent2=mas_agent(0,1,1,0,2)
        agent3=mas_agent(0,1,1,0,3)
        agent4=mas_agent(0,1,1,0,4)  
        agent_list=[agent1,agent2,agent3,agent4]
        sigma=[0.99,0.99,0.99,0.99]
        a=0.2
        '''
         a的取值必须满足0<a<1/|N_i|,也就是说,0<a<1/N_max,其中 N_max=max(topology.degree),本例为1/3
        '''
        global ev_dis_MAS1
        ev_dis_MAS1=event_triggered_mas_sys_distributed(agent_list,topology,sigma,a)
        for N in range(sim_times):
            ev_dis_MAS1.mas_pro_applied(0.01)     
            
    switch_dict={1:sim_mas,2:sim_ev_mas_cen,3:sim_ev_mas_dis}
    switch_dict[sim_type]()
      