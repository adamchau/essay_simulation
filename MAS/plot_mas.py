# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 09:07:07 2014

@author: ydzhao
"""
from ev_tr import *

if __name__=="__main__":
        '''
            mas consensus
        '''
        plt.figure()
        for i in range(MAS1.agent_num):
            agent1_var=[data[i] for data in MAS1.status_his]
            plt.plot(MAS1.T,agent1_var)
        
        '''
            event-triggered consensus
        '''
        plt.figure()
        for i in range(ev_MAS1.agent_num):
            agent1_var=[data[i] for data in ev_MAS1.status_his]
            plt.plot(ev_MAS1.T,agent1_var)
            
        plt.figure()
        plt.plot(ev_MAS1.T[0:800],ev_MAS1.error_his[0:800])
        plt.plot(ev_MAS1.T[0:800],ev_MAS1.bound_his[0:800])
        
        