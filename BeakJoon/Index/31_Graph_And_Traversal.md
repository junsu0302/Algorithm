# 그래프 (Graph)

그래프(Graph)는 노드(Node)와 간선(Edge)으로 구성되는 추상 자료구조이다. 그래프는 현실 세계의 다양한 상호 관계를 모델링하는 상황에 사용된다.

그래프의 주요 특징은 다음과 같다.
1. 노드(Node) : 그래프의 기본 요소 (데이터 저장)
2. 간선(Edge) : 노드와 노드를 연결하는 선 (관계)
3. 가중치(Weight) : 간선에 할당되는 경로의 비용
4. 방향성 : 간선의 연결이 단방향 or 양뱡향 설정

그래프의 종류는 다음과 같다.
1. 무방향 그래프(Undirected Graph) : 간선이 방향을 가지지 않는 그래프
   - 간선을 통해 양방향으로 이동 가능
2. 방향 그래프(Directed Graph) : 간선에 방향성이 있는 그래프
   - 한 노드에서 다른 노드로의 방향성 존재
3. 가중치 그래프(Weighted Graph) : 간선에 가중치가 부여된 그래프
   - 간선을 따라 이동하면 비용이 존재
4. 사이클 그래프(Cyclic Graph) : 하나 이상의 사이클(순환 경로)를 가진 그래프
5. 비순환 그래프(Acyclic Graph) : 사이클이 없는 그래프 ex) Tree

그래프 사용 사례는 다음과 같다.
1. 그래프 순회 : 그래프의 모든 노드를 순회하는 문제
   - DFS(깊이 우선 탐색) or BFS(너비 우선 탐색)
3. 최단 경로 문제 : 도 노드 간의 최단 경로를 찾는 문제
   - Dijkstra(다익스트라) or Bellman-Ford(벨만-포드) 알고리즘
5. 사이클 검사 : 그래프 내에 사이클 존재 여부 검사
   - DFS or Union-Find(유니온 파인드)
7. 위상 정렬 : 방향 그래프 내에서 노드들을 순서대로 나열
   - 위상 정렬 알고리즘
9. 구간 그래프 : 특정 구간 내에서 노드와 간선을 가진 그래프를 파악하여 구간 내 빠른 쿼리
    - 구간 트리 or 세그먼트 트리
11. 최소 신장 트리 : 그래프 내에 모든 노드를 연결하는 부분 그래프 중에서 간선의 가중치 합이 최소가 되는 경우를 찾는 문제
    - Kruskal(크루스칼) or Prim(프림) 알고리즘
13. 네트워크 흐름 문제 : 그래프 내에서 노드 간의 데이터 흐름을 조절하는 문제
    - Ford-Fulkerson(포드-풀커슨) or Edmonds-Karp(에드몬드-카프) 알고리즘
   
# 그래프 순회 (Graph Traversal)
그래프 순회(Graph Traversal)는 그래프 내의 모든 노드와 간선을 효율적으로 방문하는 과정이다. 일반적인 그래프 순회 방식은 다음 2가지가 있다.
- 깊이 우선 탐색 (DFS, Depth-First Search) : 한 경로를 따라 가능한 멀리까지 탐색한 후, 다른 경로를 따라 탐색
  1. 대기열(Stack)과 방문목록(Visited) 배열을 초기화
  2. 노드 0에 방문하여 아직 방문하지 않은 인접 노드를 대기열에 추가
  3. 인접 노드 중 가장 위에 있는 노드에 방문 후 Stack에서 pop, Visited에 push
  4. Stack이 비어있을 때까지 반
     
- 너비 우선 탐색 (BFS, Freadth-First Search) : 한 노드의 모든 이웃 노드들을 먼저 탐색한 후, 해당 이웃 노드들의 이웃 노드들을 순차적으로 탐색
  1. 대기열(Queue)과 방문목록(Visited) 배열을 초기화
  2. 노드 0을 Queue에 넣고 Visited에 방문한 것으로 표시
  3. 대기열 앞의 노드 0을 제거하고 방문하지 않은 이웃을 Queue에 추가, Visited 갱신
  4. Queue에 값을 추가 못할 떄까지 반복
  
