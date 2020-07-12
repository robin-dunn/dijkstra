# Language: Python v3
# Description: Script to read OSM network data and calculate walking routes
from typing import List, Dict
import math
from Network import Network
from PriorityQueue import PriorityQueue

def loadData(filename: str, network: Network):
    with open(filename) as file_in:
        countNodes = 0
        countLinks = 0
        lineIndex = 0

        for line in file_in:
            if (lineIndex == 0):
                # First line should be total number of nodes
                countNodes = int(line)
            elif (lineIndex == (countNodes + 1)):
                # This line should be total number of links
                countLinks = int(line)
            elif lineIndex <= countNodes:
                # Read node
                network.addNode(int(line))
            else:
                # Read link
                lineParts = line.split()
                fromNodeId = int(lineParts[0])
                toNodeId = int(lineParts[1])
                distance = int(lineParts[2])
                network.addLink(fromNodeId, toNodeId, distance)

            lineIndex = lineIndex + 1

def dijkstraSearch(network: Network, startNodeId: int, endNodeId: int):
    if startNodeId not in network.nodeIds:
        print('Node ID: ' + str(startNodeId) + ' not found')

    if endNodeId not in network.nodeIds:
        print('Node ID: ' + str(endNodeId) + ' not found')

    costs = {}
    backtrace = {}
    pq = PriorityQueue()

    # Set the costs of all nodes to infinity except the start node which we give zero cost.
    costs[startNodeId] = 0
    for nodeId in network.nodes:
        if (nodeId != startNodeId):
            costs[nodeId] = math.inf

    # Begin by adding start node to the queue
    pq.enqueue([startNodeId, 0])

    while (not pq.isEmpty()):
        shortestStep = pq.dequeue()
        currentNodeId = shortestStep[0]

        for neighbor in network.adjacencies[currentNodeId]:
            cost = costs[currentNodeId] + neighbor.cost

        if (cost < costs[neighbor.nodeId]):
            costs[neighbor.nodeId] = cost
            backtrace[neighbor.nodeId] = currentNodeId
            pq.enqueue([neighbor.nodeId, cost])

    path = [endNodeId]
    lastStep = endNodeId

    while(lastStep != startNodeId):
        path.insert(0, backtrace[lastStep])
        lastStep = backtrace[lastStep]
    
    return f'Path is {path} and time is {costs[endNodeId]}'

def run():
    network = Network()

    loadData('./graph.dat', network)

    print('cn ' + str(len(network.nodeIds)))

    dijkstraSearch(network, 314185938, 1320557460)

run()