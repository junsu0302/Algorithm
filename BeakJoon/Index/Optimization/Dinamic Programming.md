다이나믹 프로그래밍에서 많이 사용되는 최적화 기법에 대해서 알아보자
https://koosaga.com/242
https://justicehui.github.io/hard-algorithm/2020/04/30/monge-array/
# Convex Hull Optimization
Recurrence : $DP[i][j] = Min_{k < j}(DP[i-1][k] + C[k][j])$ 
Condition : $C[i][j]$ is a Monge Array
