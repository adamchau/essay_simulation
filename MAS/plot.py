# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 17:23:56 2014

@author: ydzhao
"""

for i in range(MAS1.agent_num):
     agent1_var=[data[i] for data in MAS1.status_his]
     plt.plot(MAS1.T[0:5000],agent1_var[0:5000])