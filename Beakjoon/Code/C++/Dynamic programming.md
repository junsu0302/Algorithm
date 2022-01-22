# 동적 계획법

## 파일 합치기
```C++
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define MAX 1000000000

int T, K;
int sum[501], file[501], dp[501][501];

int main()
{
	cin >> T;

	while (T--)
	{
		cin >> K;
		for (int i = 1; i <= K; i++)
		{
			cin >> file[i];
			sum[i] = sum[i - 1] + file[i];
		}

		for (int i = 1; i <= K; i++)
		{
			for (int j = 1; j <= K - i; j++)
			{
				dp[j][i + j] = MAX;
				for (int k = j; k < i + j; k++)
					dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + sum[i + j] - sum[j - 1]);
			}
		}

		cout << dp[1][K] << "\n";
	}
}
```

## 행렬 곱셈 순서
```C++
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define MAX 1000000000

int N, r, c;
int sum[501], matrix[501][2], dp[501][501];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		cin >> r >> c;
		matrix[i][0] = r;
		matrix[i][1] = c;
	}
}

void run()
{
	for (int i = 1; i < N; i++)
	{
		for (int j = 1; i + j <= N; j++)
		{
			dp[j][i + j] = MAX;
			for (int k = j; k <= i + j; k++)
				dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + matrix[j][0] * matrix[k][1] * matrix[i+j][1]);
		}
	}
}

void print()
{
	cout << dp[1][N];
}

int main()
{
  setting();
  run();
  print();
}
```

## 내리막 길
```C++
#include <iostream>
using namespace std;

int M, N;
int arr[501][501]= {};
int dp[501][501] = {};
bool visited[501][501] = {0};
int arr_x[4] = { 0, 1, 0, -1 };
int arr_y[4] = { 1, 0, -1, 0 };

int Solve(int y, int x) 
{
	if (y == M  && x == N) 	return 1; 
	if (visited[y][x])	return dp[y][x];

	visited[y][x] = 1;
	for (int i = 0; i < 4; i++) 
  {
		int next_y = y + arr_y[i];
		int next_x = x + arr_x[i];

		if (next_y > 0 && next_y <= M && next_x > 0 && next_x <= N)
			if (arr[y][x] > arr[next_y][next_x]) 
				dp[y][x] += Solve(next_y, next_x); 
	}
	return dp[y][x];
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> M >> N;

	for (int i = 1; i <= M; i++)
		for (int j = 1; j <= N; j++)
			cin >> arr[i][j];
}

int main() 
{
  setting();
	cout << Solve(1, 1);
}
```

## 팰린드롬?
```C++
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N, M, S, E;
int arr[2001];
bool palindrom[2001][2001] = {0};

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);	
  
  cin >> N;
}

void run()
{
	for (int i = 1; i <= N; i++) 
		cin >> arr[i];

	for (int i = 1; i <= N - 1; i++)
		if (arr[i] == arr[i + 1])
			palindrom[i][i + 1] = true;

	for (int i = 1; i <= N; i++) 
		palindrom[i][i] = true;

	for (int i = N - 1; i >= 1; i--) 
		for (int j = i + 2; j <= N; j++) 
			if (arr[i] == arr[j] && palindrom[i + 1][j - 1] == true) 
				palindrom[i][j] = true;  
}

void print()
{
	cin >> M;

	for (int i = 0; i < M; i++) 
  {
		cin >> S >> E;
		cout << palindrom[S][E] << '\n';
	}
}

int main()
{
  setting();
  run();
	print();
}
```

## 양팔저울
```C++
#include<iostream>
#include<algorithm>
using namespace std;

int N, M, K, weight[31];
bool dp[31][15001];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> weight[i];  
}

void run(int i, int w)
{
	if (i > N || dp[i][w]) return;
	dp[i][w] = true;
	run(i + 1, w + weight[i]);
	run(i + 1, abs(w - weight[i]));
	run(i + 1, w);
}

void print()
{
 	cin >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> K;

		if(K > 15000) cout << "N ";
		else if (dp[N][K]) cout << "Y ";
		else cout << "N ";
	}	 
}

int main()
{
  setting();
	run(0, 0);
  print();
}
```

## 동전 1
```C++
#include <iostream>
#include <vector>
using namespace std;

int N, K;
vector<int> arr(100);
vector<int> dp(10000);

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N >> K;

	for (int i = 0; i < N; i++)
		cin >> arr[i];
}

void run()
{
	dp[0] = 1;
	for (int i = 0; i < N; i++)
		for (int j = arr[i]; j <= K; j++) 
			dp[j] +=dp[j - arr[i]];
}

void print()
{
  cout << dp[K];
}


int main() 
{
  setting();
  run();
  print();
}
```

## 앱
```C++
#include<iostream>
#include<algorithm>
using namespace std;

int N, M, ans, sum;
int bite[101], cost[101];
int dp[101][10001];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
	cin >> N >> M;

	for (int i = 1; i <= N; i++) 
    cin >> bite[i];
	for (int i = 1; i <= N; i++) 
	{
		cin >> cost[i];
		sum += cost[i];
	}
}

void run()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 0; j <= sum; j++)
		{
			if (j - cost[i] >= 0)
				dp[i][j] = max(dp[i][j], dp[i - 1][j - cost[i]] + bite[i]);
			
			dp[i][j] = max(dp[i][j], dp[i - 1][j]);
		}
	}
}

void print()
{
	for (int i = 0; i <= sum; i++)
	{
		if (dp[N][i] >= M)
		{
			cout << i;
			break;
		}	
	}
}

int main()
{
  setting();
  run();
  print();
}
```
