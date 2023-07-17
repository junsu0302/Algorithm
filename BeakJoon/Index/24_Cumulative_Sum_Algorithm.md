# Cumulative Sum Algorithm

누적합 알고리즘(Cumulative Sum Algorithm)은 주어진 배열 또는 리스트의 각 요소까지의 누적 합을 빠르게 계산하는 알고리즘입니다. 이 알고리즘을 사용하면 배열의 일부 구간의 합을 빠르게 계산할 수 있으며, 쿼리(Query) 작업 등에서 유용하게 활용될 수 있습니다.

누적합 알고리즘은 다음과 같은 방식으로 동작합니다:

1. 주어진 배열의 첫 번째 요소부터 마지막 요소까지 반복하면서 각 요소까지의 누적 합을 계산합니다.
2. 누적 합을 저장하기 위한 배열 또는 리스트를 생성하고, 첫 번째 요소는 주어진 배열의 첫 번째 요소와 동일합니다.
3. 두 번째 요소부터 마지막 요소까지 반복하면서 이전 요소의 누적 합에 현재 요소를 더하여 새로운 누적 합을 계산합니다. 이 값을 누적합 배열에 저장합니다.
4. 모든 요소에 대한 누적 합을 계산한 후, 누적합 배열을 반환합니다.

누적합 알고리즘은 한 번의 전처리 과정으로 누적 합을 계산하므로, 이후에 쿼리(Query) 작업을 수행할 때 시간 복잡도가 O(1)으로 매우 빠릅니다. 예를 들어, 주어진 배열의 특정 구간의 합을 구하려면 해당 구간의 마지막 요소의 누적 합에서 시작 요소의 누적 합을 빼주면 됩니다.

누적합 알고리즘은 다양한 문제에서 활용될 수 있습니다. 예를 들어, 구간 합 문제, 평균 계산, 누적 빈도수 계산 등 다양한 쿼리 작업에 활용될 수 있습니다. 또한, 누적합을 활용하여 주어진 배열에서 특정 값보다 작은(또는 큰) 요소의 개수를 빠르게 계산하는 것도 가능합니다.

누적합 알고리즘은 배열의 크기에 비례하여 추가적인 공간을 필요로 하므로, 공간 복잡도는 O(N)입니다. 그러나 쿼리 작업의 시간 복잡도는 O(1)이기 때문에 많은 쿼리 작업이 필요한 경우에 유리하게 사용될 수 있습니다.

# 구간 합 구하기 4
`Silber 3` `11659`
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

sum = 0
prefix_sum = [0]
for idx in numbers:
  sum += idx
  prefix_sum.append(sum)

for _ in range(M):
  i, j = map(int, input().rstrip().split())
  result = prefix_sum[j] - prefix_sum[i-1]
  print(result)
```

# 수열
`Silver 3` `2559`
```python
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
temperatures = list(map(int, input().split()))

result = []
result.append(sum(temperatures[:K]))

for i in range(N-K):
    result.append(result[i] - temperatures[i] + temperatures[K+i])
        
print(max(result))
```

# 인간-컴퓨터 상호작용
`Silver 1` `16139`
```python

```

# 나머지 합
`Gold 3` `10986`
```python

```

# 구간 합 구하기 5
`Silver 1` `11660`
```python

```

# 체스판 다시 칠하기 2
`Gold 5` `25682`
```python

```
