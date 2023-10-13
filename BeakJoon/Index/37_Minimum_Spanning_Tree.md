# Minimum Spanning Tree (MST)

최소 신장 트리(Minimum Spanning Tree)는 그래프 내에 존재하는 부분 그래프이다. 해당 그래프는 그래프 내 부분 그래프 중에서 가장 작은 가중치 합을 갖는다.

MST는 다음과 같은 특징을 갖는다.
- 사이클 x
- 여러 MST가 존재 가능

MST의 종류는 다음과 같다.
- Kruskal 알고리즘 : 가중치를 기준으로 작은 것부터 순서대로 선택하며 MST 구성
  - 무방향 그래프에서 유리
  - 간선이 많은 그래프에서 유리
  - 자료구조 : 유니온 파인드
- Prim 알고리즘 : 시작 노드를 선택하여 인접한 최소 가중치 간선을 선택하며 MST 구성
  - 밀집 그래프에서 유리
  - 간선이 적은 그래프에서 유리
  - 자료구조 : 우선순위 큐

MST 알고리즘들을 구현하는 방법은 다음과 같다.
- Kruskal 알고리즘
  1. 모든 간선을 가중치를 기준으로 정렬
  2. 빈 MST 초기화
  3. 정렬된 간선 리스트를 순회하며, 사이클을 형성하지 않는 간선을 MST에 추가
  4. 모든 노드가 MST에 포함될 때까지 반복
- Prim 알고리즘
  1. 임의의 시작 노드 선택 후 해당 노드를 MST에 추가
  2. MST에 연결된 간선 중에서 가장 작은 가중치의 간선 선택
  3. 선택한 간선으로 연결된 노드를 MST에 추가 후 해당 노드와 연결된 간선을 후보 간선 목록에서 제거
  4. 모든 노드가 MST에 포함될 때까지 반복

# 상근이의 여행
`Silver 4` `9372`
```python
from sys import stdin
from collections import deque

input = stdin.readline

class Graph:
  def __init__(self, size):
    self.size = size
    self.graph = {}
    self.visited = {}

  def makeGraph(self, u, v):
    if u not in self.graph:
      self.graph[u] = [v]
      self.visited[u] = 0
    else:
      if v not in self.graph[u]:
        self.graph[u].append(v)

    if v not in self.graph:
      self.graph[v] = [u]
      self.visited[v] = 0
    else:
      if u not in self.graph[v]:
        self.graph[v].append(u)

  def BFS(self, start):
    path = [] 
    queue = deque([start])
    
    self.visited[start] = 1
    path.append(start)
    count = 0
  
    while queue:
      node = queue.popleft()
  
      for nextNode in self.graph[node]:
        if self.visited[nextNode] == 0:
          queue.append(nextNode)
          path.append(nextNode)
          self.visited[nextNode] = 1
          count += 1
  
    return count
  
  def solution(self, cnt):
    for _ in range(cnt):
      u, v = map(int, input().rstrip().split())
      self.makeGraph(u, v)

    result = self.BFS(1)
    print(result)
      
if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    N, M = map(int, input().rstrip().split())
    uf = Graph(N)
    uf.solution(M)
```

# 최소 스패닝 트리
`Gold 4` `1197`
```python
from sys import stdin

input = stdin.readline

class kruckalMST:
  def __init__(self, size):
    self.size = size
    self.mst = []
    self.graph = []
    self.parent = {}

  def find(self, x):
    if self.parent[x] < 0:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    if self.parent[x] > self.parent[y]:
      self.parent[x] = y
    else:
      if self.parent[x] == self.parent[y]:
        self.parent[x] -= 1
      self.parent[y] = x

  def kruckal(self):
    graph = sorted(self.graph, key=lambda x: x[2])

    for u, v, weight in graph:
      rootU, rootV = self.find(u), self.find(v)
      if rootU != rootV:
        self.mst.append((u, v, weight))
        self.union(rootU, rootV)
  
  def solution(self, cnt):
    for _ in range(cnt):
      u, v, weight = list(map(int, input().rstrip().split()))
      self.graph.append([u, v, weight])
      self.parent[u] = -1
      self.parent[v] = -1

    self.kruckal()

    result = 0
    for _, _, weight in self.mst:
      result += weight
    print(result)
      
if __name__ == "__main__":
  V, E = map(int, input().rstrip().split())
  mst = kruckalMST(V)
  mst.solution(E)
```

