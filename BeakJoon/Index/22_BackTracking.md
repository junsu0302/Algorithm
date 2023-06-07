# 1. N과 M 1
`Silver 3` `15649`
```python
import sys
from collections import deque
input = sys.stdin.readline

def DFS():
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(1, N+1):
		if i not in stack:
			stack.append(i)
			DFS()
			stack.pop()

if __name__ == '__main__':
	N, M = map(int, input().rstrip().split())
	stack = deque()

	DFS()
```

# 2. N과 M 2
`Silver 3` `15650`
```python
import sys
from collections import deque
input = sys.stdin.readline

def DFS(start):
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(start, N+1):
		if i not in stack:
			stack.append(i)
			DFS(i+1)
			stack.pop()

if __name__ == '__main__':
	N, M = map(int, input().rstrip().split())
	stack = deque()

	DFS(1)
```

# 3. N과 M 3
`Silver 3` `15651`
```python
import sys
from collections import deque
input = sys.stdin.readline

def DFS(start):
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(start, N+1):
		if i not in stack:
			stack.append(i)
			DFS(i+1)
			stack.pop()

if __name__ == '__main__':
	N, M = map(int, input().rstrip().split())
	stack = deque()

	DFS(1)
```

# 4. N과 M 4
`Silver 3` `15652`
```python
import sys
from collections import deque
input = sys.stdin.readline

def DFS(start):
	if len(stack) == M:
		print(" ".join(map(str, stack)))
		return

	for i in range(start, N+1):
		if i not in stack:
			stack.append(i)
			DFS(i+1)
			stack.pop()

if __name__ == '__main__':
	N, M = map(int, input().rstrip().split())
	stack = deque()

	DFS(1)
```

# 5. N-Queen
`Gold 4` `9663`
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
`Gold 4` `2580`
```python
import sys
input = sys.stdin.readline


def dfs(cnt):
	if cnt == 81:
		for i in range(9):
			print(*board[i])
		quit()

	x = cnt // 9
	y = cnt % 9

	if board[x][y] == 0:
		for i in range(1, 10):
			if not col[x][i] and not row[y][i] and not rect[(x // 3) * 3 + (y // 3)][i]:
				col[x][i] = 1
				row[y][i] = 1
				rect[(x // 3) * 3 + (y // 3)][i] = 1
				board[x][y] = i

				dfs(cnt + 1)

				col[x][i] = 0
				row[y][i] = 0
				rect[(x // 3) * 3 + (y // 3)][i] = 0
				board[x][y] = 0
			else:
				dfs(cnt + 1)


if __name__ == '__main__':
	board = [[0 for _ in range(9)] for _ in range(9)]
	col = [[0 for _ in range(10)] for _ in range(9)]
	row = [[0 for _ in range(10)] for _ in range(9)]
	rect = [[0 for _ in range(10)] for _ in range(9)]

	for i in range(9):
		number = input().strip().split()
		for j in range(len(number)):
			board[i][j] = int(number[j])
				if board[i][j] != 0:
					col[i][board[i][j]] = 1
					row[j][board[i][j]] = 1
					rect[(i // 3) * 3 + (j // 3)][board[i][j]] = 1

	dfs(0)
```

# 7. 연산자 끼워넣기
`Silver 1` `14888`
```python
import sys
input = sys.stdin.readline

def DFS(depth, total, plus, minus, multiply, divide):
	global maximum, minimum

	if depth == N:
		maximum = max(total, maximum)
		minimum = min(total, minimum)
		return

	if plus:
		DFS(depth+1, total+numbers[depth], plus-1, minus, multiply, divide)
	if minus:
		DFS(depth+1, total-numbers[depth], plus, minus-1, multiply, divide)
	if multiply:
		DFS(depth+1, total*numbers[depth], plus, minus, multiply-1, divide)
	if divide:
		DFS(depth+1, int(total/numbers[depth]), plus, minus, multiply, divide-1)

if __name__ == '__main__':
	N = int(input())
	numbers = list(map(int, input().rstrip().split()))
	operators = list(map(int, input().rstrip().split()))

	maximum = -1e9
	minimum = 1e9

	DFS(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
	print(maximum)
	print(minimum)
```

# 8. 스타트와 링크
`Silver 2` `14889`
```python
import sys
input = sys.stdin.readline

def DFS(depth, cnt):
	global result

	if depth == N//2:
		start = 0
		link = 0

		for i in range(N):
			for j in range(N):
				if members[i] and members[j]:
					start += people[i][j]
				elif not members[i] and not members[j]:
					link += people[i][j]

		result = min(result, abs(start - link))
		return

	for i in range(cnt, N):
		if not members[i]:
			members[i] = True
			DFS(i+1, depth+1)
			members[i] = False

if __name__ == '__main__':
	N = int(input())
	people = [list(map(int, input().rstrip().split())) for _ in range(N)]
	members = [False for _ in range(N)]
	result = 1e9	

	DFS(0,0)
	print(result)
```










