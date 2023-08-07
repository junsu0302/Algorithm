# 분할 정복 (Divide and Conquer)
분할 정복은 어떤 문제를 해결할 때, 주어진 문제를 더 작은 부분 문제로 나누고(Divide), 각각의 작은 문제를 해결한 뒤에 그 결과를 합쳐서(Conpuer) 원래 문제를 해결하는 알고리즘 기법이다.
주로 재귀적인 방법으로 구현되며, 다음과 같이 구현된다

1. 베이스 케이스 정의 : 문제가 더 이상 분할되지 않고, 쉽게 해결할 수 있는 경우를 정의
   *베이스 케이스를 재귀를 종료하는 조건으로 사용*
2. 주어진 문제를 더 작은 부분으로 나눔 : 원래 문제를 더 작은 크기의 부분 문제들로 분할
   *부분 문제들은 원래 문제와 동일한 형태*
3. 각각의 작은 부분 문제 해결 : 부분 문제들을 재귀적으로 해결
4. 부분 문제들의 해를 합쳐서 원래 문제의 해 산출 : 각각의 작은 부분 문제들의 해를 합쳐서 원래 문제의 해 산출

분할 정복은 대표적으로 이진 탐색, 합병 정렬, 퀵 정렬 등에서 사용하는 기법이다. 
분할 정복은 문제를 더 작은 단위로 나누어 해결하기 때문에 일부 문제에서는 효율적인 알고리즘이 가능하다. 하지만 어떤 문제에서는 중복되는 부분 문제가 많이 발생할 수 있어서 적절한 기법을 선택해야 한다.

# 색종이 만들기
`2630` `Silver 2`
```python
import sys
input = sys.stdin.readline

def Divied(n, x, y):
  global blue_Count, white_Count

  base = paper[y][x]

  for row in range(y, y+n):
    for col in range(x, x+n):
      if base != paper[row][col]:
        Divied(n//2, x, y)
        Divied(n//2, x, y+n//2)
        Divied(n//2, x+n//2, y)
        Divied(n//2, x+n//2, y+n//2)
        return

  if base == 0:
    white_Count += 1
  else:
    blue_Count += 1

if __name__ == '__main__':
  N = int(input())
  paper = [list(map(int, input().rstrip().split())) for _ in range(N)]
  blue_Count = 0
  white_Count = 0
  
  Divied(N, 0, 0)
  print(white_Count)
  print(blue_Count)
```

# 퀴드트리
`1992` `Silver 1`
```python
import sys
input = sys.stdin.readline

def Divied(n, col, row):
  global result
  referencePoint = video[row][col]

  for r in range(row, row+n):
    for c in range(col, col+n):
      if referencePoint != video[r][c]:
        result.append('(')
        Divied(n//2, col, row)
        Divied(n//2, col+n//2, row)
        Divied(n//2, col, row+n//2)
        Divied(n//2, col+n//2, row+n//2)
        result.append(')')
        return 
        
  if referencePoint == '0':
    result.append('0')
  elif referencePoint == '1':
    result.append('1')
  
if __name__ == "__main__":
  N = int(input())
  video = [list(input().rstrip()) for _ in range(N)]

  result = []
  Divied(N, 0, 0)
  print(''.join(result))
```

# 종이의 개수
`1780` `Silver 2`
```python
import sys
input = sys.stdin.readline

def Divied(n, col, row):
  global minusCount, zeroCount, plusCount
  referencePoint = paper[row][col]

  for r in range(row, row+n):
    for c in range(col, col+n):
      if referencePoint != paper[r][c]:
        Divied(n//3, col, row)
        Divied(n//3, col+n//3, row)
        Divied(n//3, col+n*2//3, row)
        Divied(n//3, col, row+n//3)
        Divied(n//3, col+n//3, row+n//3)
        Divied(n//3, col+n*2//3, row+n//3)
        Divied(n//3, col, row+n*2//3)
        Divied(n//3, col+n//3, row+n*2//3)
        Divied(n//3, col+n*2//3, row+n*2//3)
        return

  if referencePoint == 1:
    plusCount += 1
  elif referencePoint == 0:
    zeroCount += 1
  elif referencePoint == -1:
    minusCount += 1

if __name__ == "__main__":
  N = int(input())
  paper = [list(map(int, input().rstrip().split())) for _ in range(N)] 
  minusCount, zeroCount, plusCount = 0, 0, 0

  Divied(N, 0, 0)
  print(minusCount)
  print(zeroCount)
  print(plusCount)
```

# 곱셈
`1629` `Silver 1`
```python
import sys
input = sys.stdin.readline

"""
지수 법칙
A^m+n = A^m x A^n

나머지 분배 법칙
(AxB)%C = (A%C) *(B%C) % C
"""

A, B, C = map(int,sys.stdin.readline().split()) 

def Divied(A, B): 
  if B == 1: 
    return A % C 
  else: 
    tmp = Divied(A, B//2) 
    if B % 2 == 0: 
      return (tmp * tmp) % C 
    else: 
      return (tmp * tmp * A) % C 
      
print(Divied(A, B))
```

