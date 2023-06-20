a

# 하노이
```python
import sys
input = sys.stdin.readline

def hanoi(n, a, b, c):
  if n == 1:
    print(a, c)
    return

  hanoi(n-1, a, c, b)
  print(a, c)
  hanoi(n-1, b, a, c)

if __name__ == "__main__":
  N = int(input())
  print(2 ** N - 1)
  if N <= 20:
    hanoi(N, 1, 2, 3)
```

# A와 B
```python
import sys
input = sys.stdin.readline

def check(word):
  if word == S:
    return 1
  if len(word)<=len(S):
    return 0

  result = 0
  if word[-1] == 'A':
    result = check(word[:-1])
    
  if result == 1:
    return 1

  if word[0] == 'B':
    tmp = word[::-1]
    result = check(tmp[:-1])

  return result

if __name__ == "__main__":
  S = input().rstrip()
  T = input().rstrip()
  result = check(T)
  print(result)
```
