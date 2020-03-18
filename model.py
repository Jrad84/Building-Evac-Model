# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:46:17 2020

@author: User
"""

import networkx as nx
import matplotlib.pyplot as plt

# Create empty graph
G = nx.Graph()

#List of edges & nodes
edges = []
nodes = []

# Number of floors in building
floors = 11  

# Add stairwell A nodes
def add_stairsA(floors, stairwell):
    
    for i in range(floors):
        if (i > 2):
            name = ''
            stairs = 'SW' + stairwell
            level = ''
            level += str(i+1)
            name = stairs + str(level)
            G.add_node(name, capacity=20)
    G.add_node('SWA1', capacity=50)
    G.add_node('SWA2', capacity=60)
            
# Add stairwell B nodes
def add_stairsB(floors, stairwell):   
    for i in range(floors):
        if (i > 2):  
            name = ''
            stairs = 'SW' + stairwell 
            level = ''
            level += str(i+1)
            name = stairs + str(level)
            G.add_node(name, capacity=20)
    G.add_node('SWB2', capacity=60)
    G.add_node('SWB0', capacity=100)
    
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

swa_nodes = add_stairsA(floors, 'A')
swb_nodes = add_stairsB(floors, 'B')
halls = add_halls(floors)
# Elevators
G.add_node('EL9', capacity=50)
G.add_node('LEL9', capacity=50)
G.add_node('EL5', capacity=50)
G.add_node('LEL5', capacity=50)

# Work Centres
G.add_node('WC6', capacity=13)
G.add_node('WC7', capacity=12)
G.add_node('WC8', capacity=15)
G.add_node('WC9', capacity=10)
G.add_node('W10', capacity=29)
G.add_node('W9', capacity=34)
G.add_node('W8', capacity=22)
G.add_node('W7', capacity=13)
G.add_node('W6', capacity=27)
G.add_node('W5', capacity=32)
G.add_node('W4', capacity=33)
G.add_node('W3', capacity=33)
G.add_node('W2', capacity=31)

G.add_node('DUMMY', capacity=64)
G.add_node('RCPD', capacity=100)
G.add_node('PCD', capacity=100)
G.add_node('TRNF')
G.add_node('TRNS')
G.add_node('TRNC')
G.add_node('EXIT')

# Edges
G.add_edge('WC11', 'HC11', capacity=7)
G.add_edge('LEL9', 'DUMMY', capacity=32)
G.add_edge('LEL5', 'DUMMY', capacity=32)
G.add_edge('DUMMY', 'RCPD', capacity=64)
G.add_edge('RCPD', 'PCD', capacity=7)
G.add_edge('PCD', 'RCPD', capacity=14)
G.add_edge('PCD', 'SWB0', capacity=14)
G.add_edge('SWB0', 'PCD', capacity=7)
G.add_edge('W2', 'H2', capacity=90)
G.add_edge('W3', 'H3', capacity=120)
G.add_edge('W4', 'H4', capacity=95)
G.add_edge('W5', 'H5', capacity=80)
G.add_edge('W6', 'H6', capacity=135)
G.add_edge('W7', 'H7', capacity=65)
G.add_edge('W8', 'H8', capacity=45)
G.add_edge('W9', 'H9', capacity=70)
G.add_edge('W10', 'H10', capacity=85)
G.add_edge('W11', 'H11', capacity=45)
G.add_edge('WC11', 'HC11', capacity=7)
G.add_edge('WC9', 'HC9', capacity=7)
G.add_edge('WC8', 'HC8', capacity=7)
G.add_edge('WC7', 'HC7', capacity=7)
G.add_edge('WC6', 'HC6', capacity=7)
G.add_edge('HC11', 'SWB11', capacity=21)
G.add_edge('HC9', 'SWB9', capacity=21)
G.add_edge('HC8', 'SWB8', capacity=21)
G.add_edge('HC7', 'SWB7', capacity=21)
G.add_edge('HC6', 'SWB6', capacity=21)
G.add_edge('SWB2', 'SWB0', capacity=7)
G.add_edge('SWA1', 'PCD', capacity=14)
G.add_edge('SWA9', 'EL9')
G.add_edge('SWA5', 'EL5')
G.add_edge('EL5', 'LEL5')
G.add_edge('LEL5', 'DUMMY', capacity=32)
G.add_edge('EL9', 'LEL9')
G.add_edge('LEL9', 'DUMMY', capacity=32)
G.add_edge('RCPD', 'TRNF', capacity=28)
G.add_edge('RCPD', 'TRNS', capacity=7)
G.add_edge('PCD', 'TRNS', capacity=14)
G.add_edge('SWB0', 'TRNC', capacity=14)
G.add_edge('TRNF', 'EXIT')
G.add_edge('TRNS', 'EXIT')
G.add_edge('TRNC', 'EXIT')

#G.nodes.data()

# Add Stairwell edges
def add_swa_edge(floors):    
    for i in range(floors):
        if (i > 0):
            level = ''
            level += str(i + 1)
            name_a = 'SWA' + level
            name_b = 'SWA' + str(i)
            G.add_edge(name_a, name_b, capacity=7)
                
def add_swb_edge(floors):
    for i in range(floors):        
        if (i > 1):
            level = ''
            level += str(i + 1)
            name_a = 'SWB' + level
            name_b = 'SWB' + str(i)
            G.add_edge(name_a, name_b, capacity=7)

def add_hall_edge(floors, sw):
    for i in range(floors):
        if (sw == 'SWB'):
            if (i > 1 and i < 6):
                level = ''
                level += str(i + 1)
                name_a = 'H' + level
                name_b = sw + level
                G.add_edge(name_a, name_b, capacity=21)
            if (i > 5 and i < 10):
                level = ''
                level += str(i + 1)
                name_a = 'H' + level
                name_b = sw + level
                G.add_edge(name_a, name_b, capacity=7)
            G.add_edge('H10', 'SWB10', capacity=14)
            G.add_edge('H11', 'SWB11', capacity=7)
            G.add_edge('SWB9', 'H9', capacity=14)
        elif (sw == 'SWA'):
            if (i > 0):
                level = ''
                level += str(i + 1)
                name_a = 'H' + level
                name_b = sw + level
                G.add_edge(name_a, name_b, capacity=21)

swa_edge = add_swa_edge(floors)
swb_edge = add_swb_edge(floors)
h_swa_edge = add_hall_edge(floors, 'SWA')
h_sba_edge = add_hall_edge(floors, 'SWB')


nx.draw(G, with_labels=True)
plt.show()

