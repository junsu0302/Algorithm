# 그리디 알고리즘 (Greedy Algorithm)

그리디 알고리즘은 최적해를 구해 각 단계에서 가장 좋아 보이는 선택을 하는 알고리즘이다.
이러한 선택은 지역적 최적해를 통해 전체적 최적해를 산출하려고 하기 때문에 해당 단계에서는 가장 이상적인 것으로 보일 수 있지만, 항상 전체적인 최적해를 보장하지는 않는다. 하지만 빠르고 간결한 해결책을 제시할 수 있다.

그리디 알고리즘은 다음과 같이 구현된다.
1. 그리디적인 방법으로 해결 가능한지 확인
2. 문제를 하나의 기준(비용, 거리, 가치 등)에 따라 정렬
3. 정렬된 순서대로 각 단계에서 최적의 선택 수행
4. 최종적으로 구한 선택들이 문제의 조건을 만족하는 최적해인지 확인

그리디 알고리즘이 최적해를 보장하지 않는 경우는 다른 알고리즘을 고려해 문제를 해결해야한다.

# 동전 0
`11047` `Sliver 4`
```python
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coins = [0]*N
for i in range(N):
  coins[i] = int(input())

count = 0
for idx in reversed(coins):
  if K == 0:
    break
  count += K // idx
  K = K % idx

print(count)
```

# 회의실 배정
`1931` `Sliver 1`
```python
import sys
input = sys.stdin.readline

N = int(input())

meeting = [None] * N
for i in range(N):
    start, end = map(int, input().rstrip().split())
    meeting[i] = [start, end]

meeting.sort(key=lambda x: (x[1], x[0]))  # 종료 시간을 기준으로 정렬

last_Time = 0
count = 0
for start, end in meeting:
    if start >= last_Time:
        count += 1
        last_Time = end

print(count)
```

# ATM
`11399` `Sliver 4`
```python
import sys
input = sys.stdin.readline

N = int(input())
waiting_Time = list(map(int, input().rstrip().split()))
waiting_Time.sort()

result = 0
for i in range(N):
  result += waiting_Time[i] * (N-i)

print(result)
```

# 잃어버린 괄호
`1541` `Sliver 2`
```python
import sys
input = sys.stdin.readline

input_Data = input().rstrip().split('-')

numbers = [] 

for idx in input_Data:
  sum = 0
  tmp = idx.split('+')
  for index in tmp:
    sum += int(index)
  numbers.append(sum)

result = numbers[0] 

for i in range(1,len(numbers)):
  result -= numbers[i]
print(result)
```

# 주유소
`13305` `Sliver 3`
```python
import sys
input = sys.stdin.readline

N = int(input())
load = list(map(int, input().rstrip().split()))
city = list(map(int, input().rstrip().split()))

result = 0
min_cost = 1000000001
for i in range(N-1):
  if min_cost > city[i]:
    min_cost = city[i]
    result += city[i] * load[i]
  else:
    result += min_cost * load[i]

print(result)
```
