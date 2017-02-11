#!/usr/bin/python

from topsort import TopologicalSort

graph1 = {}
graph1['u'] = ['x', 'v']
graph1['v'] = ['y']
graph1['w'] = ['y', 'z']
graph1['x'] = ['v']
graph1['y'] = ['x']
graph1['z'] = ['z']

ts1 = TopologicalSort(graph1)
sorted_nodes1 = ts1.top_sort()
print sorted_nodes1

graph2 = {}
graph2['undershorts'] = ['pants', 'shoes']
graph2['socks'] = ['shoes']
graph2['watch'] = []
graph2['pants'] = ['shoes', 'belt']
graph2['belt'] = ['jacket']
graph2['shirt'] = ['belt', 'tie']
graph2['shoes'] = []
graph2['tie'] = ['jacket']
graph2['jacket'] = []

ts2 = TopologicalSort(graph2)
sorted_nodes2 = ts2.top_sort()
print sorted_nodes2
