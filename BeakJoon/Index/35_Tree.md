# Tree

트리(Tree)는 계층적 데이터를 효과적으로 다루기 위한 자료구조이다. 

트리는 다음과 같은 특징을 갖는다.
- 계층 구조 : 각 노드의 부모 자식 관계를 통해 계층 구조를 갖는다.
- 방향성 : 각 간선은 한 방향으로만 이동 가능한 방향성을 갖는다.
- 사이클 x : 어떤 경로로 이동해도 한 노드를 중복 방문하지 않는다.

트리의 종류는 다음과 같다.
- Binary Tree : 가장 기본적인 트리
- Binary Search Tree : 정렬된 데이터를 저장 and 탐색
- Balanced Tree : 균형을 유지하는 이진 탐색 트리
  - AVL Tree : 회전 연산을 통해 균형을 유지
  - Red-Black Tree : 레드, 블랙 노드 색을 통해 균형 유지
- Heap : 최대 or 최소값을 빠르게 찾기 위한 자료구조
- Trie : 문자열 검색 and 자동완성에 사용
- B-Tree : 대용량 데이터를 효율적으로 관리
- M-Way Tree : B-트리와 유사하며, 각 노드가 여러 자식을 가질 수 있음
- Threaded Binary Tree : 이진 트리에 링크를 추가하여 호율적인 순회

# 트리의 부모 찾기
`Silver 2` `11725`
```Python
# 트리의 부모를 찾는 방법의 경우 DFS가 적합하다.
from sys import stdin

input = stdin.readline

class Tree():
  def __init__(self, size):
    self.size = size
    self.tree = [[] for _ in range(size+1)]
    self.visited = [0 for _ in range(size+1)]
    self.parents = [0 for _ in range(size+1)]

  def makeTree(self):
    for _ in range(self.size-1):
      u, v = map(int, input().rstrip().split())
      self.tree[u].append(v)
      self.tree[v].append(u)
    
  def DFS(self, start):
    stack = [start]

    while stack:
      nowNode = stack.pop()

      if self.visited[nowNode] == 1:
        continue

      self.visited[nowNode] = 1
      for nextNode in self.tree[nowNode]:
        if self.visited[nextNode] == 0:
          stack.append(nextNode)
          self.parents[nextNode] = nowNode

  def solution(self):
    self.DFS(1)
    print('\n'.join(map(str, self.parents[2:])))

if __name__ == "__main__":
  N = int(input())
  tree = Tree(N)
  tree.makeTree()
  tree.solution()
```

# 트리의 지름
`Gold 2` `1167`
```Python
# 트리의 지름을 구하는 경우 DFS가 적합하다.
from sys import stdin

input = stdin.readline

class Tree():
  def __init__(self, size):
    self.size = size
    self.tree = [[] for _ in range(size+1)]
    self.visited = [0 for _ in range(size+1)]
    self.distance = [0 for _ in range(size+1)]

  def makeTree(self):
    for _ in range(self.size):
      u, *data = map(int, input().rstrip().split()[:-1])
      for i in range(0, len(data), 2):
        v, w = data[i], data[i+1]
        self.tree[u].append((v,w))

  def DFS(self, start):
    stack = [start]
    while stack:
      nowNode = stack.pop()

      if self.visited[nowNode] == 1:
        continue

      self.visited[nowNode] = 1
      for nextNode, nextWeight in self.tree[nowNode]:
        if self.visited[nextNode] == 0:
          stack.append(nextNode)
          self.distance[nextNode] = self.distance[nowNode] + nextWeight

  def findMax(self):
    maxValue, index = 0, 0
    for idx, value in enumerate(self.distance):
      if maxValue < value:
        maxValue = value
        index = idx

    return maxValue, index

  def solution(self):
    self.DFS(1)
    _ , node = self.findMax()

    self.visited = [0 for _ in range(self.size+1)]
    self.distance = [0 for _ in range(self.size+1)]
    self.DFS(node)
    value, _ = self.findMax()

    print(value)
  
if __name__ == "__main__":
  N = int(input())
  tree = Tree(N)
  tree.makeTree()
  tree.solution()
```

# 트리의 지름
`Gold 4` `1967`
```Python
from sys import stdin

input = stdin.readline

class Tree():
  def __init__(self, size):
    self.size = size
    self.tree = [[] for _ in range(size+1)]
    self.visited = [0 for _ in range(size+1)]
    self.distance = [0 for _ in range(size+1)]

  def makeTree(self):
    for _ in range(self.size-1):
      u, v, w = map(int, input().rstrip().split())
      self.tree[u].append((v, w))
      self.tree[v].append((u, w))

  def DFS(self, start):
    stack = [start]
    while stack:
      nowNode = stack.pop()

      if self.visited[nowNode] == 1:
        continue

      self.visited[nowNode] = 1
      for nextNode, nextWeight in self.tree[nowNode]:
        if self.visited[nextNode] == 0:
          stack.append(nextNode)
          self.distance[nextNode] = self.distance[nowNode] + nextWeight

  def findMax(self):
    maxValue, index = 0, 0
    for idx, value in enumerate(self.distance):
      if maxValue < value:
        maxValue = value
        index = idx

    return maxValue, index

  def solution(self):
    self.DFS(1)
    _ , node = self.findMax()

    self.visited = [0 for _ in range(self.size+1)]
    self.distance = [0 for _ in range(self.size+1)]
    self.DFS(node)
    value, _ = self.findMax()

    print(value)
  
if __name__ == "__main__":
  N = int(input())
  tree = Tree(N)
  tree.makeTree()
  tree.solution()
```

# 트리 순회
`Silver 1` `1991`
```Python

```

# 트리의 순회
`Gold 1` `2263`
```Python

```

# 이진 검색 트리
`Gold 5` `5639`
```Python

```

# 트리
`Gold 4` `4803`
```Python

```
