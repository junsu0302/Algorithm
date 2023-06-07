# 1. N과 M 1
```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
stack = deque()

def DFS():
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(1, N+1):
		if i not in stack:
			stack.append(i)
			DFS()
			stack.pop()

DFS()
```

# 2. N과 M 2
```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
stack = deque()

def DFS(start):
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(start, N+1):
		if i not in stack:
			stack.append(i)
			DFS(i+1)
			stack.pop()

DFS(1)
```

# 3. N과 M 3

```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
stack = deque()

def DFS(start):
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(start, N+1):
		if i not in stack:
			stack.append(i)
			DFS(i+1)
			stack.pop()

DFS(1)
```

# 4. N과 M 4

```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
stack = deque()

def DFS(start):
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(start, N+1):
		if i not in stack:
			stack.append(i)
			DFS(i+1)
			stack.pop()

DFS(1)
```

# 5. N-Queen

```python
import sys
input = sys.stdin.readline

def put_Queen(n):
	global count
	if n == N:
		count += 1
		return

	for i in range(N):
		if not col[i] and not diagonal_right[n+i] and not diagonal_left[n-i+N-1]:
			col[i] = True
			diagonal_right[n + i] = True
			diagonal_left[n - i + N - 1] = True
			put_Queen(n + 1)
			col[i] = False
			diagonal_right[n + i] = False
			diagonal_left[n - i + N - 1] = False

N = int(input().rstrip())
count = 0
col = [False for _ in range(N)]
diagonal_right = [False for _ in range(2 * N - 1)]
diagonal_left = [False for _ in range(2 * N - 1)]

put_Queen(0)
print(count)
```

# 6. 스도쿠

```python

```














