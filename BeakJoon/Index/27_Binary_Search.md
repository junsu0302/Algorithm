이분 탐색(Binary Search)은 정렬된 배열에서 특정 값을 찾는 알고리즘이다. 탐색 범위를 반씩 줄여가면서 원하는 값을 빠르게 찾는 방법이다. 이분 탐색은 시간 복잡도가 O(log n)으로 매우 효율적이다.

이분 탐색은 다음과 같은 단계로 동작한다:
1. 정렬된 배열에서 시작, 중간, 끝 위치의 인덱스를 구한다.
2. 중앙 위치의 값과 찾고자 하는 값을 비교한다.
3. 중간 값이 찾고자 하는 값과 일치하면 종료한다.
4. 중간 값이 찾고자 하는 값보다 크면 끝 위치를 중간 위치보다 하나 작은 값으로 설정하여 탐색 범위를 줄인다.
5. 중간 값이 찾고자 하는 값보다 작으면 시작 위치를 중간 위치보다 하나 큰 값으로 설정하여 탐색 범위를 줄인다.
6. 위 과정을 탐색 범위가 축소될 때까지 반복한다.

이분 탐색은 일반적으로 정렬된 배열 or 리스트에서 특정 값의 존재 여부를 빠르게 확인하는데 사용한다. 대표적으로 데이터베이스 인덱스 겁색, 계산 문제에서 최적값 찾기, 정렬된 리스트 내에서의 범위 찾기 등에서 활용된다.
뿐만 아니라 이진 검색 트리와 같은 자료 구조를 구현하는데 사용되기도 한다.

# 수 찾기
`Silver 4` `1920`
```python
import sys
input = sys.stdin.readline

def binarySearch(start, end, target):
  if start > end:
    return 0

  mid = (start + end) // 2
  if target == inputData[mid]:
    return 1
  elif target > inputData[mid]:
    return binarySearch(mid+1, end, target)
  elif target < inputData[mid]:
    return binarySearch(start, mid-1, target)
  
if __name__ == "__main__":
  N = int(input())
  inputData = sorted(list(map(int, input().rstrip().split())))
  M = int(input())
  targets = list(map(int, input().rstrip().split())) 

  for idx in targets:
    print(binarySearch(0, N-1, idx))
```

# 숫자 카드 2
`Silver 4` `10816`
```python
import sys
input = sys.stdin.readline

def binarySearch(start, end, target):
  if start > end:
    return 0

  mid = (start + end) // 2
  if target == inputData[mid]:
    return resultDict[target]
  elif target > inputData[mid]:
    return binarySearch(mid+1, end, target)
  elif target < inputData[mid]:
    return binarySearch(start, mid-1, target)
  
if __name__ == "__main__":
  N = int(input())
  inputData = sorted(list(map(int, input().rstrip().split())))
  M = int(input())
  targets = list(map(int, input().rstrip().split())) 

  resultDict = {}
  for idx in inputData:
    if idx in resultDict:
      resultDict[idx] += 1
    else:
      resultDict[idx] = 1

  for target in targets:
    print(binarySearch(0, N-1, target), end=' ')
```

# 랜선 자르기
`Silver 2` `1654`
```python
import sys
input = sys.stdin.readline

def binarySearch(start, end):
  if start > end:
    return 0

  mid = (start + end) // 2
  count = targetCount(mid)
  if count >= N:
    return max(mid, binarySearch(mid+1, end))
  else:
    return binarySearch(start, mid-1)

def targetCount(targetLen):
  count = 0
  for idx in inputData:
    count += idx // targetLen

  return count

if __name__ == "__main__":
  K, N = map(int, input().rstrip().split())
  inputData = [int(input()) for _ in range(K)]

  print(binarySearch(1, max(inputData)))
```

# 나무 자르기
`Silver 2` `2805`
```python
import sys
input = sys.stdin.readline

def binarySearch(start, end):
  if start > end:
    return -1

  mid = (start + end) // 2
  count = restLenCount(mid)
  if count >= M:
    return max(mid, binarySearch(mid+1, end))
  else:
    return binarySearch(start, mid-1)

def restLenCount(target):
  restLen = 0
  for idx in trees:
    if idx > target:
      restLen += idx - target

  return restLen

if __name__ == "__main__":
  N, M = map(int, input().rstrip().split())
  trees = list(map(int, input().rstrip().split()))
  result = binarySearch(0, max(trees))
  print(result)
```

# 공유기 설치
`Gold 4` `2110`
```python
import sys
input = sys.stdin.readline

def binarySearch(start, end):
  if start > end:
    return -1

  mid = (start + end) // 2
  current = coordinates[0]
  count = 1

  for i in range(1, len(coordinates)):
    if coordinates[i] >= current + mid:
      current = coordinates[i]
      count += 1

  if count >= C:
    return max(mid, binarySearch(mid+1, end))
  else:
    return binarySearch(start, mid-1)
  
if __name__ == "__main__":
  N, C = map(int, input().rstrip().split())
  coordinates = sorted([int(input()) for _ in range(N)])
  print(binarySearch(1, coordinates[-1] - coordinates[0]))
```

# K번째 수
`Gold 2` `1300`
```python
import sys
import math
input = sys.stdin.readline

def countIndex(N, x):
  tmp = int(math.sqrt(x))

  targetSum = 0
  for i in range(1, tmp+1):
    targetSum += min(N, x//i)
  targetSum = 2 * targetSum - tmp*tmp
  return targetSum

def binarySearch(start, end):
  if start > end:
    return start

  mid = (start + end) // 2
  count = countIndex(N, mid)

  if count >= K:
    return binarySearch(start, mid-1)
  elif count < K:
    return binarySearch(mid+1, end)
    
if __name__ == "__main__":
  N = int(input())
  K = int(input())

  print(binarySearch(1, N*N))
```

# 가장 긴 증가하는 부분 수열 2
`Gold 2` `12015`
```python
import sys
from collections import deque
input = sys.stdin.readline

def binarySearch(start, end, target, arr):
  if start > end:
    return start

  mid = (start + end) // 2
  if arr[mid] >= target:
    return binarySearch(start, mid - 1, target, arr)
  elif arr[mid] < target:
    return binarySearch(mid + 1, end, target, arr)

def makeSequence():
  for idx in sequence:
    if not stack or stack[-1] < idx:
      stack.append(idx)
    else:
      tmp = binarySearch(0, len(stack) - 1, idx, stack)
      stack[tmp] = idx

  return len(stack)

if __name__ == "__main__":
  N = int(input())
  sequence = list(map(int, input().rstrip().split()))
  stack = deque()
  print(makeSequence())
```
시간 초과 방지를 위한 모듈 사용

```python
import sys
from bisect import bisect_left
input = sys.stdin.readline

def makeSequence():
  stack = []
  for idx in sequence:
    if not stack or stack[-1] < idx:
      stack.append(idx)
    else:
      tmp = bisect_left(stack, idx)  # bisect_left 사용
      stack[tmp] = idx

  return len(stack)

if __name__ == "__main__":
  N = int(input())
  sequence = list(map(int, input().rstrip().split()))
  print(makeSequence())
```
