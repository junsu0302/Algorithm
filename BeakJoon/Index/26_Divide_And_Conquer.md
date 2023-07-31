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

```

# 이항 계수 3
`11401` `Gold 1`
```python

```

# 행렬 곱셈
`2740` `Silver 5`
```python

```

# 행렬 제곱
`10830` `Gold 4`
```python

```

# 피보나치 수 6
`11444` `Gold 2`
```python

```

# 히스토그램에서 가장 큰 직사각형
`6549` `Platinum 5`
```python

```
