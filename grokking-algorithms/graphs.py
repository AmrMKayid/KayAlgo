from collections import deque
from pprint import pprint

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(*, name: str) -> bool:
  return name[-1] == 'm'


def bfs(*, graph: dict, name: str = 'you') -> bool:

  search_queue = deque()
  search_queue += graph[name]
  searched = []

  while search_queue:
    print(search_queue)
    person = search_queue.popleft()
    if person not in searched:
      if person_is_seller(name=person):
        print(f"{person} is a mango seller!")
        return True

      search_queue += graph[person]
      searched.append(person)

  return False


pprint(graph)
bfs(graph=graph)
