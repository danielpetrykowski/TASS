# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:08:40 2020

@author: Daniel Petrykowski
"""

import networkx as nx 
import matplotlib.pyplot as plt 
import collections

G = nx.Graph() 
fh = open('patent_authors.txt', 'r', encoding='utf-8') 
for line in fh.readlines(): 
    line = line.strip() 
    
    patentInventors = []
    idStart = line.find("'inventor_name': '")
    while(idStart!=-1):
        idStart = idStart+18
        idEnd = line.find("'",idStart)
        name = line[idStart:idEnd]
        patentInventors.append(name)
        print(name)
        idStart = line.find("'inventor_name': '", idEnd)
        
    
    for i in patentInventors:
        for j in patentInventors:
            if i != j:
                G.add_edge(i,j)
            
            
print("Rząd sieci: {}".format(G.number_of_nodes())) 
print("Rozmiar sieci: {}".format(G.number_of_edges()))

maxDegree = 0 
for n, d in G.degree():
    if(d>maxDegree):
        maxDegree=d
        
print('Max degree %d' % maxDegree)
            
# Największa składowa spójna 
print("Największa składowa spójna") 
largest_cc = max(nx.connected_components(G), key=len) 
S = G.subgraph(largest_cc) 
print("Rząd największe składowej spójnej: {}".format(S.number_of_nodes())) 
print("Rozmiar największej skłądowej spójnej: {}".format(S.number_of_edges()))    

#Liczba rdzeni print("Licza rdzeni") 
numberCoreDict = nx.core_number(G) 
numberCore = [v for v in numberCoreDict.values()] 
maxCore = max(numberCore) 
print("Największy możliwy rząd rdzenia to {} w grafie wystepuje takich rdzeni {}" 
      .format(maxCore, numberCore.count(maxCore))) 
print("Drugi największy możliwy rząd rdzenia to {} w grafie wystepuje takich rdzeni {}" 
      .format(maxCore-1, numberCore.count(maxCore-1))) 
print("Trzeci największy możliwy rząd rdzenia to {} w grafie wystepuje takich rdzeni {}" 
      .format(maxCore-2, numberCore.count(maxCore-2)))
average_neighbor_degree = nx.average_neighbor_degree(G)
print("Współczynnik gronowania {}".format(average_clustering))
transitivity = nx.transitivity(G)
print("Przechodniosc {}".format(transitivity))
average_shortest_path_length = nx.average_shortest_path_length(S)
print("average_shortest_path_length {}".format(average_shortest_path_length))
density = nx.density(G)
print("density {}".format(density))


#Rozkład stopni wirzchołka 
degree = sorted([d for n, d in G.degree()], reverse=True) 
counter=collections.Counter(degree)



plt.hist(degree, 100) 
plt.title("Degree Histogram") 
plt.ylabel("Count") 
plt.xlabel("Degree") 
plt.show()


#options = {
#    'node_color': 'black',
#    'node_size': 50,
#    'line_color': 'grey',
#    'linewidths': 0,
#    'width': 0.1,
#}
#nx.draw(G, **options)
#plt.show()

