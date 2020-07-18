
# Language: Python v3
# Description: Tests to check the dijkstra algorithm returns the expected shortest distance

from Network import Network
from ShortestPath import ShortestPath

network = Network.loadData('./graph_test.dat')

startNodeId = 1
endNodeId = 4
expectedDistance = 60

print (f"Expect shortest distance from node {startNodeId} to {endNodeId} is {expectedDistance}")

shortestDistance = ShortestPath.dijkstraSearch(network, startNodeId, endNodeId)

if shortestDistance == expectedDistance:
    print("PASS")
else:
    print("FAIL")