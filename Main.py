# Language: Python v3
# Description: Script to read OSM network data and calculate walking routes
from Network import Network
from ShortestPath import ShortestPath

network = Network.loadData('./graph.dat')
ShortestPath.dijkstraSearch(network, 314185938, 1320557460)
