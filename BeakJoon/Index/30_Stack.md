# 스택

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

```
