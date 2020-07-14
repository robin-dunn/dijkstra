
# Language: Python v3
# Description: functions to calculate shotest path between nodes in a graph.
from typing import List, Dict
import math
from Network import Network
from PriorityQueue import PriorityQueue

class ShortestPath:
    @staticmethod
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
        for nodeId in network.nodeIds:
            if (nodeId != startNodeId):
                costs[nodeId] = math.inf

        # Begin by adding start node to the queue
        pq.enqueue(startNodeId, 0)

        # Use priority queue to traverse the nodes
        while (not pq.isEmpty()):
            shortestStep = pq.dequeue()
            currentNodeId = shortestStep.nodeId

            for neighbor in network.adjacencies[currentNodeId]:
                cost = costs[currentNodeId] + neighbor.cost

                if (cost < costs[neighbor.nodeId]):
                    costs[neighbor.nodeId] = cost
                    backtrace[neighbor.nodeId] = currentNodeId
                    pq.enqueue(neighbor.nodeId, cost)

        path = [endNodeId]
        lastStep = endNodeId

        while(lastStep != startNodeId):
            path.insert(0, backtrace[lastStep])
            lastStep = backtrace[lastStep]

        totalCost = costs[endNodeId]

        print(f'Path is {path} and time is {totalCost}')

        return totalCost