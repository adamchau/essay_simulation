# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 13:35:36 2014

@author: ydzhao
"""

import networkx as nx
import numpy as np
L=np.matrix([[1,-1,0,0],[-1,3,-1,-1],[0,-1,2,-1],[0,-1,-1,2]])
D=np.matrix(np.diag(np.diag(L)))
A=D-L
G=nx.from_numpy_matrix(A)
nx.draw(G)