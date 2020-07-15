# Language: Python v3
# Description: Script to read OSM network data and calculate walking routes
import sys
from Network import Network
from ShortestPath import ShortestPath

network = Network.loadData('./graph.dat')
ShortestPath.dijkstraSearch(network, int(sys.argv[1]), int(sys.argv[2]))
