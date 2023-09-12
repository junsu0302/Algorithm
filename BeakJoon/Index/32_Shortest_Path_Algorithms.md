# 최단 경로 알고리즘 (Shortest Path Algorithm)

최단 경로 알고리즘(Shortest Path Algorithm)은 그래프에서 두 노드 사이의 가장 짧은 경로를 찾는 알고리즘이다. 경로의 길이는 간선의 가중치(Weight)의 합으로 측정한다.

최단 경로 알고리즘의 특징은 다음과 같다.
1. 목적 지점까지의 최단 경로 탐색
2. 가중 그래프 : 간선에 가중치가 할당되어 경로의 길이 탐색
3. 유향 및 무향 그래프
4. 최적 부분 구조 : 큰 문제를 작은 부분 문제로 나누어 최적해의 결합을 통해 전체 최적해 탐색 
  
최단 경로 알고리즘의 종류는 다음과 같다.
## Dijkstra Algorithm
음수 가중치를 가진 간선이 없는 그래프에서 한 노드에서 다른 모든 노드까지의 최단 경로를 찾는 방법이다.
- 특징
  1. 그리디 알고리즘(Greed Algorithm)의 일종
  2. 우선순위 큐를 사용하여 최소 거리 정점을 선택
- 구현 방법
  1. 시작 정점의 최단 경로를 0으로 초기화, 나머지 정점들의 최단 경로를 무한대로 초기화
  2. 시작 정점을 우선순위 큐에 삽입
  3. 우선순위 큐에서 가장 짧은 경로를 가지는 정점을 선택하고, 해당 정점을 기준으로 인접한 정점들의 최단 경로 갱신
  4. 모든 노드를 방문할 때까지 위 과정 반복
## Bellman-Ford Algorithm
음수 가중치를 가진 간선을 포함한 그래프에서도 사용 가능한 한 노드에서 모든 노드까지의 최단 경로를 찾는 방법이다.
- 특징
  1. 동적 계획법(Dynamic Programming)의 일종
  2. 배열을 사용하여 각 정점의 최단 경로를 저장
- 구현 방법
  1. 시작 정점의 최단 경로를 0으로 초기화, 나머지 정점들의 최단 경로를 무한대로 초기화
  2. 간선들을 반복하여 현재까지의 최단 경로를 갱신
  3. 모든 간선을 반복하여 최단 경로 생신
## Floyd-Warshall Algorithm
모든 정점 쌍 간의 최단 경로를 찾을 때 사용한다. 각 정점을 경유지로 최단 경로를 계산한다.
- 특징
  1. 다이나믹 프로그램(Dynamic Programming)의 일종
  2. 3중 반복문을 통해 구현
  3. 인접 행렬을 통해 각 정점 쌍 사이의 거리 저장
- 구현 방법
  1. 모든 노드 쌍 사이의 최단 경로를 초기화
  2. 모든 중간 노드를 순회하면서 해당 중간 노드를 경유하는 경로가 더 짧으면 최단 경로 갱신
  3. 위 과정을 모든 노드와 중간 노드에 대해 반복

# 최단경로
`Gold 4` `1753`
```python
from sys import stdin, maxsize
from heapq import heappop, heappush

input = stdin.readline
INF = maxsize

def Dijkstra(start, graph):
  dp = [INF for _ in range(V+1)]
  visited = [0 for _ in range(V+1)]
  heap = [(0, start)]
  dp[start] = 0

  while heap:
    nowWeight, nowNode = heappop(heap)
    visited[nowNode] = 1

    if dp[nowNode] >= nowWeight:
      for nextNode, nextWeight in graph[nowNode]:
        nextWeight = nextWeight + nowWeight
        if nextWeight < dp[nextNode] and visited[nextNode] == 0:
          dp[nextNode] = nextWeight
          heappush(heap, (nextWeight, nextNode))
  return dp

if __name__ == "__main__":
  V, E = map(int, input().rstrip().split())
  K = int(input())

  graph = [[] for _ in range(V+1)]
  for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))

  result = Dijkstra(K, graph)
  for i in range(1, V+1):
    print("INF" if result[i] == INF else result[i])
```

# 특정한 최단 경로
`Gold 4` `1504`
```python

```

# 숨바꼭질 3
`Gold 5` `13549`
```python

```

# 미확인 도착지
`Gold 2` `9370`
```python

```

# 타임머신
`Gold 4` `11657`
```python

```

# 플로이드
`Gold 4` `11404`
```python

```

# 운동
`Gold 4` `1956`
```python

```
