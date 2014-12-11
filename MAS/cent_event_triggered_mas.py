# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 18:10:41 2014

@author: ydzhao
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 15:17:13 2014

@author: ydzhao
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import control as control
import networkx as nx

class mas_sys:
    def __init__(self,agent_list,topology):
        self.agent_list=agent_list
        self.agent_num=len(agent_list)
        self.G=topology
        self.init_state=[ag.state for ag in agent_list]
        self.status=self.init_state
        self.t=0
        self.T=[0]
        self.status_his=[self.status]
        self.neighbor_set=[]
        for node_i in range(self.agent_num):
            self.G.node[node_i]=self.agent_list[node_i]
            i_node_neighbor_list=[n for n in self.G[node_i]]
            self.neighbor_set.append(i_node_neighbor_list)
    
    def draw_mas_sys(self):
        plt.figure()
        nx.draw_networkx(self.G)
        
    def mas_protocol(self,i):
        '''
        使用协议
        '''
        N=len(self.neighbor_set[i])
        state_set=[self.G.node[n].state for n in self.neighbor_set[i]]
        u=np.sum(state_set)-N*self.G.node[i].state
        return u
        
    def update_mas_status(self):
        self.status=[self.G.node[i].state for i in range(self.agent_num)]
        
    def agent_u_applied(self,i,T_intval):
        ui=self.mas_protocol(i)
        self.G.node[i].input_sim(ui,0.01)
    
    def mas_pro_applied(self,T_intval):
        for i in range(self.agent_num):
           self. agent_u_applied(i,T_intval)
        self.t+=T_intval
        self.T.append(self.t)
        self.update_mas_status()
        self.status_his.append(self.status)

class event_triggered_mas_sys:
    def __init__(self,agent_list,topology,status_ref,sigma):
        self.agent_list=agent_list
        self.status_ref=status_ref
        self.sigma=sigma
        self.agent_num=len(agent_list)
        self.G=topology
        self.L=nx.laplacian_matrix(topology)
        self.init_state=[ag.state for ag in agent_list]
        self.status=self.init_state
        self.status_sim=self.status
        self.status_keep=self.status
#        保持的状态
        self.t=0
        self.T=[0]
        self.triggeredT=[0]
        self.error_his=[0]
        self.trigger_bound()
        self.bound_his=[self.bound]
        self.status_his=[self.status]
        self.neighbor_set=[]
        for node_i in range(self.agent_num):
            self.G.node[node_i]=self.agent_list[node_i]
            i_node_neighbor_list=[n for n in self.G[node_i]]
            self.neighbor_set.append(i_node_neighbor_list)
            
    def update_status_sim(self):
        self.status_sim=self.status_ref.pop(0)
    
    def draw_mas_sys(self):
        plt.figure()
        nx.draw_networkx(self.G)
        
    def mas_protocol(self,i):
        '''
        使用协议,event-triggered
        '''
        N=len(self.neighbor_set[i])
        state_set=[self.status_keep[n] for n in self.neighbor_set[i]]
        u=np.sum(state_set)-N*self.G.node[i].state
        return u
        
        
    def update_mas_status(self):
        self.status=[self.G.node[i].state for i in range(self.agent_num)]
        
    def error_estimate(self):
        self.error_norm=np.linalg.norm(np.array(self.status_sim)-np.array(self.status_keep))
        
    def trigger_bound(self):
         self.bound=(np.linalg.norm(self.L*np.array(self.status_sim)))/np.linalg.norm(np.matrix(self.L.toarray()))
    
    def triggered_judge(self,sigma):
        self.error_estimate()
        self.trigger_bound()
        if (self.error_norm)>(sigma*self.bound):
             self.status_keep=self.status_sim
             self.triggeredT.append(self.t)

    def agent_u_applied(self,i,T_intval):
        ui=self.mas_protocol(i)
        self.G.node[i].input_sim(ui,0.01)
    
    def mas_pro_applied(self,T_intval):
        self.update_status_sim()
        self.triggered_judge(self.sigma)
        self.bound_his.append(self.bound)
        self.error_his.append(self.error_norm)
        for i in range(self.agent_num):
           self. agent_u_applied(i,T_intval)
        self.t+=T_intval
        self.T.append(self.t)
        self.update_mas_status()
        self.status_his.append(self.status)
        
        
        

        
class mas_agent:
    def __init__(self,A=0,B=1,C=1,D=0,x0=1):
        self.agent_model=control.ss(A,B,C,D)
        self.x0=x0
        self.state=x0
        
    def input_sim(self,u=0,T_intval=0.01):
        T, yout, xout=control.forced_response(self.agent_model, np.array([0,T_intval]), u, self.state)
        self.state=yout[-1]

def create_graph_from_laplacian(L):
    D=np.matrix(np.diag(np.diag(L)))
    A=D-L
    G=nx.from_numpy_matrix(A)
    return G
        
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
    for i in range(MAS1.agent_num):
        agent1_var=[data[i] for data in MAS1.status_his]
        plt.plot(MAS1.T,agent1_var)
    
    
        
    
    