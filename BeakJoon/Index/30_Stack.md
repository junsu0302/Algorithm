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

```

# 오아시스 재결합
`Platinum 5` `3015`
```python

```
