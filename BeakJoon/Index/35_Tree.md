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
from sys import stdin

input = stdin.readline

class BinaryTree():
  def __init__(self, size):
    self.size = size
    self.tree = {}

  def makeTree(self):
    for _ in range(self.size):
      node, left, right = map(str, input().rstrip().split())
      self.tree[node] = [left, right]
    
  def preorder(self, root): # 전위 순회 : root -> left -> right
    if root != '.':
      print(root, end='')
      self.preorder(self.tree[root][0])
      self.preorder(self.tree[root][1])
      
  def inorder(self, root): # 중위 순회 : left -> root -> right
    if root != '.':
      self.inorder(self.tree[root][0])
      print(root, end='')
      self.inorder(self.tree[root][1])
  
  def postorder(self, root): # 후위 순회 : left -> right -> root
    if root != '.':
      self.postorder(self.tree[root][0])
      self.postorder(self.tree[root][1])
      print(root, end='')

  def solution(self):
    self.preorder('A')
    print()
    self.inorder('A')
    print()
    self.postorder('A')

if __name__ == "__main__":
  N = int(input())
  binarytree = BinaryTree(N)
  binarytree.makeTree()
  binarytree.solution()
```

# 트리의 순회
`Gold 1` `2263`
```Python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# pre, in, post order 의 순회 정리
# pre order : 부모, 왼쪽 자식, 오른쪽 자식
# in order : 왼쪽 자식, 부모, 오른쪽 자식
# post order : 왼쪽 자식, 오른쪽 자식, 부모

# 특정 노드를 루트 노드로 가지는 부분 트리가 존재한다면
# pre, in, post order 배열은 각 order 안의 부분 트리의 위치만 다를 뿐, 해당 부분 트리의 노드들이 붙어있는 구조를 가지고 있다
# 즉 각 order 배열을 인덱싱하여 부분 트리를 뽑아낼 수 있다

# 인덱싱 된 post order 배열의 마지막 노드는 해당 부분 트리의 루트 노드이다
# 인덱싱 된 in order 의 루트 노드는 자식 노드의 부분 트리 사이에 위치한다
# post order 에서 가져온 루트 노드를 in order 에서 찾으면 왼쪽 부분 트리 / 루트 노드 / 오른쪽 부분 트리 의 관계를 찾을 수 있다

def slicing(start, end, in_w, pre_w):
  # 예외처리
  if start > end or start < 0 or end < 0:
    return

  # post order 의 마지막 노드는 루트 노드
  root = post_order[end]
  # 해당 루트 노드를 pre order 배열에 넣는다
  # pre_w: post order 기준 pre order 에서 부분 트리가 밀린 횟수
  pre_order[start+pre_w] = str(root)

  # 부분 트리가 노드 1개밖에 없다면 종료
  if start == end:
    return

  # pre order 와 in order 의 끝 노드가 같다면, 해당 부분 트리는 오른쪽 자식이 없다
  if root == in_order[end + in_w]:
    # 왼쪽 자식을 재귀 호출할 시 in order 부분 트리는 밀리지 않지만 pre order 부분 트리는 한 칸 밀리므로 pre_w 에 +1
    slicing(start, end - 1, in_w, pre_w + 1)
    return

  # pre order 의 끝 노드가 in order 의 시작 노드와 같다면, 해당 부분 트리는 왼쪽 자식이 없다
  if root == in_order[start + in_w]:
    # 오른쪽 자식을 재귀 호출할 시 in oder, pre order 부분 트리 모두 한 칸씩 밀리므로 in_w, pre_w 에 각각 +1
    slicing(start, end - 1, in_w + 1, pre_w + 1)
    return

  # in order 를 이용하여 트리 구조를 찾음
  root_idx = -1
  for idx in range(end-1, start, -1):
    if in_order[idx + in_w] == root: # 루트 노드를 찾으면 해당 인덱스를 받고 탈출
      root_idx = idx
      break

  # 왼쪽 자식 부분 트리, 오른쪽 자식 부분 트리에 대해 재귀 호출
  slicing(start, root_idx - 1, in_w, pre_w + 1)
  slicing(root_idx, end - 1, in_w + 1, pre_w + 1)

if __name__ == "__main__":
  n = int(input())

  in_order = list(map(int, input().split()))
  post_order = list(map(int, input().split()))
  pre_order = ["" for _ in range(n)]

  slicing(0, n - 1, 0, 0)     # pre_order 구성
  print(" ".join(pre_order))
```

# 이진 검색 트리
`Gold 5` `5639`
```Python
from sys import stdin

input = stdin.readline

class binarySearchTree():
  def __init__(self, root):
    self.root = root
    self.tree = {}

  def makeTree(self):
    self.tree[self.root] = [-1, -1]
    while True:
      node = str(input().rstrip())
      if node == '':
        break

      node = int(node)
      comparison = self.root
      while True:
        if comparison < node:
          if self.tree[comparison][1] == -1:
            self.tree[comparison][1] = node
            self.tree[node] = [-1, -1]
            break
          comparison = self.tree[comparison][1]

        if node < comparison:
          if self.tree[comparison][0] == -1:
            self.tree[comparison][0] = node
            self.tree[node] = [-1, -1]
            break
          comparison = self.tree[comparison][0]

  def postorder(self, root):
    if root != -1:
      self.postorder(self.tree[root][0])
      self.postorder(self.tree[root][1])
      print(root)

  def solution(self):
    self.postorder(self.root)

if __name__ == "__main__":
  root = int(input().rstrip())
  tree = binarySearchTree(root)
  tree.makeTree()
  tree.solution()
```

# 트리
`Gold 4` `4803`
```Python
from sys import stdin

input = stdin.readline

class Graph():
  def __init__(self, nodes, edges):
    self.nodes = nodes
    self.edges = edges
    self.graph = {}
    for i in range(1, nodes+1):
      self.graph[i] = i

  def makeGraph(self):
    for i in range(1, self.nodes+1):
      self.graph[i] = i
      
    for _ in range(self.edges):
      u, v = map(int, input().rstrip().split())
      if self.graph[u] == u:
        self.graph[u] = v
      else:
        self.graph[v] = u
        
  def findTree(self):
    count = 0
    node = 1
    while True:
      if node == self.nodes:
        if self.graph[node] == node:
          count += 1
          break
        else:
          break
      
      if self.graph[node] == node:
        count += 1
        node +=1
      else:
        node +=1

    return count
  
  def solution(self):
    self.makeGraph()
    result = self.findTree()
    if result == 0:
      print('No trees.')
    elif result == 1:
      print('There is one tree.')
    elif result > 1:
      print(f'A forest of {result} trees.')

if __name__ == "__main__":
  while True:
    N, M = map(int, input().rstrip().split())
    if N != 0 and M != 0:
      graph = Graph(N, M)
      graph.solution()
```
