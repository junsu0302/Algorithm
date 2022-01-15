# 동적 계획법 1

## 피보나치 함수
```C++
// 시간복잡도를 줄이기 위해 점화식 사용

#include <iostream> 
using namespace std; 

int main() 
{ 
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int zero[41]={1,0,}; 
  int one[41]={0,1,}; 
  int T,n; 
  cin >> T;

  for (int i=0; i<T; i++) 
  { 
    cin >> n; 
    for(int j = 2 ; j<=n; j++) 
    { 
      zero[j] = zero[j-1] +zero[j-2]; 
      one[j] = one[j-1] + one[j-2]; 
    } 
    cout << zero[n] << " " << one[n] << "\n";
  } 
}
```

## 신나는 함수 실
```C++
#include <iostream> 
using namespace std; 

int arr[20][20][20]; 

int w(int a, int b, int c) 
{ 
  if (a <= 0 || b <= 0 || c <= 0) return 1; 
  else if (a > 20 || b > 20 || c > 20) return w(20, 20, 20); 
  else if (arr[a][b][c] != 0) return arr[a][b][c]; // 메모이제이션
  else if (a < b && b < c) arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
  else arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1); 
  
  return arr[a][b][c];
} 

int main() 
{ 
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int a, b, c; 
  while(1)
  { 
    cin >> a >> b >> c; 
    if(a == -1 && b == -1 && c == -1) break; 
    
    cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << "\n"; 
  } 
}
```

## 01타일
```C++
#include <iostream> 
using namespace std;

int N;

int main() 
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N;
  int arr[N];

	arr[1] = 1;
	arr[2] = 2;
	for (int i = 3; i <= N; i++) 
	{
		arr[i] = (arr[i-2] + arr[i-1])%15746;
	}

	cout << arr[N] << "\n";
}
```

## 파도반 수열
```C++
#include <iostream>
using namespace std;
long long arr[101] = {0,1,1,};

long long P(int N)
{
    if(N < 3)  return arr[N];
    else if(arr[N] == 0)  arr[N] = P(N-2) + P(N-3);
    return arr[N];
}

int main() 
{
  int T;
  int N;
  cin >> T;
  for(int i = 0; i < T; i++)
  {
    cin >> N;
    cout << P(N) << '\n';
  }
}
```

## RGB 거리
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int house[1001][3];

int main() 
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  int N;
  int cost[3];
  house[0][0] = 0;
  house[0][1] = 0;
  house[0][2] = 0;
  cin >> N;

  for(int i = 1; i <= N; ++i)
  {
    cin >> cost[0] >> cost[1] >> cost[2];
    house[i][0] = min(house[i-1][1], house[i-1][2]) + cost[0];
    house[i][1] = min(house[i-1][0], house[i-1][2]) + cost[1];
    house[i][2] = min(house[i-1][1], house[i-1][0]) + cost[2];
  }
  cout << min(house[N][2],min(house[N][0],house[N][1]));
}
```

## 정수 삼각형
```C++
#include <algorithm>
#include <iostream>
using namespace std;

int arr[501];
int ans[501];
int N, num;

int main()
{
  cin >> N;
  for (int i=1; i<=N; i++)
  {
    if (i == 1)
    {
      cin >> ans[1];
      arr[1] = ans[1];
      continue;
    }
    else
    {
      for (int j=1; j<=i; j++)
      {
        cin >> num;

        if (j == 1)  arr[j] = num + ans[1];
        else if (j == i)  arr[j] = num + ans[j-1];
        else  arr[j] = num + max(ans[j-1], ans[j]);
      }

      for(int k=1; k<=i; k++)
        ans[k] = arr[k];
    }
  }

  sort(ans+1, ans+1+N, greater<int>());

  cout << ans[1];
}
```

## 계단 오르기
```C++
#include <iostream> 
using namespace std; 

int N; 
int stairs[301]; 
int result[301]; 

int main() 
{ 
  cin >> N; 
  for(int i=0; i<N; i++) 
    cin >> stairs[i]; 
    
  result[0] = stairs[0]; 
  result[1] = max(stairs[1], stairs[0]+stairs[1]); 
  result[2] = max(stairs[0] + stairs[2], stairs[1]+stairs[2]); 
  
  for(int i=3; i<N; i++) 
    result[i] = max(stairs[i] + result[i-2], stairs[i]+stairs[i-1]+result[i-3]); 
    
  cout << result[N-1]; 
}
```

## 1로 만들기
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	int N;
	cin >> N ;
	vector<int> arr(N+1);

	arr[1] = 0;
	for (int i=2; i<=N; i++) 
  {
		arr[i] = arr[i - 1] + 1;
		if (!(i % 3)) arr[i] = min(arr[i], arr[i/3] + 1);
		if (!(i % 2)) arr[i] = min(arr[i], arr[i/2] + 1);
	}
	cout << arr[N] << "\n";
}
```

