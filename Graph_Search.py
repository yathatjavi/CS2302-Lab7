# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:22:25 2019

@author: yatha
"""
# Implementation of simple graph operations 
# Programmed by Olac Fuentes
# Last modified April 15, 2019
import random
import dsf
import numpy as np
import matplotlib.pyplot as plt
import math
from queue import *

'''
will take an adjacency matrix and return the adjacency list representation
of the graph
'''
def AM_to_AL(AM):
    AL = Create_AL(len(AM))
    
    for i in range(len(AM)):
        for j in range(len(AM[i])):
            if AM[i][j] == True:
                AL[i].append(j)
                #AL[j].append(i)
    return AL


def breadth_first_search(G,v):
    #will take a graph represented as Adjaceny list and return an array 
    #containng the previous vertex of that index
    visited = np.full(len(G), False, dtype=bool)
    prev = np.full(len(G), -1, dtype=int)
    #Q holds items discoverd be still needing to be visited
    Q = Queue(maxsize=0)
    Q.put(v)
    visited[v] = True
    
    while not Q.empty():
        u = Q.get(0)
        #will print the traversal order
        #print(u)
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.put(t)
    
    return prev

def depth_first_search(G,source,visited,prev):
    visited[source] = True
    
    for t in G[source]:
        if not visited[t]:
            prev[t] = source
        depth_first_search(G,t,visited,prev)
    print(prev)

def depth_first_iter(G,v):
    #will take a graph represented as Adjaceny list and return an array 
    #containng the previous vertex of that index
    visited = np.full(len(G), False, dtype=bool)
    prev = np.full(len(G), -1, dtype=int)
    #S holds items discoverd be still needing to be visited
    S = []
    S.append(v)
    visited[v] = True
    
    while len(S)>0:
        u = S.pop(-1)
        #will print the traversal order
        #print(u)
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                S.append(t)
    
    return prev
    

def Create_AM(rows,cols):
    #will create 2d list of false type boolean
    #given the size of rows*columns
    x =[]
    for i in range(rows):
        x.append(False)
        
    AM =[]
    for i in range(cols):
        AM.append(x)
    return AM

def True_AM(rows,cols):
    x =[]
    for i in range(rows):
        x.append(True)
        
    AM =[]
    for i in range(cols):
        AM.append(x)
    return AM

'''
 #creates an empty Adjacency list 
'''
def Create_AL(vertices):
   
    temp = []
    AL =[]
    for i in range(vertices):
        AL.append(temp)
    return AL



def dijkstra(G,source):
    Known = np.full(len(G), False, dtype=bool)
    prev = np.full(len(G), -1, dtype=int)
    dist = np.full(len(G), sys.maxint, dtype=int)
    dist[source] =0
    knownVertices = 0
    
    while KnownVertices < len(G):
        return
    return


def adj_list_to_adj_mat(G):
    g = np.zeros((len(G),len(G)),dtype=bool)
    for source in range(len(G)):
        for dest in G[source]:
            g[source,dest] = True
            g[dest,source] = True  #Comment out if graph is directed
    return g


def adj_list_to_edge_list(G):
    g = []
    for source in range(len(G)):
        for dest in G[source]:
            if dest>=source: #ignore duplicate edges
                g.append([source,dest])
    return g


def random_graph(vertices, edges, duplicate=False):
    # Generates random graph with given number of vertices and edges
    # If duplicate is true, each edge is included twice in the list
    # that is, for edge (u,v), u is in G[v] and v is in G[u]
    G = [ [] for i in range(vertices) ]
    n=0
    while n<edges:
        s = random.randint(0, vertices-1)
        d = random.randint(0, vertices-1)
        if s<d and d not in G[s]:
            G[s].append(d)
            if duplicate:
                G[d].append(s)
            n+=1
    return G

def random_graph2(vertices):
    G =[]
    for i in range(vertices):
        G.append([])
    for s in range(vertices):
        d = random.randint(1, vertices-1)
        d = (d+s)%vertices
        G[s].append(d)
    return G

def connected_components(G,diplay_dsf=False):
    S= dsf.DisjointSetForest(len(G))
    for source in range(len(G)):
        for dest in G[source]:
            dsf.union_by_size(S,source,dest)
            if diplay_dsf:
                dsf.draw_dsf(S)
    return dsf.NumSets(S), S
        
def draw_graph(G):
    fig, ax = plt.subplots()
    n = len(G)
    r = 30
    coords =[]
    for i in range(n):
        theta = 2*math.pi*i/n+.001 # Add small constant to avoid drawing horizontal lines, which matplotlib doesn't do very well
        coords.append([-r*np.cos(theta),r*np.sin(theta)])
    for i in range(n):
        for dest in G[i]:
            ax.plot([coords[i][0],coords[dest][0]],[coords[i][1],coords[dest][1]],
                     linewidth=1,color='k')
    for i in range(n):
        ax.text(coords[i][0],coords[i][1],str(i), size=10,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.set_aspect(1.0)
    ax.axis('off') 

if __name__ == "__main__":     

    plt.close("all")   
    random.seed(a=86)
    #G=random_graph(8,6,True)
    #draw_graph(G)
    #print('Adjacency list representation:')
    #print(G)
    #AM = adj_list_to_adj_mat(G)
    #print('Adjacency matrix representation:')
    #print(AM)
    #print('Edge list representation:')
    #EL = adj_list_to_edge_list(G)
    #print(EL)
    #n,S = connected_components(G,True)
    #print('Connected components=',n)
    #dsf.draw_dsf(S)
    #print('Sets:',dsf.dsfToSetList(S))
      

    AM = [[False, False, True, True, False],
          [False, False, True, True, False],
          [True, True, False, False, True],
          [True, True, False, False, True],
          [False, False, True, True, False]]
    
    AL= [[2,3],
         [3,2],
         [0,1,4],
         [0,1,4],
         [2,3]]
    
    EL = [[0,2],[0,3], [1,3], [1,2], [2,4], [3,4]]
    visited = np.full(len(AL), False, dtype=bool)
    prev = np.full(len(AL), -1, dtype=int)
    
    #draw_graph(AL)
    test = breadth_first_search(AL,0)
    print(test)
    print(depth_first_iter(AL,0))
   # depth_first_search(AL,0,visited,prev)