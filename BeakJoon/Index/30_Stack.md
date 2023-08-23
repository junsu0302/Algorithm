# 스택

스택(Stack)은 데이터를 저장하고 관리하는 자료구조이다. 후입선출(LIFO) 방식으로 작동하기 때문에 마지막에 추가된 데이터가 가장 먼저 제거된다.

스택은 다음의 원칙을 따른다.
1. LIFO : 가장 최근에 삽입된 데이터가 가장 먼저 제거
2. Push : 스택에 데이터 삽입
3. Pop : 스택에서 최상위 데이터를 제거하고 반환
4. Top : 스택의 최상위 데이터를 조회

스택의 종류는 다음과 같다.
1. 배열 기반 스택(Array-Based Stack) : 크기가 고정되어 있음
2. 연결 리스트 기반 스택(Linked List-Based Stack) : 동적 크기 조정이 가능하며 메모리를 효율적으로 활용
3. 동적 배열 기반 스택(Dynamic Array-Based Stack) : 크기 조정이 가능

스택의 활용 사례는 다음과 같다.
1. 함수 호출 : 호출된 함수의 정보를 스택에 저장하여, 함수 종료 시 복귀 주소 및 지역 변수 등을 복구
2. 수식 평가 : 후위 표기법(Postfix Notation)을 사용하여 계산할 때, 연산자와 피연산자를 스택에 저장하여 계산
3. 재귀 알고리즘 : 재귀 함수 호출 시, 함수 호출 순서와 관련된 정보 관리

# 문자열 폭발
`Gold 4` `9935`
```python
import sys
input = sys.stdin.readline

if __name__ == "__main__":
  inputString = input().rstrip()
  target = input().rstrip()

  lastTarget = target[-1]
  targetLen = len(target)

  stack = []
  for idx in inputString:
    stack.append(idx)
    if stack[-1] == lastTarget:
      if ''.join(stack[-targetLen:]) == target:
        del stack[-targetLen:]

  if stack:
    print(''.join(stack))
  else:
    print('FRULA')
```

# 오큰수
`Gold 4` `17298`
```python
import sys
input = sys.stdin.readline

def NGF(sequence):
  n = len(sequence)
  stack = []
  for i in range(n):
    while stack and sequence[i] > sequence[stack[-1]]:
      sequence[stack.pop()] = sequence[i]
    stack.append(i)
  while stack:
    sequence[stack.pop()] = -1

  return sequence

if __name__ == "__main__":
  N = int(input())
  sequence = list(map(int, input().rstrip().split()))
  result = NGF(sequence)
  print(' '.join(map(str, result)))
  
```

# 오등큰수
`Gold 3` `17299`
```python
import sys
from collections import Counter

def NGF(sequence):
  N = len(sequence)
  stack = []
  result = [-1] * N
  counter = Counter(sequence)
  
  for i in range(N):
    while stack and counter[sequence[stack[-1]]] < counter[sequence[i]]:
      index = stack.pop()
      result[index] = sequence[i]
    stack.append(i)

  return result

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    sequence = list(map(int, input().split()))
    result = NGF(sequence)
    print(' '.join(map(str, result)))
```

# 히스토그램
`Platinum 5` `1725`
```python
import sys
input = sys.stdin.readline

def findArea(n, inputList):
  stack = []
  result = 0
  for i in range(N):
    while stack and inputList[stack[-1]] > inputList[i]:
      height = inputList[stack.pop()]
      width = i
      if stack:
        width = i - stack[-1] - 1
      result = max(result, height * width)
    stack.append(i)
    
  while stack:
    height = inputList[stack.pop()]
    width = n
    if stack:
      width = n - stack[-1] - 1
    result = max(result, height * width)
    
  return result

if __name__ == '__main__':
  N = int(input())
  inputList = [int(input()) for _ in range(N)]

  result = findArea(N, inputList)
  print(result)
```

# 오아시스 재결합
`Platinum 5` `3015`
```python
import sys
input = sys.stdin.readline

def findArea(inputList):
  stack = []
  result = 0
  for idx in inputList:
    while stack and stack[-1][0] < idx:
      result += stack.pop()[1]

    if not stack:
      stack.append((idx, 1))
      continue

    if stack[-1][0] == idx:
      count = stack.pop()[1]
      result += count

      if stack:
        result += 1
      stack.append((idx, count+1))
    else:
      stack.append((idx, 1))
      result += 1
    
  return result

if __name__ == '__main__':
  N = int(input())
  inputList = [int(input()) for _ in range(N)]

  result = findArea(inputList)
  print(result)
```
