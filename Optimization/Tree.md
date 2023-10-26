# Tree

트리(Tree)는 계층적 데이터를 효과적으로 다루기 위한 자료구조이다. 

트리는 다음과 같은 특징을 갖는다.
- 계층 구조 : 각 노드의 부모 자식 관계를 통해 계층 구조를 갖는다.
- 방향성 : 각 간선은 한 방향으로만 이동 가능한 방향성을 갖는다.
- 사이클 x : 어떤 경로로 이동해도 한 노드를 중복 방문하지 않는다.

트리의 종류는 다음과 같다.
- Binary Tree : 가장 기본적인 트리
- Binary Search Tree : 정렬된 데이터를 저장 and 탐색
- Trie : 문자열 검색 and 자동완성에 사용
- Balanced Tree : 균형을 유지하는 이진 탐색 트리
  - AVL Tree : 회전 연산을 통해 균형을 유지
  - Red-Black Tree : 레드, 블랙 노드 색을 통해 균형 유지
- Heap : 최대 or 최소값을 빠르게 찾기 위한 자료구조
- B-Tree : 대용량 데이터를 효율적으로 관리
- M-Way Tree : B-트리와 유사하며, 각 노드가 여러 자식을 가질 수 있음
- Threaded Binary Tree : 이진 트리에 링크를 추가하여 호율적인 순회

# Tree
```python
class Tree:
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
```

# Binary Tree
```python
class BinaryTree:
  def __init__(self, size):
    self.size = size
    self.tree = {}

  def makeTree(self):
    for _ in range(self.size):
      node, left, right = map(str, input().rstrip().split())
      self.tree[node] = [left, right]
```

# Binaru Search Tree
```python
class binarySearchTree:
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
```

# Trie
```python
class Node:
  def __init__(self, key, data=None):
    self.key = key
    self.data = data
    self.children = {}

class Trie:
  def __init__(self):
    self.root = Node('root')

  def insert(self, word):
    nowNode = self.root
    for char in word:
      if char not in nowNode.children:
        nowNode.children[char] = Node(char)
      nowNode = nowNode.children[char]
    nowNode.data = word

  def search(self, word):
    nowNode = self.root
    for char in word:
      if char in nowNode.children:
        nowNode = nowNode.children[char]
      else:
        return False

    if nowNode.data is not None:
      return nowNode.data

  def get_trie(self, depth, nowNode=None):
    if depth == 0:
      nowNode = self.root

    for char in sorted(nowNode.children.keys()):
      print('--'*depth, char, sep='')
      self.get_trie(depth+1, nowNode.children[char])
```
