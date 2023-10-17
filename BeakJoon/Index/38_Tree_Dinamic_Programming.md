# Tree Dinamic Programming

Tree Dinamic Programming은 트리 관련 문제를 효과적으로 해결하기 위한 알고리즘 기법이다. 
Tree DP는 다음과 같은 방법으로 구현한다.
1. 트리 구조 활용 : 데이터를 트리로 표현
2. 재귀적 문제 분해 : 트리를 순회하면서 각 노드에서 하위 노드에 대한 문제를 분해
3. 메모이제이션 : 하위 문제의 해결책을 저장하여 중복 계산 회피

Tree DP의 종류는 다음과 같다.
- Max/Min Tree DP
  최대 or 최소값을 찾는 문제 해결 
- Counting Tree DP
  트리 내에서 측정 조건을 만족하는 요소의 수를 찾는 문제 해결
- Tree Coloring DP
  트리 노드를 색칠하는 문제 해결

# 트리와 쿼리
`Gold 5` `15681`
```python
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

class Tree:
  def __init__(self, root):
    self.root = root
    self.graph = {}
    self.subtree = {}

  def addEdge(self, u, v):
    if u not in self.graph:
      self.graph[u] = [v]
      self.subtree[u] = 0
    else:
      self.graph[u].append(v)

  def getSubTree(self, root):
    self.subtree[root] = 1
    for children in self.graph[root]:
      if self.subtree[children] == 0:
        self.subtree[root] += self.getSubTree(children)
    return self.subtree[root]

  def solution(self, treeCnt, printCnt):
    for _ in range(treeCnt):
      u, v = map(int, input().split())
      self.addEdge(u, v)
      self.addEdge(v, u)

    self.getSubTree(self.root)

    for _ in range(printCnt):
      root = int(input())
      print(self.subtree[root])

if __name__ == "__main__":
  N, R, Q = map(int, input().rstrip().split())
  tree = Tree(R)
  tree.solution(N-1, Q)
```

# 트리의 독립집합
`Gold 1` `2213`
```python

```

# 사회망 서비스 (SNS)
`Gold 3` `2533`
```python

```

# 우수 마을
`Gold 2` `1949`
```python

```
