from pprint import pprint

graph = {}

graph['start'] = {'A': 6, 'B': 2}
graph['A'] = {'finish': 1}
graph['B'] = {'A': 3, 'finish': 5}
graph['finish'] = {}

infinity = float('inf')
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['finish'] = infinity

parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['finish'] = None


def dijkstra(graph: dict, costs: dict, parents: dict):
  processed = []

  def find_lowest_cost_node(costs: list) -> str:
    lowest = float('inf')
    lowest_node = None
    for node in costs:
      if costs[node] < lowest and node not in processed:
        lowest = costs[node]
        lowest_node = node
    return lowest_node

  node = find_lowest_cost_node(costs)
  while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors.keys():
      new_cost = cost + neighbors[neighbor]
      if new_cost < costs[neighbor]:
        costs[neighbor] = new_cost
        parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


pprint(graph)
pprint(costs)
pprint(parents)
dijkstra(graph, costs, parents)
pprint(graph)
pprint(costs)
pprint(parents)
