# 정수론 및 조합론

## 배수와 약수
```C++
#include<iostream>
using namespace std;

int a, b;

int main()
{
	while (1)
	{
		cin >> a >> b;
		if(a == 0 && b == 0)  break;
		if(a == 0 || b == 0)  cout << "neither" << "\n";
		else if(a % b == 0)  cout << "multiple" << "\n";
		else if(b % a == 0)  cout << "factor" << "\n";
		else cout << "neither" << "\n";
	}
}
```

## 약수
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
  int n;
  int arr[51];
  cin >> n;
  for(int i=0; i<n; i++)  cin >> arr[i];
  sort(arr, arr + n);

  cout << arr[0] * arr[n-1];
}
```

## 최대공약수와 최소공배수
```C++
#include <iostream>
using namespace std;

int GCD(int a, int b) 
{
	int c = a % b;
	while (c != 0) 
  {
		a = b;
		b = c;
		c = a % b;
	}
	return b;
}

int LCM(int a, int b) 
{
	return (a * b) / GCD(a, b);
}

int main() 
{
	int a, b;
	cin >> a >> b;
	cout << GCD(a, b) << "\n";
  cout << LCM(a, b);
}
```

## 최소공배수
```C++
#include <iostream>
using namespace std;

int GCD(int a, int b) 
{
	int c = a % b;
	while (c != 0) 
  {
		a = b;
		b = c;
		c = a % b;
	}
	return b;
}

int LCM(int a, int b) 
{
	return (a * b) / GCD(a, b);
}

int main() 
{
	int N, a, b;
	cin >> N;

	for (int i=0; i<N; i++)
	{
		cin >> a >> b;
    cout << LCM(a,b) << "\n";
  }
}
```

## 검문
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, gcd;
int x;
vector<int> v, ans;

int GCD(int a, int b) 
{
	if (b == 0) return a;
	return GCD(b, a % b);
}

void setting()
{
	cin >> N;

	for (int i = 0; i < N; i++) 
	{	
		cin >> x;
		v.push_back(x);
	}
}

void run()
{
	sort(v.begin(), v.end());
	gcd = v[1] - v[0];

	for (int i=2; i<N; i++) 
    gcd = GCD(gcd, v[i] - v[i - 1]);

	for (int i=2; i*i<=gcd; i++) 
  {
		if (gcd % i == 0)
		{
			ans.push_back(i); 
			ans.push_back(gcd / i);
		}
  }
	ans.push_back(gcd);
  sort(ans.begin(), ans.end());
	ans.erase(unique(ans.begin(), ans.end()), ans.end());
}

int main() 
{
  setting();
  run();
	for(int i=0; i<ans.size(); i++) 
    cout << ans[i] << " ";
}
```

## 링
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, num;
int arr[101];

int GCD(int a, int b) 
{
	if (b == 0) return a;
	return GCD(b, a % b);
}

void setting()
{
  cin >> N;
  cin >> arr[0];
}

void run()
{
  for (int i=1; i<N; i++) 
  {
    cin >> arr[i];
    num = GCD(arr[0], arr[i]);
    cout << arr[0] / num << "/" << arr[i] / num << "\n";
  }
}

int main() 
{
  setting();
  run();
}
```

## 이항 게수1
```C++
#include<iostream>
using namespace std;
 
int N, K;

void setting()
{
  cin >> N >> K;
}
 
int run(int i)
{
  if(i == 1 || i == 0)  return 1;    
  else  return run(i-1) * i;
}
 
int main()
{  
  setting();
  cout << run(N) / (run(K) * run(N-K)); 
}
```

## 이항 계수 2
```C++
#include<iostream>
using namespace std;

int N, K;
long long DP[1001][1001];

void setting()
{
	cin >> N >> K;

	DP[0][0] = 1;
	DP[1][0] = 1;
	DP[1][1] = 1;
}

void run()
{
	for(int i=2; i<=N; i++)
  {
		for(int j=0; j<=i; j++)
		{
			if (j == 0)  DP[i][0] = 1;
			else if (j == i)  DP[i][j] = 1;
			else  DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j]) % 10007;
    }
  }
}

int main()
{
  setting();
  run();	
	cout << DP[N][K];
}
```

## 다리 놓기
```C++
#include<iostream>
#include<vector>
using namespace std;

int N, A, B;

int func(int n,int m) 
{
	vector<vector<int>> v(n+1,vector<int>(m+1,0));
	for(int i=1; i<=m; i++)	
		v[1][i] = i;
	
	for(int i=2; i<=n; i++) 
  {
		for(int j=i; j<=m; j++) 
    {
			if(j == i) 
      {
				v[i][j] = 1;
				continue;
			}
			for(int k=i-1; k<=j-1;k++) 
				v[i][j] += v[i-1][k];
		}
	}

	return v[n][m];
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run()
{
	for(int i=0; i<N; i++)
  {
	cin >> A >> B;
	cout << func(A,B) << "\n";
	}
}

int main() 
{
  setting();
  run();
}
```

## 패션왕 신해빈
```C++
#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int T, N;

void setting()
{
  cin >> T;
}

void run()
{
  while (T--) 
  {
		vector<int> v;
		map<string, int> m;
		cin >> N;
		while (N--) 
    {
			string clothes, kind;
			cin >> clothes >> kind;
			m[kind]++;
		}

		int ans = 1;
		map<string, int>::iterator iter;
		for(iter = m.begin(); iter != m.end(); iter++)
			ans *= (iter->second + 1);
		cout << ans - 1 << "\n";
	}
}

int main()
{
	setting();
  run();
}
```

## 팩토리얼 0의 개수
```C++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
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
    int num = i;
    for (int j = 2; j * j <= i; j++)
    {
      while (num % j == 0)
      {
        v.push_back(j);
        num = num / j;
      }
    }

    if (num > 1)
      v.push_back(num);
  }
}

int main()
{
  setting();
  run();
  cout << count(v.begin(), v.end(), 5);
}
```

## 조합 0의 개수
```C++
#include <iostream>
using namespace std;
 
int N, M;
int cnt5, cnt2;
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N >> M;
}

void run()
{
  for(long long i=5; i<=N; i*=5)
    cnt5 += N / i;
  for(long long i=5; i<=N-M; i*=5)
    cnt5 -= (N - M) / i;
  for(long long i=5; i<=M; i*=5)
    cnt5 -= M / i;
  for(long long i=2; i<=N; i*=2)
    cnt2 += N / i;
  for(long long i=2; i<=N-M; i*=2)
    cnt2 -= (N - M) / i;
  for(long long i=2; i<=M; i*=2)
    cnt2 -= M / i;
}

int main()
{
  setting();
  run();

  if (cnt5 >= cnt2)
    cout << cnt2;
  else
    cout << cnt5;
}
```
