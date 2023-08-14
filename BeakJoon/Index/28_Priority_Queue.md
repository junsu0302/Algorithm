# 우선순위 큐 (Peiority Queue)
우선순위 큐(Peiority Queue)는 데이터의 우선순위를 가지고 있는 자료구조로, 가장 높은 우선순위를 가진 항목에 접근할 수 있는 자료구조다. 

우선순위 큐는 다음과 같은 특징을 갖는다.
1. 높은 우선순위의 원소에 우선 접근
   가장 높은 우선순위를 가진 원소에 먼저 접근
2. 삽입 및 삭제 연산의 높은 효율성
   힙의 특성을 활용하여 삽입 및 삭제 연산을 O(logN) 시간에 수행
3. 데이터 정렬
   원소들이 정렬된 상태로 저장

우선순위 큐는 다음과 같이 구현된다.
- 배열 기반
  배열을 사용하여 우선순위가 높은 순서대로 정렬된 배열을 유지
  삽입 및 연산 시 배열의 재구성이 필요하여 효율성이 떨어짐
- 힙 기반
  이진 트리 형태를 원소들을 저장하고, 힙 속성을 유지
  최소 힙 or 최대 힙의 형태를 취해 삽입 및 삭제 연산 시 효율성 보장

우선순위 큐는 다음과 같은 사례에서 활용될 수 있다.
1. 다익스트라 알고리즘
   최단 경로를 찾는 알고리즘으로, 다음에 방문할 노드를 선택할 때 우선순위 큐를 사용하여 가장 가까운 노드 선택
2. 허프만 코딩
   데이터 압축 알고리즘에서 사용, 빈도수가 높은 문자에 낮은 비트를 할당하여 데이터 압축
3. 작업 스케줄링
   우선순위 큐를 사용하여 작업을 관리 및 처리
4. 이벤트 시뮬레이션
   시간에 따라 발생하는 이벤트의 시뮬레이션 처리 및 다음 이벤트 선택

# 최대 힙
`Sliver 2` `11279`
```Python
import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
  x = int(input())
  if x:
    # heap에 (우선순위, 값)의 형태로 저장
    hq.heappush(heap, (-x, x))  # (-value, value)의 형태로 저장
  else:
    if len(heap) >= 1:
      print(hq.heappop(heap)[1])
    else:
      print(0)
```

# 최소 힙
`Sliver 2` `1927`
```Python
import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
  x = int(input())
  if x != 0:
    hq.heappush(heap, x)
  else:
    try:
      print(hq.heappop(heap))
    except:
      print(0)
```

# 절댓값 힙
`Sliver 1` `11286`
```Python
import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
  x = int(input())
  if x != 0:
    hq.heappush(heap, (abs(x), x))
  else:
    try:
      print(hq.heappop(heap)[1])
    except:
      print(0)
```
