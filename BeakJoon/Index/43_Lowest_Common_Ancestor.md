# Lowest Common Ancestor (LCA)

최소 공통 조상(Lowest Common Ancestor, LCA) 알고리즘은 트리에서 두 노드의 가장 가까운 공통 조상을 찾는 알고리즘이다. 

LCA의 종류는 다음과 같다.
- 최소 공통 조상 찾기
  트리를 한 번 순회하면서 각 노드의 조상을 기록하는 방법
- 바이너리 리프팅
  DP를 사용하여 트리의 사전처리를 통해 조상을 기록

# 가장 가까운 공통 조상
`Gold ` ``
```python
from sys import stdin

input = stdin.readline

class Node:
  def __init__(self, key):
    self.key = key
    #self.depth = None
    self.parent = None
    #self.children = []

class Tree:
  def __init__(self):
    self.root = None
    self.tree = {}

  def add_node(self):
    parent, child = map(int, input().rstrip().split())
    if parent not in self.tree:
      self.tree[parent] = Node(parent)
    if child not in self.tree:
      self.tree[child] = Node(child)
    #self.tree[parent].children.append(child)
    self.tree[child].parent = parent

  def find_parent_list(self, target):
    result = [target]
    nowNode = self.tree[target]
    while True:
      if nowNode.parent is None:
        break
      result.append(nowNode.parent)
      nowNode = self.tree[nowNode.parent]

    return result
  
  def LCA(self):
    target1, target2 = map(int, input().rstrip().split())
    parentList1 = self.find_parent_list(target1)
    parentList2 = self.find_parent_list(target2)

    for target1 in parentList1:
      for target2 in parentList2:
        if target1 == target2:
          return target1

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    tree = Tree()
    N = int(input())
    for _ in range(N-1):
      tree.add_node()
    result = tree.LCA()
    print(result)
```

# 합성합수와 쿼리
`Gold ` ``
```python

```

# LCA 2
`Platinum ` ``
```python

```

# 도로 네트워크
`Platinum ` ``
```python

```

# 트리와 쿼
`Platinum ` ``
```python

```
