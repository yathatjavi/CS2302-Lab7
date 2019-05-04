# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:19:59 2019

@author: yatha
"""

import dsf
import draw_maze as DM
import Graph_Search as GS
import numpy as np

def solve_Maze(AL):
    search_type=int(input("For Breadth-first search enter(1) for Depth-first search enter (2)  for Depth-first search with recursion enter (3)"))
    if search_type == 1:
        print("Breadth-first search selected")
        print(GS.breadth_first_search(AL,0))
    elif search_type == 2:
        print('Depth-first search selected')
        return
    else:
        print('Depth-first search with recursion selected')
        return
'''
will take a list/dsf and return an adjacency matrix representation
'''
def list_to_AM(L,length,height):
    num_cells = length*height
    AM = np.full((num_cells,num_cells),True,dtype=bool)
    for i in range(len(L)):
        left = L[i][0]
        right = L[i][1]
        AM[left][right]=False
        AM[right][left]=False
    return AM


def Send_It():
    maze_rows =5
    maze_cols = 5
    maze_size= maze_rows *maze_cols
    nMinOne = maze_size-1
    Print = False
    
    if maze_rows < 500 and maze_cols <500:
        Print = True
        
    walls = DM.wall_list(maze_rows,maze_cols)
    
    print('There are ',maze_size, " cells in this maze.", end=" ")
    m= int(input("How many walls would you like to remove?"))
    print()
    
    if nMinOne == m:
        print('There is a unique path from source to destination.')
        #method has been overloaded since original uses golbal variables
        walls =DM.remove_walls_c(walls,Print,maze_rows,maze_cols)
        
        AM =list_to_AM(walls,maze_rows,maze_cols) 
        AL = GS.AM_to_AL(AM)
        #denug here
     
        solve_Maze(AL)
       
    elif m< nMinOne:
        print('A path from source to destination is not guaranteed to exist.')
        #DM.remove_x_walls(walls, sets,Print,maze_rows,maze_cols,m)
        walls =DM.remove_x_walls(walls,Print,maze_rows,maze_cols,m)
         
        
    else:
        print('There is at least one path from source to destination')
        walls =DM.remove_x_walls(walls,Print,maze_rows,maze_cols,m)
        
        
        #for i in range(len(AM)):
            #print(AM[i])
        
   
Send_It()
        