# 별자리 만들기
`Gold 3` `4386`
```python
from sys import stdin
from math import sqrt

input = stdin.readline

class kruskalMST:
  def __init__(self):
    self.mst = []
    self.graph = []
    self.parent = {}
    self.coordinate = {}

  def find(self, x):
    if self.parent[x] < 0:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    if self.parent[x] > self.parent[y]:
      self.parent[x] = y
    else:
      if self.parent[x] == self.parent[y]:
        self.parent[x] -= 1
      self.parent[y] = x

  def kruskal(self):
    graph = sorted(self.graph, key=lambda x: x[2])

    for u, v, weight in graph:
      rootU, rootV = self.find(u), self.find(v)
      if rootU != rootV:
        self.mst.append((u, v, weight))
        self.union(rootU, rootV)

  def makeGraph(self):
    for u in range(len(self.coordinate)):
      for v in range(len(self.coordinate)):
        if u == v:
          continue
        x1, y1 = self.coordinate[u]
        x2, y2 = self.coordinate[v]
        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

        self.graph.append((u, v, distance))
        if u not in self.parent:
          self.parent[u] = -1
        if v not in self.parent:
          self.parent[v] = -1

  def solution(self, cnt):
    for i in range(cnt):
      x, y = map(float, input().rstrip().split())
      self.coordinate[i] = (x, y)
      
    self.makeGraph()
    self.kruskal()

    result = 0
    for _, _, weight in self.mst:
      result += weight
    print(round(result, 2))

if __name__ == "__main__":
  N = int(input())
  mst = kruskalMST()
  mst.solution(N)
```

# 우주신과의 교감
`Gold 3` `1774`
```python
from sys import stdin
from math import sqrt

input = stdin.readline

class kruskalMst:
  def __init__(self):
    self.mst = []
    self.graph = []
    self.coordinate = {}
    self.parent = {}

  def find(self, x):
    if self.parent[x] < 0:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    if self.parent[x] > self.parent[y]:
      self.parent[x] = y
    else:
      if self.parent[x] == self.parent[y]:
        self.parent[x] -= 1
      self.parent[y] = x

  def kruskal(self):
    graph = sorted(self.graph, key=lambda x: x[2])

    for u, v, weight in graph:
      rootU, rootV = self.find(u), self.find(v)
      if rootU != rootV:
        self.mst.append((u, v, weight))
        self.union(rootU, rootV)

  def makeGraph(self):
    for u in range(len(self.coordinate)):
      for v in range(len(self.coordinate)):           
        if u == v:
          continue
        x1, y1 = self.coordinate[u]
        x2, y2 = self.coordinate[v]
        distance = round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

        self.graph.append((u, v, distance))

        if u not in self.parent:
          self.parent[u] = -1
        if v not in self.parent:
          self.parent[v] = -1

  def solution(self, nodeCnt, linkedCnt):
    for i in range(nodeCnt):
      x, y = map(float, input().rstrip().split())
      self.coordinate[i] = (x, y)

    self.makeGraph()

    for _ in range(linkedCnt):
      u, v = map(int, input().rstrip().split())
      for a, b, w in self.graph:
        if a == u-1 and b == v-1:
          self.graph.remove((a, b, w))
          rootU, rootV = self.find(u-1), self.find(v-1)
          self.union(rootU, rootV)

    self.kruskal()

    result = 0
    for u, v, weight in self.mst:
      result += weight
    print(result)

if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())
  mst = kruskalMst()
  mst.solution(N, M)
```

# 전력난
`Gold 4` `6497`
```python

```

# 다리 만들기 2
`Gold 1` `17472`
```python

```
