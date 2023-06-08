# Dinamic Programming (동적 계획법)

최적화 이론의 한 기술이며, 특정 범위까지의 값을 구하기 위해서 다른 범위까지의 값을 이용하여 값을 구하는 알고리즘

`DP = 분할 정복 + 메모이제이션(재귀) or 타뷸레이션(for문)`

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

# 2. 신나는 함수 실행
`Silver 2` `9184`
```python
import sys
input = sys.stdin.readline

def w(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	elif a > 20 or b > 20 or c > 20:
		return w(20, 20, 20)

	if dp[a][b][c]:
		return dp[a][b][c]

	if a < b < c:
		dp[a][b][c] = w(a-1, b, c) + w(a, b-1, c-1) - w(a, b-1, c)
	else:
		dp[a][b][c] = w

if __name__ == "__main__":
	while True:
		a, b, c = map(int, input().rstrip().split())

		if a == b == c == -1:
			break
		else:
			w(a, b, c)
```

# 3. 01 타일
`Silver 3` `1904`
```python

```

# 4. 파도반 수열
`Silver 3` `9461`
```python

```

# 5. 연속합
`Silver 2` `1912`
```python

```

# 6. RGB 거리
`Silver 1` `1149`
```python

```

# 7. 정수 삼각1
`Silver 1` `1932`
```python

```

# 8. 계단 오르기
`Silver 3` `2579`
```python

```

# 9. 1로 만들기
`Silver 3` `1463`
```python

```

# 10. 쉬운 계단 수
`Silver 1` `10844`
```python

```

# 11. 포도주 시식
`Silver 1` `2156`
```python

```

# 12. 가장 긴 증가하는 부분 수열 
`Silver 2` `11053`
```python

```

# 13. 가장 긴 바이토닉 부분 수열
`Gold 4` `11054`
```python

```

# 14. 전깃줄 
`Gold 5` `2565`
```python

```

# 15. LCS
`Gold 5` `9251`
```python

```

# 16. 평범한 배낭
`Gold 5` `12865`
```python

```