## 쉬운 계단 수
```C++
#include <iostream>
#include <vector>
using namespace std;

int n, result = 0;
int arr[101][10] = {0};
int main()
{
  cin >> n;

  for (int i=1; i<10; i++)
    arr[1][i] = 1;

  for (int i=2; i<=n; i++) 
  {
    for (int j=0; j<10; j++) 
    {
      if (j == 0)  arr[i][0] = arr[i-1][j+1];
      else if (j == 9)  arr[i][9] = arr[i-1][j-1];
      else  arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1];

      arr[i][j] %= 1000000000;
    }
  }

  for (int i = 0; i < 10; i++) 
    result = (result + arr[n][i]) % 1000000000;

    cout << result << "\n";
}
```

## 포도주 시식
```C++
#include<iostream>
using namespace std;

int podo[10001];
int result[10001]; 

int main() 
{
	int n;
	cin >> n; 
	for (int i=1; i<=n; i++) 
		cin >> podo[i]; 

	result[1] = podo[1];
	result[2] = podo[1] + podo[2];
	for (int i = 3; i <= n; i++) 
  {
		result[i] = result[i-1];
		if (result[i] < result[i-2] + podo[i])
			result[i] = result[i-2] + podo[i];
		if (result[i] < result[i-3] + podo[i-1] + podo[i])
			result[i] = result[i-3] + podo[i-1] + podo[i];
	}
	cout << result[n] << '\n';
}
```

## 가장 긴 증가하는 부분 수열
```C++
#include <iostream>
#include <algorithm> 
using namespace std;

int main()
{
	int n;
	int dp[1000] = {};
	int arr[1000] = {};
	int sum = 0;

	cin >> n;

	for (int i=0; i<n; i++)
		cin >> arr[i];

	for (int i=0; i<n; i++)
	{
		dp[i] = 1;

		for (int j = 0; j < i; j++)
			if (arr[i] > arr[j])
				dp[i] = max(dp[i], dp[j] + 1);
		
    sum = max(sum, dp[i]);
	}
	cout << sum << endl;
}
```

## 가장 긴 바이토닉 부분 수열
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int N;
int result = 1;
int arr[1001];
int upcount[1001];
int downcount[1001];

int main()
{
  cin >> N;
  for (int i=1; i<=N; i++) 
    cin >> arr[i];

  for (int i=1; i<=N; i++) 
  {
    upcount[i] = 1;
    for (int j=0; j<i; j++) 
    {
      if (arr[i] > arr[j] && upcount[i] < upcount[j]+1)
        upcount[i] = upcount[j] + 1;
    }
  }

  for (int i = N; i >= 1; i--) 
  {
    downcount[i] = 1;
    for (int j=N; j>i; j--) 
    {
      if (arr[i] > arr[j] && downcount[i] < downcount[j]+1)
        downcount[i] = downcount[j] + 1;
    }
  }

  for (int i = 1; i <= N; i++) 
    result= max(result, upcount[i] + downcount[i]-1);

  cout << result;
}
```

## 전깃줄
```C++
#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

int dp[1010];
int arr[101];

int main() 
{
	pair<int, int>pole[101];
	int n; 
  cin >> n;

	for(int i=0; i<n; i++)
		cin >> pole[i].first >> pole[i].second;
  
	sort(pole, pole + n);
	int result = -1;

	for (int i = 0; i < n; i++) 
  {
		dp[i] = 1;
		for (int j = 0; j < i; j++)
			if (pole[j].second < pole[i].second)
				dp[i] = max(dp[i], dp[j] + 1);
		
    result = max(result, dp[i]);
	}
	cout << n - result;
}
```

## LCS
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int dp[1001][1001];

int main() 
{
	string a, b;
  cin >> a >> b;
	
  for(int i=1; i<=b.size(); i++)
  {
    for(int j=1; j<=a.size(); j++) 
    {
      if (b[i-1] == a[j-1])
        dp[i][j] = dp[i-1][j-1] + 1;
      else
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
    }
  }
	cout << dp[b.size()][a.size()]<<'\n';
}
```

## 연속합
```C++
#include<iostream>
using namespace std;

int a[100000];
int d[100000];

int main() 
{
	int N, result;
	cin >> N;
	for(int i=0; i<N; i++) 
		cin >> a[i];

	result = a[0];
	for(int i=0; i<N; i++) 
  {
		d[i] = a[i];
		if(i == 0) continue;
		if(d[i] < d[i-1] + a[i])
			d[i] = d[i-1] + a[i];
		if(d[i] > result) 
      result = d[i]; 
	}
	cout << result;
}
```

## 평범한 배낭
```C++
#include<iostream>
#include<algorithm>
using namespace std;

int N, K;
int DP[101][100001];
int Weight[101];
int Value[101];

int main()
{
	cin >> N >> K;

	for (int i=1; i<=N; i++)
		cin >> Weight[i] >> Value[i];

	for (int i=1; i<=N; i++)
	{
		for (int j=1; j<=K; j++)
		{ 
			if (j - Weight[i] >= 0) 
        DP[i][j] = max(DP[i-1][j], DP[i-1][j - Weight[i]] + Value[i]);
			else 
        DP[i][j] = DP[i-1][j];
		}
	}
	cout << DP[N][K];
}
```
