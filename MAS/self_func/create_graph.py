# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 14:39:30 2014

@author: ydzhao
"""

import networkx as nx
import numpy as np
def create_graph_from_laplacian(L):
    L=np.matrix([[1,-1,0,0],[-1,3,-1,-1],[0,-1,2,-1],[0,-1,-1,2]])
    D=np.matrix(np.diag(np.diag(L)))
    A=D-L
    G=nx.from_numpy_matrix(A)
    return G
    
if  __name__ == "__main__":
    L=np.matrix([[1,-1,0,0],[-1,3,-1,-1],[0,-1,2,-1],[0,-1,-1,2]])
    G=create_graph_from_laplacian(L)
    nx.draw_networkx(G)
    info_neb0=[G.node[n]  for n in G[0]]