from NodeInfo import NodeInfo

class PriorityQueue:
    collection = []
    
    def enqueue(self, nodeId, cost):
        node = NodeInfo(nodeId, cost)

        if (self.isEmpty()): 
            self.collection.append(node)
        else:
            added = False
            i = 1
            while (i <= len(self.collection)):
                if (node.cost < self.collection[i - 1].cost):
                    self.collection.insert(i - 1, node)
                    added = True
                    break
                i = i + 1

            if (added == False):
                self.collection.append(node)

    def dequeue(self):
        return self.collection.pop(0)

    def isEmpty(self):
        return len(self.collection) == 0
