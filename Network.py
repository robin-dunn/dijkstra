# Language: Python v3
# Description: class to hold the nodes and links of a routing network

from typing import List, Dict
from NodeInfo import NodeInfo

class Network:
    nodeIds: List = []
    adjacencies: Dict = {}

    def addNode(self, nodeId: int):
        self.nodeIds.append(nodeId)
        self.adjacencies[nodeId] = []

    def addLink(self, fromNodeId: int, toNodeId: int, distance: int):
        if (self.adjacencies.get(fromNodeId) is None):
            print('Node with ID ' + fromNodeId + ' not found')
            return

        if (self.adjacencies.get(toNodeId) is None):
            print('Node with ID ' + toNodeId + ' not found')
            return

        self.adjacencies[fromNodeId].append(NodeInfo(toNodeId, distance))
        self.adjacencies[toNodeId].append(NodeInfo(fromNodeId, distance))

    def printNodes(self):
        for nodeId in self.nodeIds:
            print('Node ID: ' + str(nodeId))