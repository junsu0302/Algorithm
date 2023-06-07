# Dinamic Programming (동적 계획법)

최적화 이론의 한 기술이며, 특정 범위까지의 값을 구하기 위해서 다른 범위까지의 값을 이용하여 값을 구하는 알고리즘

`DP = 분할 정복 + 메모이제이션 or 타뷸레이션`

# 1.알고리즘 수업 - 피보나치 수 1
`Bronze 1` `24416`
```python
import sys
input = sys.stdin.readline

def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fibonacci(n):
	dp = [0 for _ in range(n+1)]
	dp[1], dp[2] = 1, 1
	cnt = 0

	for i in range(3, n+1):
		cnt += 1
		dp[i] = dp[i-1] + dp[i-2]
	return cnt

if __name__ == "__main__":
	n = int(input())
	print(fib(n), fibonacci(n))
```