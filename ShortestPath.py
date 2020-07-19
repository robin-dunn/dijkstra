# Language: Python v3
# Description: Calculate shortest path between nodes in a graph.

import math
from Network import Network
from PriorityQueue import PriorityQueue

class ShortestPath:

    @staticmethod
    def dijkstraSearch(network: Network, startNodeId: int, endNodeId: int):
        if (not network.nodesExist([startNodeId, endNodeId])):
            return -1
            
        costs = {}
        pq = PriorityQueue()

        # Set the costs of all nodes to infinity except the start node which we give zero cost.
        costs[startNodeId] = 0
        for nodeId in network.nodeIds:
            if (nodeId != startNodeId):
                costs[nodeId] = math.inf

        # Begin by adding start node to the queue.
        pq.enqueue(startNodeId, 0)

        # Use priority queue to traverse the nodes having least cost.
        while (not pq.isEmpty()):
            shortestStep = pq.dequeue()
            currentNodeId = shortestStep.nodeId

            # Calculate the cost of travelling to each neighbor.
            for neighbor in network.adjacencies[currentNodeId]:
                cost = costs[currentNodeId] + neighbor.cost

                # If the cost of this path to the neighbor is less than another path
                # we add the neighbor node ID to the queue as a candidate to be traversed.  
                if (cost < costs[neighbor.nodeId]):
                    costs[neighbor.nodeId] = cost
                    pq.enqueue(neighbor.nodeId, cost)

        return costs[endNodeId]