# 이항 계수 3
`11401` `Gold 1`
```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1000000007

# 팩토리얼 값 계산(나머지 연산 적용)
def factorial(N):
  tmp = 1
  for i in range(2, N+1):
    tmp = (tmp * i) % MOD
  return tmp

# 거듭제곱 계산(나머지 연산 적용)
def square(n, k):
  if k == 0:
    return 1
  elif k == 1:
    return n
    
  tmp = square(n, k//2)
  if k % 2:
    return tmp * tmp * n % MOD
  else:
    return tmp * tmp % MOD

top = factorial(N)
bot = factorial(N-K) * factorial(K) % MOD

# 페르마의 소정리 이용해서 조합 공식 곱셈 형태로 변형
print(top * square(bot, MOD-2) % MOD)
```

# 행렬 곱셈
`2740` `Silver 5`
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
matrix1 = [list(map(int, input().rstrip().split())) for _ in range(N)]
M, K = map(int, input().rstrip().split())
matrix2 = [list(map(int, input().rstrip().split())) for _ in range(M)]

result = [[0 for _ in range(K)] for _ in range(N)]
for r in range(N):
  for c in range(K):
    tmp = 0
    for i in range(M):
      tmp += matrix1[r][i] * matrix2[i][c]
    result[r][c] = tmp

for idx in result:
  print(*idx)
```

# 행렬 제곱
`10830` `Gold 4`
```python
import sys
input = sys.stdin.readline

def matrixMul(a, b):
  result = [[0 for _ in range(N)] for _ in range(N)]

  for i in range(N):
    for j in range(N):
      for k in range(N):
        result[i][j] += a[i][k] * b[k][j]

  for i in range(N):
    for j in range(N):
      result[i][j] %= 1000

  return result

if __name__ == "__main__":
  N, B = map(int, input().rstrip().split())
  matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
  # 2진법으로 변환하여 분할정복 실행
  B = bin(B)[2:]

  # 단위 행렬
  indentity_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

  # 2진법 자릿수만큼 제곱 & 제곱한 행렬끼리 곱해줌
  result = indentity_matrix[:]
  for i in range(len(B)):
    if B[-i-1] == '1':
      tmp = matrix[:]
      while i != 0:
        tmp = matrixMul(tmp, tmp)
        i -= 1
      result = matrixMul(result, tmp)

  for idx in result:
    print(*idx)
```

# 피보나치 수 6
`11444` `Gold 2`
```python
import sys
input = sys.stdin.readline
MOD = 1000000007

def fibonacci(n):
  if dp.get(n) != None:
    return dp[n]
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  elif n % 2 == 0:
    dp[n//2+1] = fibonacci(n//2+1) % MOD
    dp[n//2-1] = fibonacci(n//2-1) % MOD
    return dp[n//2+1] ** 2 - dp[n//2-1] ** 2
  else:
    dp[n//2+1] = fibonacci(n//2+1) % MOD
    dp[n//2] = fibonacci(n//2) % MOD
    return dp[n//2+1] ** 2 + dp[n//2] ** 2

if __name__ == "__main__":
  N = int(input())
  dp = dict()
  result = fibonacci(N) % MOD
  print(result)
```

# 히스토그램에서 가장 큰 직사각형
`6549` `Platinum 5`
```python
from collections import deque
import sys
input = sys.stdin.readline

"""
1. 스택이 비어있으면 스택에 현재 막대기를 추가한다.
2. 스택에 마지막으로 들어간 막대보다 짧은 막대를 만나면 스택에 들어있는 막대의 넓이를 계산한다.
3. 스택에 들어있는 막대를 꺼낼 때는, 현재 막대의 길이보다 큰 것까지만 꺼낸다.
4. 스택에 마지막으로 들어간 막대보다 긴 막대를 만나면 스택에 추가한다.
5. 위 단계를 반복한 후 스택에 남은 막대가 있는지 확인한다.
"""

while True:
  inputData = list(map(int, input().rstrip().split()))

  if inputData[0] == 0:
    break

  stack = deque()
  maxResult = 0

  for i, height in enumerate(inputData):
    if i == 0:
      continue

    # 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 작은 경우
    if stack and stack[-1][1] > height:
      while stack: # 스택에서 빼내며 최대 직사각형 넓이 계산
        stackI, stackHeight = stack.pop()
        widthStart = 1
        if stack:
          widthStart = stack[-1][0] + 1
        result = (i-widthStart) * stackHeight
        maxResult = max(result, maxResult) # 최댓값 갱신
        # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
        if not stack or stack[-1][1] <= height:
          break
    # 스택이 비어있거나 스택의 가장 왼쪽 막대기보다 현재 막대기의 높이가 크거나 같은 경우
    if not stack or stack[-1][1] <= height:
      stack.append((i, height)) # 스택에 현재 막대기를 추가

  # 반복이 종료되고, 스택에 남은 막대기가 있는 경우
  while stack:
    stackI, stackHeight = stack.pop()
    widthStart = 1
    if stack:
      widthStart = stack[-1][0] + 1
    result = (inputData[0]+1 - widthStart) * stackHeight
    maxResult = max(result, maxResult) # 최댓값 갱신
  # 최대 
  print(maxResult)
```