그래프 순회의 사용 사례는 다음과 같다.
1. DFS (깊이 우선 탐색)
   - 연결된 요소 찾기 : 그래프 내에 연결된 요소들을 탐색하여 그룹화
   - 사이클 검사 : 그래프 내에 사이클 존재 여부 검사
   - 토폴로지 정렬 : 방향 그래프 내에서 노드를 정렬
   - 길 찾기 : 출발점부터 목적지까지의 경로 탐색
2. BFS (너비 우선 탐색)
   - 최단 경로 탐색 : 그래프 내에서 두 노드 간의 최단 경로 탐색
   - 네트워크 트래픽 분석 : 네트워크의 노드 간 트래픽 흐름을 분석
   - 레벨 순서 분석 : 트리 구조에서 각 레벨마다 노드들을 분석
  
이러한 그래프와 순회는 원하는 정보를 빠르게 탐색하는 데에 활용된다. 이를 통해 네트워크, 데이터베이스, 인공지능, 게임 개발 등에 활용된다.

# 알고리즘 수업 - 깊이 우선 탐색 1
`Silver 2` `24479`
```python
import sys
input = sys.stdin.readline

def DFS(start, graph):
  visited = [-1 for _ in range(N+1)] # 방문 여부 확인
  path = [0 for _ in range(N+1)] # 각 노드가 방문된 순서
  stack = [start]
  count = 1 # 방문 순서

  while stack:
    node = stack.pop() # 최상위 원소

    # 이미 방문된 최상단 노드
    if visited[node] == 1:
      continue

    # 방문이 아직 안 된 상태라면
    visited[node] = 1 # 방문 처리
    path[node] = count  # 방문 순서 할당
    count += 1

    # 해당 노드에 존재하는 하위 노드를 stack에 할당
    for adNode in graph[node]:
      if visited[adNode] == -1:
        stack.append(adNode)

  return path

if __name__ == "__main__":
  N, M, R = map(int, input().split())
  
  # 그래프 생성 : 각 노드마다 연결된 정보 파악
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  # 그래프의 각 노드에 대한 연결 정보 내림차순 정렬
  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=True)
  
  result = DFS(R, graph)

  print(*result[1:], sep='\n')
```

# 알고리즘 수업 - 깊이 우선 탐색 2
`Silver 2` `24480`
```python
import sys
input = sys.stdin.readline

def DFS(start, graph):
  visited = [-1 for _ in range(N+1)]
  path = [0 for _ in range(N+1)]
  stack = [start]
  count = 1 

  while stack:
    node = stack.pop() 

    if visited[node] == 1:
      continue

    visited[node] = 1 
    path[node] = count 
    count += 1

    for adNode in graph[node]:
      if visited[adNode] == -1:
        stack.append(adNode)

  return path

if __name__ == "__main__":
  N, M, R = map(int, input().split())
  
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=False)
  
  result = DFS(R, graph)

  print(*result[1:], sep='\n')
```

# 알고리즘 수업 - 너비 우선 탐색 1
`Silver 2` `24444`
```python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, graph):
  visited = [-1 for _ in range(N+1)] # 방문 여부 확인
  path = [0 for _ in range(N+1)] # 각 노드가 방문된 순서
  count = 1 # 방문 순서
  queue = deque([start])
  
  visited[start] = 1
  path[start] = count
  count += 1

  while queue:
    node = queue.popleft()

    for adNode in graph[node]:
      if visited[adNode] == -1:
        queue.append(adNode)
        visited[adNode] = 1
        path[adNode] = count
        count += 1

  return path

if __name__ == "__main__":
  N, M, R = map(int, input().split())
  
  # 그래프 생성 : 각 노드마다 연결된 정보 파악
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  # 그래프의 각 노드에 대한 연결 정보 오름차순 정렬
  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=False)
  
  result = BFS(R, graph)

  print(*result[1:], sep='\n')
```

