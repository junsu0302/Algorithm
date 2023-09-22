# 투 포인터 (Two Pointer)

투 포인터 알고리즘(Two Pointer Algorithm)은 두 개의 포인터를 사용하여 특정 조건을 만족하는 부분을 찾거나 원하는 결과를 얻는데 사용한다. 이 알고리즘은 연속적인 데이터에서 일정 범위를 처리 or 검색할 때 유용하다.

투 포인터의 특징은 다음과 같다.
1. 선형 데이터 구조에서 사용
2. 두 개의 포인터를 사용하여 시작 포인터와 끝 포인터로 데이터 처리
3. 시간 복잡도가 O(n)으로 효율적인 동작
4. 상수 공간을 활용하여 낮은 공간 복잡도

투 포인터의 활용 사례는 다음과 같다.
- 두 수의 합
- 슬라이딩 윈도우
- 배열 정렬
- 연결 리스트

# 두 수의 합
`Sliver 3` `3273`
```python
from sys import stdin
input = stdin.readline

def twoPointer(numberList, target):
  numberList.sort()
  left = 0
  right = len(numberList) - 1

  count = 0
  while left < right:
    leftNumber = numberList[left]
    rightNumber = numberList[right]

    if leftNumber + rightNumber > target:
      right -= 1
    elif leftNumber + rightNumber < target:
      left += 1
    else:
      count += 1
      left += 1
      right -= 1

  return count

if __name__ == "__main__":
  N = int(input())
  numberList = list(map(int, input().rstrip().split()))
  x = int(input())

  result = twoPointer(numberList, x)
  print(result)
```

# 두 용액
`Gold 5` `2470`
```python
from sys import stdin, maxsize
input = stdin.readline

INF = maxsize

def findNumber(numberList):
  numberList.sort()
  left = 0
  right = len(numberList) - 1

  targetList = [0, 0]
  targetValue = INF
  while left < right:
    leftNumber = numberList[left]
    rightNumber = numberList[right]
    currentSum = leftNumber + rightNumber

    if currentSum == 0:
      targetList = [leftNumber, rightNumber]
      return targetList

    if currentSum > 0:
      right -= 1
    elif currentSum < 0:
      left += 1

    if abs(currentSum) < abs(targetValue):
      targetList = [leftNumber, rightNumber]
      targetValue = currentSum
  
  return targetList

if __name__ == "__main__":
  N = int(input())
  solutionList = list(map(int, input().rstrip().split()))
  
  result = findNumber(solutionList)
  print(*result)
```

# 부분합
`Gold 4` `1806`
```python
from sys import stdin
input = stdin.readline

def twoPointer(numberList, target):
  start = 0
  valueSum = 0
  for end, value in enumerate(numberList, 1):
    valueSum += value
    if valueSum >= target:
      break

  if valueSum < target:
    return 0

  while True:
    valueSum -= numberList[start]
    start += 1
    if valueSum < target:
      if end == len(numberList):
        start -= 1
        break
      valueSum += numberList[end]
      end += 1
    
  return end - start

if __name__ == "__main__":
  N, S = map(int, input().rstrip().split())
  numberList = list(map(int, input().rstrip().split()))

  result = twoPointer(numberList, S)
  print(result)
```

# 소수의 연속합
`Gold 3` `1644`
```python
from sys import stdin
input = stdin.readline

def getPrimes(N): # 에라토스테네스의 
    isPrime = [True for _ in range(N+1)]
    for i in range(3, int(N**0.5) + 1, 2):
        if isPrime[i]:
            isPrime[i*i :: 2*i] = [False] * ((N - i * i) // (2 * i) + 1)
    return [2] + [i for i in range(3, N+1, 2) if isPrime[i]]

def twoPointer(numberList, target):
  start, end = 0, 0
  valueSum = 0
  count = 0

  while True:
    if valueSum < target:
      if end == len(numberList):
        break
      valueSum += numberList[end]
      end += 1
    elif valueSum > target:
      valueSum -= numberList[start]
      start += 1
    else:
      count += 1
      valueSum -= numberList[start]
      start += 1

  return count

if __name__ == "__main__":
  N = int(input())
  primeList = getPrimes(N)

  result = twoPointer(primeList, N)
  print(result)
```

# 냅색문제
`Gold 1` `1450`
```python
from sys import stdin
from bisect import bisect_left
input = stdin.readline

def meetInTheMiddle(numberList, target):
  """
  Meet in the Middle Algorithm
  1. 주어진 입력 공간을 두 부분으로 분할
  2. 각 부분에 대해 가능한 모든 상태를 계산하고 저장
  3. 두 부분에서 얻은 결과를 조합하여 최종 결과 도출
  """
  N = len(numberList)
  AList = numberList[:N//2]
  BList = numberList[N//2:]
  
  ASum = bruteforce(AList, N, target)
  BSum = bruteforce(BList, N, target)
  BSum.sort() # binary Search를 위해 정렬

  count = 0
  for idx in ASum:
    if target - idx >= 0:
      count += bisect_left(BSum, target-idx+1) # binarySearch 후 index 반환

  return count

def bruteforce(numberList, N, target):
  result = [0]
  for idx in numberList:
    tmp = []
    for rst in result:
      if idx + rst <= target:
        tmp.append(idx+rst)
    result += tmp
    
  return result

if __name__ == "__main__":
  N, C = map(int, input().rstrip().split())
  weightList = list(map(int, input().rstrip().split()))

  result = meetInTheMiddle(weightList, C)
  print(result)
```
