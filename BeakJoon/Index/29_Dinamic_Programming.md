# 동적 계획법
동적 계획법(Dinamic Programming)은 복잡한 문제를 하위 문제로 나누어 해결하는 알고리즘 디자인 패러다임이다. 동적 게획법은 이전에 계산한 결과를 저장하고 재사용함으로써 중복 계산을 피하며, 최적화된 해답을 찾아내는 데 사용된다.

동적 계획법은 다음과 같이 구현된다.
- 재귀적 정의 찾기
  큰 문제를 작은 하위 문제로 분할, 하위 문제 사이의 관계를 재귀적으로 정의
- 메모이제이션 (Memoization)
  계산한 결과를 배열 or 맵에 저장하고 재사용
- 바텀업(Bottom-Up)
  작은 하위 문제로부터 시작하여 큰 문제의 최적해를 계산, 이 때 재귀적인 호출이 아닌 반복문을 사용

동적 계획법은 다음과 같은 문제에서 사용된다.
1. 피보나치 수열
   재귀적인 중복 계산 방지
2. 그리디 문제
   각 칸에 도달하는 최단 경로 및 최대 가치에 활용
3. 최장 공통 부분 수열 (LCS)
   두 문자열 간의 최장 공통 부분 수열을 구할 때 활용
4. 0/1 배낭 문제
   주어진 무게 한도 내에서 최대 가치를 얻는 문제에 활용
5. 최단 경로 문제
   다익스트라 알고리즘, 플로이드-와샬 알고리즘 등에 활용

# 1. 파일 합치기
`Gold 3` `11066`
```python
import sys
input = sys.stdin.readline

def BottomUp(dpValue, dpIndex, sums):
  for distance in range(1, K):
    for start in range(K-distance):
      end = start + distance
      minCostValue = 50000000
      minCostIndex = start
      
      for mid in range(dpIndex[start][end-1], dpIndex[start+1][end]+1):
        """
        행렬 곱셈의 순서 최적화 (Matrix Chain Multiplication)
        여러 행렬을 순서대로 곱하여 최소의 곱셈 연산 횟수 반환
        """
        cost = dpValue[start][mid] + dpValue[mid+1][end] + sums[end+1] - sums[start]
        if cost < minCostValue:
          minCostValue = cost
          minCostIndex = mid
          
      dpValue[start][end] = minCostValue
      dpIndex[start][end] = minCostIndex
  return dpValue[0][K-1]
  
if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    K = int(input())
    chapterFile = list(map(int, input().rstrip().split()))

    sums = [0]
    for i in range(K):
      sums.append(sums[-1] + chapterFile[i])
    valueStorage = [[0 for _ in range(K+1)] for _ in range(K+1)]
    indexStorage = [[0 for _ in range(K+1)] for _ in range(K+1)]
    for i in range(K+1):
      indexStorage[i][i] = i

    result = BottomUp(valueStorage, indexStorage, sums)
    print(result)
```

# 2. 행렬 곱셈 순서
`Gold 3` `11049`
```python

```

# 3. 내리막 길
`Gold 3` `1520`
```python

```

# 4. 양팔저울
`Gold 3` `2629`
```python

```

# 5. 동전 1
`Gold 5` `2293`
```python

```

# 6. 앱
`Gold 3` `7579`
```python

```