# 알고리즘 수업 - 너비 우선 탐색 2
`Silver 2` `24445`
```python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, graph):
  visited = [-1 for _ in range(N+1)] # 방문 여부 확인
  path = [0 for _ in range(N+1)] # 각 노드가 방문된 순서
  count = 1 # 방문 순서
  queue = deque([start])
  
  visited[start] = 1
  path[start] = count
  count += 1

  while queue:
    node = queue.popleft()

    for adNode in graph[node]:
      if visited[adNode] == -1:
        queue.append(adNode)
        visited[adNode] = 1
        path[adNode] = count
        count += 1

  return path

if __name__ == "__main__":
  N, M, R = map(int, input().split())
  
  # 그래프 생성 : 각 노드마다 연결된 정보 파악
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  # 그래프의 각 노드에 대한 연결 정보 내림차 정렬
  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=False)
  
  result = BFS(R, graph)

  print(*result[1:], sep='\n')
```

# 바이러스
`Silver 3` `2606`
```python
# 연결된 요소를 찾는 문제이기 때문에 DFS를 사용한다.
import sys
input = sys.stdin.readline
  
def DFS(start, graph, n):
  visited = [-1 for _ in range(n+1)]
  stack = [start]
  count = 0

  while stack:
    node = stack.pop()

    if visited[node] == 1:
      continue

    visited[node] = 1
    count += 1

    for adNode in graph[node]:
      if visited[adNode] == -1:
        stack.append(adNode)

  return count - 1

if __name__ == "__main__":
  computerNumber = int(input())
  linkedNumber = int(input())
  
  graph = [[] for _ in range(computerNumber+1)]

  for _ in range(linkedNumber):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=True)

  result = DFS(1, graph, computerNumber)
  print(result)
```

# DFS와 BFS
`Silver 2` `1260`
```python
import sys
from collections import deque
input = sys.stdin.readline
  
def DFS(start, graph, n):
  visited = [-1 for _ in range(n+1)]
  path = []
  stack = [start]

  while stack:
    node = stack.pop() 

    if visited[node] == 1:
      continue

    visited[node] = 1
    path.append(node)

    for adNode in graph[node]:
      if visited[adNode] == -1:
        stack.append(adNode)

  return path

def BFS(start, graph, n):
  visited = [-1 for _ in range(n+1)]
  path = [] 
  queue = deque([start])
  
  visited[start] = 1
  path.append(start)

  while queue:
    node = queue.popleft()

    for adNode in graph[node]:
      if visited[adNode] == -1:
        queue.append(adNode)
        visited[adNode] = 1
        path.append(adNode)

  return path

if __name__ == "__main__":
  N, M, V = map(int, input().rstrip().split())
  
  graph = [[] for _ in range(N+1)]

  for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

  # DFS에서 인접한 정점 중 작은 수부터 접근하기 위해서는 내림차순으로 정렬한다.
  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=True)
  DFSResult = DFS(V, graph, N)

  # BFS에서 인접한 정점 중 작은 수부터 접근하기 위해서는 오름차순으로 정렬한다.
  for idx in range(1, len(graph)):
    graph[idx].sort(reverse=False)
  BFSResult = BFS(V, graph, N)

  print(' '.join(map(str, DFSResult)))
  print(' '.join(map(str, BFSResult)))
```

# 단지 번호 붙이기
`Silver 1` `2667`
```python
import sys
input = sys.stdin.readline

def DFS(x, y, graph, maxX, maxY):
  global count
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  stack = [(x, y)] 
  graph[y][x] = '0' # 방문한 곳 0으로 설정
  count += 1

  while stack:
    x, y = stack.pop()

    for i in range(4): # 상하좌우 확인
      nx = x + dx[i]
      ny = y + dy[i]

      # 정해진 범위 내의 인접한 좌표에 있는 경우
      if nx >= 0 and nx < maxX and ny >= 0 and ny < maxY and graph[ny][nx] == '1':
        stack.append((nx, ny))
        graph[ny][nx] = '0'
        count += 1

if __name__ == "__main__":
  N = int(input().rstrip())
  graph = [list(str(input().rstrip())) for _ in range(N)]

  result = []
  # 이중 for문으로 graph를 하나씩 돌면서 1인 구간 탐색 (시작점 탐색)
  for x in range(N):
    for y in range(N):
      if graph[y][x] == '1':
        count = 0
        DFS(x, y, graph, N, N)
        result.append(count)

  print(len(result))
  result.sort()
  print('\n'.join(map(str, result)))
```

