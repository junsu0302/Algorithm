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

# 압축
```python
from collections import deque
import sys
input = sys.stdin.readline

def decompression():
  stack = deque()
  cnt=0
  before=''
  
  for c in input_data:
    if c == '(':
      stack.append([cnt-1,before])
      cnt = 0
    elif c == ')':
      info = stack.pop()
      cnt = cnt*info[1]+info[0]
    else:
      cnt += 1
      before = int(c)
  return cnt

if __name__ == "__main__":
  input_data = input().strip()
  result = decompression()
  print(result)
```

# Moo 게임
```python
import sys
input = sys.stdin.readline

def make_Moo(n, depth, before_len):
  next_len = 2 * before_len + depth + 3

  if n <= 3:
    print(moo[n-1])
    return

  if next_len < n:
    make_Moo(n, depth+1, next_len)
  else:
    if before_len < n and n <= before_len + depth + 3:
      if n - before_len != 1:
        print('o')
      else:
        print('m')
      return
    else:
      make_Moo(n-(before_len + depth + 3), 1, 3)
     
if __name__ == "__main__":
  N = int(input())
  moo = ['m', 'o', 'o']
  make_Moo(N, 1, 3)
```

# 홀수 홀릭 호석
```python
import sys
input = sys.stdin.readline

def count_odd(n):
  cnt = 0
  for i in n:
    if int(i) & 1:
      cnt += 1
  return cnt


def dividied(n, cnt):
  global max_Value, min_Value
  s = str(n)
  cnt += count_odd(s)

  if len(s) == 1:
    min_Value = min(min_Value, cnt)
    max_Value = max(max_Value, cnt)
    return
  elif len(s) == 2:
    dividied(n // 10 + n % 10, cnt)
  else:
    for i in range(1, len(s) - 1):
      for j in range(i + 1, len(s)):
        new_num = int(s[:i]) + int(s[i: j]) + int(s[j:])
        dividied(new_num, cnt)

if __name__ == "__main__":
  n = int(input())
  min_Value = float('inf')
  max_Value = 0

  dividied(n, 0)

  print(min_Value, max_Value)
```

# 별 찍기 - 18
```python
import sys
input = sys.stdin.readline

def make_Star(x, y, n):
  if n == 1:
    board[y][x] = '*'
    return
    
  new_x = pow(2, n+1) - 3
  new_y = pow(2, n) - 1
    
  if n % 2:
    for i in range(new_x):
      board[y][x+i] = '*'    
    for i in range(new_y):
      board[y-i][x+i] = '*'
      board[y-i][x+new_x-i-1] = '*'
            
    make_Star(x+(pow(2, n-1)), y-(pow(2,n-1)-1), n-1)        
  else:
    for i in range(new_x):
      board[y][x+i] = '*'
    for i in range(new_y):
      board[y+i][x+i] = '*'
      board[y+i][x+new_x-i-1]= '*'

    make_Star(x+(pow(2, n-1)), y+(pow(2,n-1)-1), n-1)   
        
if __name__ == "__main__":
  N = int(input())
  x = pow(2, N+1) - 3
  y = pow(2, N) - 1
  board = [[' ' for _ in range(x)] for _ in range(y)]
    
  if N % 2:
    make_Star(0, y-1, N)
  else:
    make_Star(0, 0, N)
        
  for s in board:
    print(''.join(s).rstrip())
```
