# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:46:17 2020

@author: User
"""

import networkx as nx
import matplotlib.pyplot as plt

# Create empty graph
G = nx.Graph()

#List of edges
edges = []
nodes = []

# Add stairwell A nodes
def add_stairsA(floors, stairwell):
    G.add_node('SWA1', capacity=50)
    G.add_node('SWA2', capacity=60)
    for i in range(floors):
        if (i > 1):
            name = ''
            stairs = 'SW' + stairwell
            level = ''
            level += str(i+1)
            name = stairs + str(level)
            G.add_node(name, capacity=20)
            
# Add stairwell B nodes
def add_stairsB(floors, stairwell):   
    for i in range(floors):
        if (i >= 1):  # No stairs level 1
            name = ''
            stairs = 'SW' + stairwell 
            level = ''
            level += str(i+1)
            name = stairs + str(level)
            G.add_node(name, capacity=20)
        
# Add hallway nodes
def add_halls(floors):
    
    for i in range(floors):
        if (i > 0 and i < 4):
            name = ''
            level = ''
            hall = 'H'
            level += str(i + 1)
            name = hall + level
            G.add_node(name, capacity=140)
    G.add_node('H5', capacity=100)
    G.add_node('H6', capacity=100)
    G.add_node('H7', capacity=100)
    G.add_node('H8', capacity=100)
    G.add_node('H9', capacity=80)
    G.add_node('H10', capacity=120)
    G.add_node('H11', capacity=100)
    G.add_node('HC6', capacity=40)
    G.add_node('HC7', capacity=40)
    G.add_node('HC8', capacity=40)
    G.add_node('HC9', capacity=30)
    G.add_node('HC11', capacity=40)

# Number of floors in building
floors = 11  
SWA = add_stairsA(floors, 'A')
SWB = add_stairsB(floors, 'B')
halls = add_halls(floors)
G.nodes.data()

# Add a node


print(nx.info(G))
nx.draw(G)