# 유기농 배추
`Silver 2` `1012`
```python
import sys
input = sys.stdin.readline

def DFS(x, y, graph, maxX, maxY):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  stack = [(x, y)]
  graph[y][x] = 0

  while stack:
    x, y = stack.pop()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < maxX and ny >= 0 and ny < maxY and graph[ny][nx] == 1:
        stack.append((nx, ny))
        graph[ny][nx] = 0

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
        
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
      c, r = map(int, input().rstrip().split())
      graph[r][c] = 1

    result = 0
    for x in range(M):
      for y in range(N):
        if graph[y][x] == 1:
          DFS(x, y, graph, M, N)
          result += 1

    print(result)
```

# 미로 탐색
`Silver 1` `2178`
```python
# 최단경로를 찾아야하는 문제이므로 BFS를 사용했다.
import sys
from collections import deque
input = sys.stdin.readline

def BFS(startX, startY, graph, maxX, maxY):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  visited = [[0 for _ in range(maxX)] for _ in range(maxY)]
  queue = deque([(startX, startY)])
  visited[startY][startX] = 1
  graph[startY][startX] = '-1'

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < maxX and 0 <= ny < maxY and graph[ny][nx] == '1':
        queue.append((nx, ny))
        visited[ny][nx] = visited[y][x] + 1
        graph[ny][nx] = '-1'

  return visited[maxY-1][maxX-1]
  
if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())
  maze = [list(str(input().rstrip())) for _ in range(N)]

  result = BFS(0, 0, maze, M, N)
  print(result)
```

# 숨바꼭질
`Silver 1` `1697`
```python
# 두 사람이 만날 수 있는 최단 거리를 구하기 때문에 BFS 사용
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, maxX, target):
  visited = [0 for _ in range(maxX)]
  queue = deque([start])

  while queue:
    x = queue.popleft()
    if x == target:
      return visited[x]
    for nx in (x-1, x+1, 2*x):
      if 0 <= nx < maxX and not visited[nx]:
        queue.append(nx)
        visited[nx] = visited[x] + 1
      
  return visited[maxX-1]

if __name__ == "__main__":
  N, K = map(int, input().rstrip().split())
  result = BFS(N, 100001, K)
  print(result)
```

# 나이트의 이동
`Silver 1` `7562`
```python
# 시작 점과 목표 지점의 최단 거리를 구하는 문제이기 떄문에 BFS 사용
import sys
from collections import deque
input = sys.stdin.readline

def BFS(startX, startY, boardLen, targetX, targetY):
  dx = [1, 1, 2, 2, -1, -1, -2, -2]
  dy = [2, -2, 1, -1, 2, -2, 1, -1]
  
  visited = [[0 for _ in range(boardLen)] for _ in range(boardLen)]
  path = [[0 for _ in range(boardLen)] for _ in range(boardLen)]
  queue = deque([(startX, startY)])
  visited[startY][startX] = 1
  path[startY][startX] = 0
  
  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < boardLen and 0 <= ny < boardLen and visited[ny][nx] == 0:
        queue.append((nx, ny))
        visited[ny][nx] = 1
        path[ny][nx] = path[y][x] + 1

    if x == targetX and y == targetY:
      break

  return path[targetY][targetX]

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    boardLen = int(input())
    startX, startY = map(int, input().rstrip().split())
    targetX, targetY = map(int, input().rstrip().split())

    result = BFS(startX, startY, boardLen, targetX, targetY)
    print(result)
```

