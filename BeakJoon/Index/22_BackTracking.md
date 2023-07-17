# 백트래킹 (BackTracking)
백트래킹(Backtracking)은 탐색 알고리즘의 일종으로, 해를 찾아가는 도중에 불필요한 경로를 배제하여 실행 시간을 단축시키는 기법입니다. 주어진 문제의 조건에 따라 해를 찾기 위해 후보군을 탐색하다가, 해당 후보군이 조건을 만족하지 않으면 이전 단계로 돌아와 다른 후보군을 탐색하는 방식을 반복합니다. 이를 통해 해를 찾는 동안 가능한한 적은 수의 후보군을 탐색하며 효율적으로 문제를 해결할 수 있습니다.

백트래킹은 보통 재귀적인 방식으로 구현되며, 일반적으로 다음과 같은 과정으로 이루어집니다

1. 후보군 탐색: 주어진 문제에 대한 가능한 모든 후보군을 생성합니다.
2. 제약 조건 확인: 생성된 후보군이 주어진 조건을 만족하는지 확인합니다.
3. 조건 만족 여부에 따른 분기: 조건을 만족하지 않으면 해당 후보군을 배제하고 다른 후보군을 탐색합니다.
4. 해 검증: 조건을 만족하는 해인지 확인합니다. 필요한 경우 해를 저장하거나 출력합니다.
5. 재귀적 호출: 조건을 만족하는 후보군에 대해 재귀적으로 다음 단계를 진행합니다.
6. 후보군 제거: 해당 후보군을 제거하고 이전 단계로 돌아갑니다.

백트래킹은 조합 최적화, 순열 생성, 제약 충족 문제 등 다양한 문제에 활용될 수 있습니다. 일반적으로 경우의 수가 많거나 가능한 해의 수가 제한적인 경우에 유용하게 사용됩니다. 그러나 모든 문제에 적용할 수 있는 것은 아니며, 최악의 경우 모든 경우의 수를 탐색해야 할 수도 있습니다.

백트래킹 알고리즘은 문제에 맞게 구현해야 하며, 재귀 호출, 상태 관리, 가지치기 등을 적절히 활용하여 효율적으로 문제를 해결할 수 있도록 해야 합니다.

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
