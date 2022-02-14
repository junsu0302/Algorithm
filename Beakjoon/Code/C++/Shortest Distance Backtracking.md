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
#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

int N, W;
vector<pair<int,int>> p;
int store[1010][1010];
int police_store[1010][1010];

int calculate_distance(int police, int target, int start)
{
  int police_x,police_y,target_x,target_y;
  if(start == 1)
  {
    police_x = 1;
    police_y = 1;
  }
  else if(start == 2)
  {
    police_x = N;
    police_y = N;
  }
  else
  {
    police_x = p[police-1].first;
    police_y = p[police-1].second;
  }
  target_x = p[target-1].first;
  target_y = p[target-1].second;
  return abs(police_x-target_x) + abs(police_y-target_y);
}

int moving_distance(int police1, int police2)
{
  if(police1 == W || police2 == W)
    return 0;

  int tmp1, tmp2, move;

  move = max(police1, police2) + 1;
  if(store[police1][police2] != -1)
    return store[police1][police2];

  if(police1 == 0)
    tmp1 = moving_distance(move,police2) + calculate_distance(police1, move, 1);
  else
    tmp1 = moving_distance(move,police2) + calculate_distance(police1, move, 0);

  if(police2 == 0)
    tmp2 = moving_distance(police1,move) + calculate_distance(police2, move, 2);
  else
    tmp2 = moving_distance(police1,move) + calculate_distance(police2, move, 0);

  store[police1][police2] = min(tmp1,tmp2);

  if(tmp1 < tmp2)
    police_store[police1][police2] = 1;
  else
    police_store[police1][police2] = 2;
    
  return min(tmp1,tmp2);
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int tmp1,tmp2;
  cin >> N;
  cin >> W;

  for(int i=0; i<W; i++)
  {
    cin >> tmp1;
    cin >> tmp2;
    p.push_back(make_pair(tmp1,tmp2));
  }

  for(int i=0; i<1010; i++)
  {
    for(int j=0; j<1010; j++)
    {
      store[i][j] = -1;
      police_store[i][j] = -1;
    }
  }
}

void running()
{
  cout << moving_distance(0,0) << "\n";

  int x = 0;
  int y = 0;
    
  for(int i=0; i<W; i++)
  {
    cout << police_store[x][y] << "\n";
    if(police_store[x][y] == 1)
      x = i+1;
    else
      y = i+1;
  }
}

int main()
{
  setting();
  running();
}
```

## 숨바꼭질 4
```C++
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
 
using namespace std;
 
int N, K;
bool visited[200001];
int path[200001];
queue<pair<int, int> > qu;
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;
}

void running() 
{
  qu.push({ N,0 });
 
  while (!qu.empty()) 
  {
    pair<int, int> find = qu.front();
    qu.pop();
 
    if (find.first == K) 
    {
      cout << find.second << "\n";
      vector<int> ans;
      int count = find.second;
      int next = K;
      ans.push_back(K);
      while (count--) 
      {
        ans.push_back(path[next]);
        next = path[next];
      }
      reverse(ans.begin(), ans.end());
 
      for (int i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";
      return;
    }
        
    if (find.first * 2 <= K * 2 && !visited[find.first * 2]) 
    {
      qu.push({ find.first * 2, find.second + 1 });
      visited[find.first * 2] = true;
      path[find.first * 2] = find.first;
    }
        
    if (find.first + 1 <= K && !visited[find.first + 1]) 
    {
      qu.push({ find.first + 1, find.second + 1 });
      visited[find.first + 1] = true;
      path[find.first + 1] = find.first;
    }
 
    if (find.first > 0 && !visited[find.first - 1]) 
    {
      qu.push({ find.first - 1, find.second + 1 });
      visited[find.first - 1] = true;
      path[find.first - 1] = find.first;
    }
  }
}
 
int main() 
{
  setting();
  running();
}
```

## DSLR
```C++
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;
 
int T, A, B;
bool c[10001];
 
int cmd_d(int n) 
{
    if (n * 2 > 9999) return (2 * n) % 10000;
    else return (2 * n);
}
int cmd_s(int n) 
{
    if (n == 0) return 9999;
    else return n - 1;
}
int cmd_L(int n) 
{
    int first = n / 1000;
    int temp = (n % 1000) * 10;
    return temp + first;
}
int cmd_R(int n) 
{
    int last = (n % 10);
    int temp = (n / 10);
    return (last * 1000) + temp;
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> T;  
}

void running()
{
  while (T--) 
  {
    cin >> A >> B;
    queue<pair<int, string> >q;
    memset(c, false, sizeof(c));
 
    q.push(make_pair(A, ""));
    while (!q.empty()) 
    {
      int num = q.front().first;
      string k = q.front().second;
            
      if (num == B) 
      {
        cout << k << "\n";
        break;
      }
      
      q.pop();
      int x = cmd_d(num);
      if (c[x] == false) 
      {
        c[x] = true;
        q.push(make_pair(x, k + "D"));
      }
      
      x = cmd_s(num);
      if (c[x] == false) 
      {
        c[x] = true;
        q.push(make_pair(x, k + "S"));
      }
      
      x = cmd_L(num);
      if (c[x] == false) 
      {
        c[x] = true;
        q.push(make_pair(x, k + "L"));
      }
      
      x = cmd_R(num);
      if (c[x] == false) 
      {
        c[x] = true;
        q.push(make_pair(x, k + "R"));
      }
    }
  }
}

int main()
{
  setting();
  running();
}
```

## 최소비용 구하기 2
```C++

```

## 플로이드 2
```C++

```
