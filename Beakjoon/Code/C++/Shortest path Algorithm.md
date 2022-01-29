# 최단 경로 알고리즘

# 최단 경로
```C++
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<pair<int,int>> v[20001];
priority_queue<pair<int,int>> pq;
bool visited[20001];
int Distance[20001];
int V, E,K;
int MAX_VALUE = 987654321;

void DIJK(int start)
{
  pq.push({0,start});
  Distance[start] = 0;
    
  while(!pq.empty())
  {
    int cost = pq.top().first;
    int node = pq.top().second;
        pq.pop();
        
    if(visited[node] ==true) continue;
        
    visited[node] = true;

    for(int i = 0; i< v[node].size(); i++)
    {
      int Next_Node = v[node][i].first;
      int Next_Cost = v[node][i].second; 

      if(visited[Next_Node] == false && Distance[Next_Node] > Distance[node] + Next_Cost)
      {
        Distance[Next_Node] = Distance[node] + Next_Cost; 
        pq.push({-(Distance[node] + Next_Cost), Next_Node});
      }
    }
  }
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> V >> E >> K;
  //dist 높은값 설정.
  for(int i = 1; i<=V; i++)
    Distance[i] = MAX_VALUE;

  //간선정보 입력
  for(int i = 0; i< E; i++)
  {
    int U, V, W;
    cin >> U >> V >> W;
    v[U].push_back({V,W});
  }
}

void print()
{
  for(int i = 1; i<= V; i++)
  {
    if(Distance[i] == MAX_VALUE) 
      cout << "INF" << "\n";
    else
      cout << Distance[i]<<'\n';
    }
}

int main()
{
  setting();
  DIJK(K);
  print();
}

```

# 특정한 최단 경로
```C++
#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int a, b, c, v1, v2;
int N, E;
long long x, y;
long long result_1[801], result_v1[801], result_v2[801];
vector<pair<int, int>> v[801];
queue<int> q;
int MAX_Value = 987654321;

void DIJK(int start, long long* result)
{
	for (int i = 1; i <= N; i++)
		result[i] = MAX_Value;

	result[start] = 0;
	q.push(start);

	while (!q.empty())
	{
		int node = q.front();
		int distance = result[node];
		q.pop();

		for (int i = 0; i < v[node].size(); i++)
		{
			int next_node = v[node][i].first;
			int next_distance = v[node][i].second;

			if (result[next_node] > distance + next_distance)
			{
				result[next_node] = distance + next_distance;
				q.push(next_node);
			}
		}
	}
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
	cin >> N >> E;

	for (int i = 0; i < E; i++)
	{
		cin >> a >> b >> c;
		v[a].push_back(pair<int, int>(b, c));
		v[b].push_back(pair<int, int>(a, c));
	}

	cin >> v1 >> v2;
}

void run()
{
	DIJK(1, result_1);
	DIJK(v1, result_v1);
	DIJK(v2, result_v2);

	x = result_1[v1] + result_v1[v2] + result_v2[N];
	y = result_1[v2] + result_v2[v1] + result_v1[N];
}

void print()
{
	if (min(x, y) >= MAX_Value) 
    cout << -1;
	else 
    cout << min(x, y);
}

int main()
{
  setting();
  run();
  print();
}
```

# 미확인 도착지
```C++

```

# 타임머신
```C++

```

# 플로이드
```C++

```

# KCM Travel
```C++

```

# 운동
```C++

```
