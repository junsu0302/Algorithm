# 1. 팩토리얼 2
`Bronze 5` `27433`
```python
import sys
import math
input = sys.stdin.readline

N = int(input())

print(math.factorial(N))
```

# 2. 피보나치 수 5
`Bronze 2` `10870`
```python
import sys
input = sys.stdin.readline

n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
	fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci[n])
```

# 3. 재귀의 귀재
`Bronze 2` `25501`
```python
import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global cnt
    cnt += 1
    
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for _ in range(T):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)
```

# 4, 알고리즘 수업 - 병합 정렬 1
`Silver 4` `24060`
```python
def merge_sort(A, p, r):
	if(p < r and cnt<= K):
		q = (p + r) // 2;
		merge_sort(A, p , q)
		merge_sort(A, q + 1, r)
		merge(A, p, q, r)
        
def merge(A, p, q, r):
	global cnt, result
	i, j = p, q + 1
	tmp = []

	while i <= q and j <= r:
		if(A[i] <= A[j]):
			tmp.append(A[i])
			i += 1
		else:
			tmp.append(A[j])
			j += 1

	while i <= q:
		tmp.append(A[i])
		i += 1
	
	while j <= r:
		tmp.append(A[j])
		j += 1
    
	i, t = p, 0;
	
	while i <= r:
		A[i] = tmp[t]
		cnt+= 1
		if cnt== K:
			result = A[i]
			break
		i += 1
		t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)
```

# 5. 칸토어 집합
`Silver 3` `4779`
```python
"""
함수
"""
import sys

def cantor(n):
    if n == 0:
        return "-"
    result = cantor(n-1)
    space = " " * 3 ** (n-1)
    result = result + space + result

    return result

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        result = cantor(n)
        print(result)

"""
for 문
"""
import sys

for line in sys.stdin:
  result = "-"
  for i in range(int(line)):
    result = result + " " * len(result) + result

  print(result)

```

# 6. 별 찍기 - 10
`2447`
```python
"""
수학적 재귀
"""

import sys
input = sys.stdin.readline

def star(n):
	if n == 1:
		return ["*"]

	stars = star(n//3)
	result = []

	for i in stars:
		result.append(i*3)
	for i in stars:
		result.append(i + ' '*(n//3) + i)
	for i in stars:
		result.append(i*3)

	return result

N = int(input())
result = star(N)
print("\n".join(result))

"""
구조적 재귀
"""
def star(n):
    if n == 1:
        return pattern
    else:
        tmp = star(n-1)
        return [i*3 for i in tmp] + [i + " "*(3**(n-1)) + i for i in tmp] + [i*3 for i in tmp]


pattern = [
    "***",
    "* *",
    "***"
]

N = int(input())
k = 0
while N > 1:
    N = N//3
    k += 1
```

# 7. 하노이 탑 이동 순서
``
```python
import sys
input = sys.stdin.readline

def hanoi(n, start, middle, end):
	if n == 1:
		print(start, end)
	else:
		hanoi(n-1, start, end, middle)
		print(start, end)
		hanoi(n-1, middle, start, end)

N = int(input())
print(2**N - 1)
hanoi(N, 1, 2, 3)
```
