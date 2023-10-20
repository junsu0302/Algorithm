# Dinamic Programming

https://zzonglove.tistory.com/13

https://cotak.tistory.com/51

Dinamic Programming은 다항한 시간안에 특정 문제를 풀기위한 기술이다. DP는 다음과 같은 단계를 거친다.
1. DP가 사용 가능한 문제인지 확인
2. 최소 매개변수를 이용해 어떻게 상태를 표현할지 결정
3. 상태 관계를 수식화
4. 도표 작성 (Memorization 추가)

https://koosaga.com/242

https://justicehui.github.io/hard-algorithm/2020/04/30/monge-array/

# Convex Hull Optimization
- Recurrence : $DP[i] = Min_{j < i}(DP[j] + B[j] * A[i])$ 
- Condition : None
- Naive Complexity : $O(n^2)$
- Optimized Complexity : $O(nlogn)$

컨벡스 헐 최적화는 동적 계획법 최적화 중에서 가장 간단한 형태이다

CHT는 다음과 같은 Lemma를 기반으로 위 동적 계획법을 최적화한다 :
- Lemma. \
  $A[i] \geq A[i+1], \ B[i] \leq B[i+1]$일 때, $C[i][j] = B[i] * A[j]$는 Monge Array다. \
- Proof. \
  $B[a]*A[c]+B[b]*A[d] \leq B[a]*A[d]+B[b]*A[c], \ (B[a]-B[b]) * (A[c]-A[d]) \leq 0$


# Divide and Conquer Optimization
- Recurrence : $DP[i][j] = Min_{k < j} (DP[i-1][k] + C[k][j])$
- Condition : $C[i][j]$ is a Monge Array
- Naive Complexity : $O(kn^2)$
- Optimized Complexity : $O(knlogn)$

여기서 Monge Array는 n*m 크기의 행렬 A가 아래 성질을 만족하는 행렬을 의미한다.

어떠한 2차원 배열이 Monge Array라는 것은, 임의의 $a \leq b \leq c \leq d$에 대해 $C[a,c]+C[b,d] \leq C[a,d]+C[b,c]$라는 것을 만족한다. 일반적으로 $C[i][j]$는 구간 $[i,j]$를 사용했을 때의 비용을 뜻한다. \
즉 이 식은 한 구간이 다른 구간을 포함하고 있으면, 그렇지 않도록 풀어주는 것이 이득이라는 것을 의미한다.

D&C Optimization은 다음과 같은 Lemma를 기반으로 위 동적 계획법을 최적화한다 : 
- Lemma.
  임의의 $c < d$에 대해, $opt_c$를 $DP[i-1][k] + C[k][c]$를 최소화하는 $k, opt_d$를 $DP[i-1][k] + C[k][d]$를 최소화하는 $k$라고 정의하자. \
  이 때 $opt_c \leq opt_d$를 만족한다.

- Proof. 반례를 고려하여 $opt_c > opt_d$를 통해 다음의 2개의 식을 유도해보자.
  - $DP[i-1][opt_c] + C[opt_c][c] < DP[i-1][opt_d] + C[opt_d][c]$
  - $DP[i-1][opt_d] + C[opt_d][d] < DP[i-1][opt_c] + C[opt_c][d]$
  
  두 식을 더하면 다음 식이 유도된다.
  - $C[opt_c][c] + C[opt_d][d] < C[opt_d][c] + C[opt_c][d]$

  즉 $b=opt_c, a=opt_d$로 설정하면 Monge Array의 정의에 모순된다.

어떠한 Monge Array C에 대해서 $C'[i][j] = C[i][j] + DP[x-1][i-1]$이라고 정의하자. 위 부등식에 대입하면 $C'$역시 Monge Array임을 알 수 있다. 

어떠한 Monge Array에 대해서, 각 $i$에 대한 $min_jC[i][j]$를 빠르게 구하는 알고리즘을 생각해보자. 이를 위해서 Divied and Conquer Optimization을 사용하면 $O(nlongn)$에 진행할 수 있다.

여기서 SMAWK 알고리즘을 사용하면 더 빠른 $O(n)$에 진행할 수 있다. 

http://web.cs.unlv.edu/larmore/Courses/CSC477/monge.pdf


# Monotone Queue Optimizatoin
- Recurrence : $DP[i] = Min_{j < i} (DP[j] + C[j][i])$
- Condition : $C[i][j]$ is Monge Array
- Naive Complexity : $O(n^2)$
- Optimized Complexity : $O(nlogn)$

Monotone Queue Optimization은 Convex Hull Optimization과 Divide and Conquer Optimization을 모두 일반화한다.

Monotone Queue Optimizatoin에 대해 논의하기 전에 Convex Hull Optimization이 최적화되는 상황에 다음 Lemma를 대입해보자. \
- Lemma. 어떠한 $i < j < k$ 에 대해서 \
  $DP[i] + C[i][k+1] \leq DP[j] + C[j][k+1]$이면 $DP[i] + C[i][k] \leq DP[j] + C[j][k]$을 만족하고, \
  $DP[i] + C[i][k] \geq DP[j] + C[j][k]$이면 $DP[i] + C[i][k+1] \geq DP[j] + C[j][k+1]$을 만족한다.
- Proof.
  - $DP[i] - DP[j] \leq C[j][k+1] - C[i][k+1] \leq C[j][k] - C[i][k]$ 이기에 성립
  - $DP[j] - DP[i] \leq C[i][k] - C[j][k] \leq C[i][k+1] - C[j][k+1]$ 이기에 성립

즉 임의의 $i < j$에 대해서 어떠한 지점 $cross(i,j)$를 가정하면 다음과 같은 결과가 나온다.
- $cross(i,j) \leq k$이면 $DP[j] + C[j][k]$가 더 작은 값을 준다.
- $cross(i,j) > k$이면 $DP[i] + C[i][k]$가 더 작은 값을 준다.

여기서 $cross(i,j)$는 이분 탐색을 사용하여 $O(logn)$으로 찾을 수 있다.

# Knuth Optimization
- Recurrence : $$
- Condition : $$
- Naive Complexity : $$
- Optimized Complexity : $$

# Lagrange Optimization (Aliens Trick)
- Recurrence : $$
- Condition : $$
- Naive Complexity : $$
- Optimized Complexity : $$

# Hirschburg Algorithm
- Recurrence : $$
- Condition : $$
- Naive Complexity : $$
- Optimized Complexity : $$

# Circular LCS
- Recurrence : $$
- Condition : $$
- Naive Complexity : $$
- Optimized Complexity : $$

# Dynamic Tree DP
- Recurrence : $$
- Condition : $$
- Naive Complexity : $$
- Optimized Complexity : $$







