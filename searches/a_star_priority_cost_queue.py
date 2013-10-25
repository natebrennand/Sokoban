
class AStarPriorityCostQueue(object):

    def __init__(self):
        self.queue = []
        self.roster = {}


    def push(self, h_cost, real_cost, item):
        total_coast = (h_cost + real_cost)
        if hash(item) in self.roster:
            print item
            print 'ERROR'
            raise Exception('Repeat item being added to priority queue')

        self.roster[hash(item)] = total_coast

        add_it = True
        for index, (h_cost, real_cost, node) in enumerate(self.queue):
            if total_coast <= h_cost:
                self.queue.insert(index, (total_coast, real_cost, item))
                add_it = False
                break
        if add_it:
            self.queue.append((total_coast, real_cost, item))


    def pop(self, index=0):
        h_cost, real_cost, item = self.queue.pop(index)
        del self.roster[hash(item)]

        assert len(self.queue) == len(self.roster.keys())

        return h_cost, real_cost, item


    def update_cost(self, h_cost, real_cost, item):
        total_cost = (h_cost + real_cost)
        if total_cost < self.roster[hash(item)]:
            for index, (element_total_cost, element_h_cost, element) in enumerate(self.queue):
                if hash(item) == hash(element):
                    self.queue[index] = (total_cost, real_cost, item)
                    self.roster[hash(item)] = total_cost


    def __contains__(self, item):
        return hash(item) in self.roster.keys()


    def __nonzero__(self):
        return len(self.queue) > 0 and len(self.roster.keys()) > 0


    def __len__(self):
        return len(self.queue)


    def __str__(self):
        return str(self.queue)
