# 동적 계획법과 최단거리 역추적

## 1로 만들기 2
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int X;
int before[1000001];
int dp[1000001];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> X;
}

void solve_1(int i)
{
	if (i % 3 == 0)
	{
		if (dp[i] > dp[i / 3] + 1)
		{
			dp[i] = dp[i / 3] + 1;
			before[i] = i / 3;
		}		
	}
}

void solve_2(int i)
{
	if (i % 2 == 0)
	{
		if (dp[i] > dp[i / 2] + 1)
		{
			dp[i] = dp[i / 2] + 1;
			before[i] = i / 2;
		}
	}
}

int solve(int N)
{
	dp[1] = 0;
	for (int i = 2; i <= N; i++)
	{
		dp[i] = dp[i - 1] + 1;
		before[i] = i - 1;

    solve_1(i);
    solve_2(i);
	}
	return dp[N];
}

void run()
{
	cout << solve(X) << '\n';

	while (true)
	{
		cout << X << " ";
		X = before[X];
		if (X == 0) break;
	}
}

int main()
{
  setting();
  run();
}
```

## 가장 긴 증가하는 부분 수열 4
```C++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, A[1001], len;
int index, tmp;
int dp[1001];
vector<int> v;

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
	{
		cin >> A[i];
		len = 0;

		for (int j = 1; j < i; j++)
		{
			if (A[j] < A[i])
				len = max(dp[j], len);
		}
		dp[i] = len + 1;
		
		if (tmp < len + 1)
		{
			tmp = len + 1;
			index = i;
		}
	}

  for (int i = index; i >= 1; i--)
	{
		if (dp[i] == tmp)
		{
			v.push_back(A[i]);
			tmp--;
		}
	}
}

void print()
{
	int size = v.size();
	cout << size << '\n'; 
	for (int i = 0; i < size; i++)
	{
		cout << v.back() << " ";
		v.pop_back();
	}
}

int main()
{
	setting();
  run();
  print();
}
```

## 가장 긴 증가하는 부분 수열 5
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, cnt;
int arr[1000001], check[1000001];
vector<int> ans, print;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N;
}

void running()
{
	for (int i = 1; i <= N; i++) 
    cin >> arr[i];

	ans.push_back(arr[1]);
	for (int i = 2; i <= N; i++) 
  {
		if (ans[cnt] < arr[i]) 
    {
			ans.push_back(arr[i]);
			cnt++;
			check[i] = cnt;
		}
		else 
    {
			int tmp = lower_bound(ans.begin(), ans.end(), arr[i]) - ans.begin();
			ans[tmp] = arr[i];
			check[i] = tmp;
		}
	}
}

void printing()
{
	cout << cnt + 1 << '\n';
	for(int i=N; i>=1 && cnt >=0; i--)
  {
		if (check[i] == cnt) 
    {
			print.push_back(arr[i]);
			cnt--;
		}
	}

	for (int i = print.size() - 1; i >= 0; i--)
		cout << print[i] << ' ';
}

int main()
{
  setting();
  running();
  printing();
}
```

## LCS 2
```C++
#include<iostream>
#include<string>
#include<vector>
using namespace std;

string s1, s2;
string LCS[1001][1001];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> s1 >> s2;
}

void running()
{
	for (int i = 1; i <= s1.length(); i++)
	{
		for (int j = 1; j <= s2.length(); j++)
		{
			if (s1[i-1] == s2[j-1])
			{	
				LCS[i][j] = LCS[i-1][j-1] + s1[i-1];
			}
			else
			{
				if(LCS[i-1][j].length() >= LCS[i][j-1].length())
					LCS[i][j] = LCS[i-1][j];
				else
					LCS[i][j] = LCS[i][j-1];
			}
		}
	}
}

void printing()
{
	cout << LCS[s1.length()][s2.length()].length() << '\n';
	cout << LCS[s1.length()][s2.length()] <<'\n';
}

int main()
{
  setting();
  running();
  printing();
}
```

## 경찰차
```C++

```

## 숨바꼭질 4
```C++

```

## DSLR
```C++

```

## 최소비용 구하기 2
```C++

```

## 플로이드 2
```C++

```
