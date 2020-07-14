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

    @staticmethod
    def loadData(filename: str):

        network = Network()

        with open(filename) as file_in:
            countNodes = 0
            countNodesAdded = 0
            countLinks = 0
            countLinksAdded = 0
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
                    countNodesAdded = countNodesAdded + 1
                else:
                    # Read link
                    lineParts = line.split()
                    fromNodeId = int(lineParts[0])
                    toNodeId = int(lineParts[1])
                    distance = int(lineParts[2])
                    network.addLink(fromNodeId, toNodeId, distance)
                    countLinksAdded = countLinksAdded + 1
                lineIndex = lineIndex + 1

        if (countNodes != countNodesAdded):
            print(f"Warning: expected {countNodes} nodes but found {countNodesAdded}")

        if (countLinks != countLinksAdded):
            print(f"Warning: expected {countLinks} links but found {countLinksAdded}")

        return network

    def printNodes(self):
        for nodeId in self.nodeIds:
            print('Node ID: ' + str(nodeId))