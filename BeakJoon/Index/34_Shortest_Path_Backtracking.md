# 최단 거리 역추적 (Shortest Path Backtracking)

최단 거리 역추적 (Shortest Path Backtracking) 알고리즘은 최단 경로를 찾는 과정에서 경로를 역추적하여 최단 경로를 찾아내는 알고리즘이다. 이를 위해 최단 경로를 찾는 과정에서 각 노드에 도달하기 위한 이전 노드를 기록한다. 최단 경로를 찾기 위해 최단 경로 알고리즘과 동적 계획법의 점화식을 활용한다.

최단 거리 역추적 알고리즘의 특징은 다음과 같다.
1. 최단 경로를 찾는 과정에서 경로를 역추적하여 실제 최단 경로 탐색
2. 점화식을 통해 각 노드로 가는 최단 거리 계산

최단 거리 역추적 알고리즘의 구현 방법은 다음과 같다.
1. 최단 거리 정보를 저장하기 위핸 DP 배열 초기화
2. 최단 경로 알고리즘을 통해 DP 배열 업데이트
3. 목표 노드로부터 출발 노드까지 최단 경로 역추적

# 1로 만들기 2
`Silver 1` `12852`
```python
from sys import stdin
from collections import deque

input = stdin.readline

def BFS(start):
  queue = deque()
  queue.append([start])
  prevNodes = {}

  while queue:
    path = queue.popleft()
    nowNode = path[-1]

    if nowNode == 1:
      return backtracking(prevNodes, nowNode)

    if nowNode % 3 == 0 and (nowNode // 3) not in prevNodes:
      queue.append(path + [nowNode // 3])
      prevNodes[nowNode // 3] = nowNode

    if nowNode % 2 == 0 and (nowNode // 2) not in prevNodes:
      queue.append(path + [nowNode // 2])
      prevNodes[nowNode // 2] = nowNode

    if (nowNode - 1) not in prevNodes:
      queue.append(path + [nowNode - 1])
      prevNodes[nowNode - 1] = nowNode 

def backtracking(prevArr, target):
  backtrackingPath = []
  while target in prevArr:
    backtrackingPath.append(target)
    target = prevArr[target]
  backtrackingPath.append(N)
  backtrackingPath.reverse()
            
  return len(backtrackingPath)-1, backtrackingPath

if __name__ == "__main__":
  N = int(input())
  count, path = BFS(N)
  print(count)
  print(*path)
```

# 가장 긴 증가하는 부분 수열 4
`Gold 4` `14002`
```python
from sys import stdin
from bisect import bisect_left

input = stdin.readline

def LIS(start, numberList):
  memorize = [numberList[start]]
  valueToIndex = [(memorize[0], start)] # (value, index)

  for target in numberList:
    if memorize[-1] < target:
      memorize.append(target)
      valueToIndex.append((target, len(memorize)-1))
    else:
      idx = bisect_left(memorize, target)
      memorize[idx] = target
      valueToIndex.append((target, idx))
    
  return backtracking(valueToIndex, len(memorize)-1)

def backtracking(prevArr, check):
  backtrackingPath = []
  for i in range(len(prevArr)-1, -1, -1):
    if prevArr[i][1] == check:
      backtrackingPath.append(prevArr[i][0])
      check -= 1

  return len(backtrackingPath), backtrackingPath

if __name__ == "__main__":
  N = int(input())
  numberList = list(map(int, input().rstrip().split()))

  length, resultList = LIS(0, numberList)
  print(length)
  print(*reversed(resultList))
```

# 가장 긴 증가하는 부분 수열 5
`Platinum 5` `14003`
```python
from sys import stdin
from bisect import bisect_left

input = stdin.readline

def LIS(start, numberList):
  memorize = [numberList[start]]
  valueToIndex = [(memorize[0], start)] # (value, index)

  for target in numberList:
    if memorize[-1] < target:
      memorize.append(target)
      valueToIndex.append((target, len(memorize)-1))
    else:
      idx = bisect_left(memorize, target)
      memorize[idx] = target
      valueToIndex.append((target, idx))
    
  return backtracking(valueToIndex, len(memorize)-1)

def backtracking(prevArr, check):
  backtrackingPath = []
  for i in range(len(prevArr)-1, -1, -1):
    if prevArr[i][1] == check:
      backtrackingPath.append(prevArr[i][0])
      check -= 1

  return len(backtrackingPath), backtrackingPath

if __name__ == "__main__":
  N = int(input())
  numberList = list(map(int, input().rstrip().split()))

  length, resultList = LIS(0, numberList)
  print(length)
  print(*reversed(resultList))
```

# LCS 2
`Gold 4` `9252`
```python
from sys import stdin

input = stdin.readline

def LCS(strA, strB):
  memorize = [[0 for _ in range(len(strB)+1)] for _ in range(len(strA)+1)]

  for i in range(1, len(strA)+1):
    for j in range(1, len(strB)+1):
      if strA[i-1] == strB[j-1]:
        memorize[i][j] = memorize[i-1][j-1] + 1
      else:
        memorize[i][j] = max(memorize[i-1][j], memorize[i][j-1])

  return memorize[len(strA)][len(strB)], backtracking(memorize, len(strB), len(strA), strA)

def backtracking(prevArr, x, y, original):
  backtrackingPath = []
  while x>0 and y>0:
    if prevArr[y][x-1] == prevArr[y][x]:
      x -= 1
    elif prevArr[y-1][x] == prevArr[y][x]:
      y -= 1
    else:
      backtrackingPath.append(original[y-1])
      x -= 1
      y -= 1
    
  return reversed(backtrackingPath)

if __name__ == "__main__":
  AString = list(map(str, input().rstrip()))
  BString = list(map(str, input().rstrip()))
  
  count, result = LCS(AString, BString)
  print(count)
  print(''.join(result))
```

# 경찰차
`Platinum 4` `2618`
```python
imprt
```

# 숨바꼭질 4
`Gold 4` `13913`
```python

```

# DSLR
`Gold 4` `9019`
```python

```

# 최소비용 구하기 2
`Gold 3` `11779`
```python

```

# 플로이드 2
`Gold 2` `11780`
```python

```
