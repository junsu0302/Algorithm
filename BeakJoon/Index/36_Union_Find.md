# Union Find

유니온 파인드(Union Find)는 데이터 집합을 효율적으로 관리하기 위한 자료 구조로 Disjoint Set Union(DSU) 또는 상호 배타적 집합이라고도 부른다. 각 집합들은 상호 배타적이며 서로 겹치지 않는다.

유니온 파인드의 주요 연산은 다음과 같다.
1. MakeSet(x) : 요소 x를 자신만으로 이루어진 집합으로 만든다.
2. Find(x) : 요소 x가 속한 집합의 대표를 반환
3. Union(x, y) : 요소 x와 y를 포함하는 두 집합을 하나로 합친다.

유니온 파인드의 주요 연산은 다음과 같다.
1. 빠른 Find 연산으로 요소가 속한 집합을 빠르게 찾음
2. 경로 압축(Path Compression) 및 순위(Rank)를 활용하여 연산의 효율성 최적화

유니온 파인드의 종류는 다음과 같다.
1. Quick Find
  - 각 집합을 배열로 표현
  - Find : 배열에서 집합의 대표를 찾음
  - Union : 두 배열을 합칠 때 모든 요소 업데이트
2. Quick Union
  - 각 집합을 트리로 표현
    - 경로 압축 및 순위를 통해 트리 높이 최소화
  - Find : 트리를 탐색하여 집합의 대표를 찾음
  - Union : 한 트리의 루트를 다른 트리의 루트로 설정하여 두 트리 결합

유니온 파인드의 구현 방법은 다음과 같다.
1. 요소 초기화 : 각 요소를 집합(배열 or 트리)로 초기화
2. Find 연산 : 주어진 요소의 집합 대표(루트)를 찾음
3. Union 연산 : 두 집합을 합침 (경로 압축 or 순위를 통한 효율성 증가)

# 집합의 표현
`Gold 5` `1717`
```python
# 정석 풀이
from sys import stdin

input = stdin.readline

class UnionFind:
  def __init__(self, size):
    self.parent = list(range(size+1)) # 부모 노드 초기화
    self.rank = [1 for _ in range(size+1)] # 트리의 높이 초기화

  def find(self, x): # x가 속한 집합의 대표(루트) 탐색
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x]) # 경로 압축
    return self.parent[x]

  def union(self, x, y): # 두 집합을 합칩니다.
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x != root_y:
      # 두 집합의 랭크를 비교하여 더 낮은 랭크의 트리를 더 높은 랭크의 트리에 연결합니다.
      if self.rank[root_x] < self.rank[root_y]:
        self.parent[root_x] = root_y
      elif self.rank[root_x] > self.rank[root_y]:
        self.parent[root_y] = root_x
      else:
        self.parent[root_y] = root_x
        self.rank[root_x] += 1

  def solution(self, cnt):
    for _ in range(cnt):
      command, elementA, elementB = map(int, input().rstrip().split())

      if command == 0:
        self.union(elementA, elementB)
      if command == 1:
        if self.find(elementA) == self.find(elementB):
          print('YES')
        else:
          print('NO')

if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())
  uf = UnionFind(N)
  uf.solution(M)
```

```python
# 변형 풀이
from sys import stdin

input = stdin.readline

class UnionFind:
  def __init__(self, size):
    self.parent = [-1 for _ in range(size+1)] # 부모 노드 초기화 (Rank 역할도 수행)
    """
    parent = -1 : 다른 노드와 연결되지 않은 상태
    parent = x (x>0) : x번째 노드와 연결
    parent = x (x<-1) : x만큼 트리의 깊이가 깊음
    """

  def find(self, x): # x가 속한 집합의 대표(루트) 탐색
    if self.parent[x] < 0: # 해당 노드가 root 노드임을 의미
      return x
    self.parent[x] = self.find(self.parent[x]) # 경로 압축
    return self.parent[x]

  def union(self, x, y): # 두 집합 결합
    if self.parent[x] > self.parent[y]: # x의 root depth가 y의 root depth보다 큰 경우
      self.parent[x] = y
    else:
      if self.parent[x] == self.parent[y]: # root depth가 같은 경우
        self.parent[x] -= 1 # root depth를 x의 depth를 낮춰 x<y로 맞춰줌
      self.parent[y] = x

  def solution(self, cnt):
    result = []
    for _ in range(cnt):
      command, elementA, elementB = map(int, input().rstrip().split())
      rootA = self.find(elementA)
      rootB = self.find(elementB)

      if command == 0:
        if rootA != rootB:
          self.union(rootA, rootB)
      if command == 1:
        if rootA == rootB:
          result.append('YES')
        else:
          result.append('NO')

    print('\n'.join(map(str, result)))

if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())
  uf = UnionFind(N)
  uf.solution(M)
```

# 여행 가자
`Gold 4` `1976`
```python

```

# 친구 네트워크
`Gold 2` `4195`
```python

```

# 사이클 게임
`Gold 4` `20040`
```python

```