# 토마토
`Gold 5` `7576`
```python
# 상자안에서 값이 1인 토마토와 값이 0인 토마토와의 최단 거리를 구하는 문제라고 생각하여 BFS 사용
import sys
from collections import deque
input = sys.stdin.readline

def BFS(startPoint, graph, maxX, maxY):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  visited = [[0 for _ in range(maxX)] for _ in range(maxY)]
  path = [[0 for _ in range(maxX)] for _ in range(maxY)]
  queue = deque()
  maxValue = 0

  for x, y in startPoint:
    queue.append((x, y))
    visited[y][x] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < maxX and 0 <= ny < maxY and visited[ny][nx] == 0 and graph[ny][nx] != -1:
        queue.append((nx, ny))
        visited[ny][nx] = 1
        path[ny][nx] = path[y][x] + 1
        if path[ny][nx] > maxValue:
          maxValue = path[ny][nx]

  filledBoard = filledBlank(path, startPoint, graph, maxX, maxY)
  for item in filledBoard:
    if 0 in item:
      return -1
  
  return maxValue

def filledBlank(path, startPoint, graph, maxX, maxY):
  for x, y in startPoint:
    path[y][x] = -1

  for y in range(maxY):
    for x in range(maxX):
      if graph[y][x] == -1:
        path[y][x] = -1

  return path
  

def findStartPoint(board, xLen, yLen):
  output = []
  for y in range(yLen):
    for x in range(xLen):
      if board[y][x] == 1:
        output.append([x, y])

  return output
  
if __name__ == "__main__":
  M, N = map(int, input().rstrip().split())
  tomatoBox = [list(map(int, input().rstrip().split())) for _ in range(N)]
  startPoint = findStartPoint(tomatoBox, M, N)

  result = BFS(startPoint,tomatoBox, M, N)
  print(result)
```

# 토마토
`Gold 5` `7569`
```python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(startPoint, graph, maxX, maxY, maxZ):
  dx = [1, -1, 0, 0, 0, 0]
  dy = [0, 0, 1, -1, 0 ,0]
  dz = [0, 0, 0, 0, 1, -1]

  visited = [[[0 for _ in range(maxX)] for _ in range(maxY)] for _ in range(maxZ)]
  path = [[[0 for _ in range(maxX)] for _ in range(maxY)] for _ in range(maxZ)] 
  queue = deque()
  maxValue = 0

  for x, y, z in startPoint:
    queue.append((x, y, z))
    visited[z][y][x] = 1

  while queue:
    x, y, z = queue.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < maxX and 0 <= ny < maxY and 0 <= nz < maxZ and visited[nz][ny][nx] == 0 and graph[nz][ny][nx] != -1:
        queue.append((nx, ny, nz))
        visited[nz][ny][nx] = 1
        path[nz][ny][nx] = path[z][y][x] + 1
        if path[nz][ny][nx] > maxValue:
          maxValue = path[nz][ny][nx]

  filledBoard = filledBlank(path, startPoint, graph, maxX, maxY, maxZ)
  for board in filledBoard:
    for item in board:
      if 0 in item:
        return -1
  
  return maxValue

def filledBlank(path, startPoint, graph, maxX, maxY, maxZ):
  for x, y, z in startPoint:
    path[z][y][x] = -1

  for z in range(maxZ):
    for y in range(maxY):
      for x in range(maxX):
        if graph[z][y][x] == -1:
          path[z][y][x] = -1

  return path
  

def findStartPoint(board, xLen, yLen, zLen):
  output = []
  for z in range(zLen):
    for y in range(yLen):
      for x in range(xLen):
        if board[z][y][x] == 1:
          output.append([x, y, z])

  return output
  
if __name__ == "__main__":
  M, N, H = map(int, input().rstrip().split())
  tomatoBox = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
  startPoint = findStartPoint(tomatoBox, M, N, H)

  result = BFS(startPoint,tomatoBox, M, N, H)
  print(result)
```

# 뱀과 사다리 게임
`Gold 5` `16928`
```python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(ladder, snake):
  dice = [6, 5, 4, 3, 2, 1]
  visited = [0 for _ in range(101)]
  queue = deque([(1, 0)]) # (현재 칸, 주사위를 던진 횟수)

  while queue:
    point, throws = queue.popleft()

    if point == 100:
      return throws

    for move in dice:
      newPoint = point + move

      if newPoint <= 100 and not visited[newPoint]:
        visited[newPoint] = 1

        if newPoint in ladder:
          queue.append((ladder[newPoint], throws + 1))
        elif newPoint in snake:
          queue.append((snake[newPoint], throws + 1))
        else:
          queue.append((newPoint, throws + 1))

if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())

  ladder = dict()
  for _ in range(N):
    u, v = map(int, input().rstrip().split())
    ladder[u] = v

  snake = dict()
  for _ in range(M):
    u, v = map(int, input().rstrip().split())
    snake[u] = v

  result = BFS(ladder, snake)
  print(result)
```

# 벽 부수고 이동하기
`Gold 3` `2206`
```python

```

# 이분 그래프
`Gold 4` `1707`
```python

```
