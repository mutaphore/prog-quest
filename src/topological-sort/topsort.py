
class TopologicalSort(object):

    def __init__(self, graph={}):
        self.graph = graph  # adjacency list repr of graph
        self.visited = {}
        self.parent = {}
        self.discover_time = {}
        self.finish_time = {}
        self.time = 0
    
    def top_sort(self):
        self.dfs()
        items = self.finish_time.items()
        top_sort = sorted(items, key=lambda t: t[1], reverse=True)
        return map(lambda t: t[0], top_sort)
    
    def dfs_helper(self, root):
        self.time += 1
        self.discover_time[root] = self.time
        for v in self.graph[root]:
            if not self.visited.get(v):
                self.visited[v] = True
                self.parent[v] = root
                self.dfs_helper(v)
        self.time += 1
        self.finish_time[root] = self.time
    
    def dfs(self):
        for k, v in self.graph.iteritems():
            if not self.visited.get(k):
                self.dfs_helper(k)
