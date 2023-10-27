# Topological Sorting

위상 정렬(Topological Sorting)은 방향 그래프에서 노드를 선형적으로 나열하는 알고리즘이다. 이를 통해 그래프 내 노드들 간의 선후관계를 나타낼 수 있다.

위상 정렬은 다음과 같은 특징이 있다.
- 방향 그래프에서만 적용 가능
- 사이클이 없는 그래프에서만 사용 가능
- 하나의 그래프에는 여러 위상 정렬 순서가 존재 가능

위상 정렬은 DFS와 BFS를 활용하여 구현한다.

# 줄 세우기
`Gold 3` `2252`
```python
from sys import stdin

input = stdin.readline

class Graph:
  def __init__(self, size):
    self.size = size
    self.graph = {}

  def add_edge(self, start, end):
    if start not in self.graph:
      self.graph[start] = []
    self.graph[start].append(end)

  def topology_sort(self):
    result = []
    indegree = [0 for _ in range(self.size+1)] # 그래프 내에서 특정 노드에 진입하는 방향의 연결 수
    stack = []

    # 진입 차수 계산
    for i in range(1, self.size+1):
      if i in self.graph:
        for nextNode in self.graph[i]:
          indegree[nextNode] += 1

    for i in range(1, self.size+1):
      if indegree[i] == 0:
        stack.append(i)

    while stack:
      nowNode = stack.pop()
      result.append(nowNode)

      if nowNode in self.graph:
        for nextNode in self.graph[nowNode]:
          indegree[nextNode] -= 1
          if indegree[nextNode] == 0:
            stack.append(nextNode)

    return result

if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())

  graph = Graph(N)

  for _ in range(M):
    start, end = map(int, input().rstrip().split())
    graph.add_edge(start, end)

  print(" ".join(map(str, graph.topology_sort())))
```

# 최종 순위
`Gold 1` `3665`
```python

```

# 문제집
`Gold 2` `1766`
```python

```
