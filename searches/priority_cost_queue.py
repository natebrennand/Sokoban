
class PriorityCostQueue(object):

    def __init__(self):
        self.queue = []
        self.roster = {}


    def push(self, cost, item):
        self.roster[hash(item)] = cost

        if len(self.queue) == 0:
            self.queue = [(cost, item)]
            return

        dont_add = False
        for index, (node_cost, node) in enumerate(self.queue):
            if cost <= node_cost:
                self.queue.insert(index, (cost, item))
                dont_add = True
                break
        if not dont_add:
            self.queue.append((cost, item))


    def pop(self, index=0):
        cost, item = self.queue.pop(index)
        del self.roster[hash(item)]
        return cost, item


    def update_cost(self, cost, item):
        if cost < self.roster[hash(item)]:
            for index, (element_cost, element) in enumerate(self.queue):
                if hash(item) == hash(element):
                    self.queue[index][0] = cost
                    self.roster[hash(item)] = cost


    def __contains__(self, item):
        return hash(item) in self.roster.keys()


    def __nonzero__(self):
        return len(self.queue) > 0 and len(self.roster.keys()) > 0


    def __len__(self):
        return len(self.queue)


    def __str__(self):
        return str(self.queue)
