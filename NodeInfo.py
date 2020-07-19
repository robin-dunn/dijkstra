# Language: Python v3
# Description: Class to hold node ID and cost to travel to the node.

class NodeInfo:
    nodeId: int
    cost: int

    def __init__(self, nodeId, cost):
        self.nodeId = nodeId
        self.cost = cost