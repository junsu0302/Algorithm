# DFS와 BFS

## DFS와 BFS
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int N, M, V; 
int arr[1001][1001]; 
bool visited[1001]; 
queue<int> q;
 
void setting()
{
  cin >> N >> M >> V;
 
  for (int i = 0; i < M; i++) 
  {
    int a, b;
    cin >> a >> b;
    arr[a][b] = 1;
    arr[b][a] = 1;
  }
}

void Reset() 
{
  for (int i = 1; i <= N; i++)
    visited[i] = 0;
}
 
void DFS(int v) 
{
  visited[v] = true;
  cout << v << " ";
    
  for (int i = 1; i <= N; i++)
    if (arr[v][i] == 1 && visited[i] == 0)
      DFS(i);
}
 
void BFS(int v) 
{
  q.push(v);
  visited[v] = true;
  cout << v << " ";
 
  while (!q.empty()) 
  {
    v = q.front();
    q.pop();
        
    for (int w = 1; w <= N; w++) 
    {
      if (arr[v][w] == 1 && visited[w] == 0) 
      {
        q.push(w);
        visited[w] = true;
        cout << w << " ";
      }
    }
  }
}
 
int main() 
{
  setting();
 
  Reset();
  DFS(V);
    
  cout << '\n';
    
  Reset();
  BFS(V);
}
```

## 바이러스
```C++
#include <iostream>
using namespace std;
 
int V, E;
int arr[101][101];
bool visited[101];
int ans = 0;
 
void DFS(int v) 
{
  visited[v] = true;
  ans++;
 
  for (int i = 1; i <= V; i++) 
    if (visited[i]==0 && arr[v][i] == 1) 
      DFS(i);
}
 
void setting()
{
  cin >> V >> E;
  for (int i = 0; i < E; i++) 
  {
    int a, b;
    cin >> a >> b;
    arr[a][b] = 1;
    arr[b][a] = 1;
  }
}

int main() 
{
  setting();
  
  DFS(1);
    
  cout << ans - 1;
}
```

## 단자번호 붙이기
```C++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
 
int N;
int arr[25][25];
bool visited[25][25];
int X_Move[] = { 1, -1, 0, 0 };
int Y_Move[] = { 0, 0, 1, -1 };
int house = 0;
int label = 1;
vector<int> v;

void DFS(int y, int x) 
{
  visited[y][x] = true;
  arr[y][x] = label;
  house++;
 
  for (int i = 0; i < 4; i++) 
  {
    int X_Arrival = x + X_Move[i];
    int Y_Arrival = y + Y_Move[i];
        
    if (X_Arrival < 0 || Y_Arrival < 0 || X_Arrival >= N || Y_Arrival >= N)  
      continue;
 
    if (arr[Y_Arrival][X_Arrival] == 1 && visited[Y_Arrival][X_Arrival] == 0) 
      DFS(Y_Arrival, X_Arrival);
  }
}

void setting()
{
  cin >> N;
    
  for (int i = 0; i < N; i++) 
  {
    string input;
    cin >> input;
 
    for (int j = 0; j < N; j++)
      arr[i][j] = input.at(j) - '0';
  }
}
 
void run()
{
  for (int i = 0; i < N; i++) 
  {
    for (int j = 0; j < N; j++) 
    {
      if (arr[i][j] == 1 && visited[i][j] == 0) 
      {
        DFS(i, j);
        label++;
        v.push_back(house);
        house = 0;
      }
    }
  }
}

void print()
{
  cout << label-1 << "\n";
  for (int i = 0; i < v.size(); i++)
        cout << v[i] << "\n";
}

int main() 
{
  setting();
  run();
 
  sort(v.begin(), v.end());
 
  print();
}
```

## 유기농 배추
```C++
#include <iostream>
using namespace std;
 
int T, M, N, K, cnt;
int arr[51][51];
int visited[51][51];
int X_Move[] = { -1, 1, 0, 0 };
int Y_Move[] = { 0, 0, -1, 1 };
 
void reset() 
{
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      arr[i][j] = 0;
    
    for (int i = 0; i < N; i++)
      for (int j = 0; j < M; j++)
        visited[i][j] = 0;
}
 
void DFS(int y, int x) 
{
    visited[y][x] = 1;
 
    for (int i = 0; i < 4; i++) 
    {
      int X_Arrival = x + X_Move[i];
      int Y_Arrival = y + Y_Move[i];
 
      if (X_Arrival < 0 || X_Arrival >= M || Y_Arrival < 0 || Y_Arrival >= N)
        continue;
        
      if (arr[Y_Arrival][X_Arrival] == 1 && visited[Y_Arrival][X_Arrival] == 0)
        DFS(Y_Arrival, X_Arrival);
    }
}
 
void setting()
{
  cin >> M >> N >> K;

  reset();
 
  while (K--) 
  {
    int x, y;
    cin >> x >> y;
    arr[y][x] = 1;
  }
}

void run()
{
  cnt = 0;
  for (int i = 0; i < N; i++) 
  {
    for (int j = 0; j < M; j++) 
    {
      if (arr[i][j] == 1 && visited[i][j] == 0) 
      {
        DFS(i, j);
        cnt++;            
      }
    }
  }
}

void print()
{
  cout << cnt << "\n";
}

int main() 
{
  cin >> T;
  while (T--) 
  {
    setting();
    run();
    print();
  }
}
```

## 미로 탐색
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int N, M;
int map[101][101];
bool visited[101][101];
int path[101][101];
int X_Move[] = { 1, -1, 0, 0 };
int Y_Move[] = { 0, 0, -1, 1 };
queue<pair<int, int>> q;

void BFS(int y, int x) 
{
  path[y][x] = 1;
  visited[y][x] = true;
  q.push(make_pair(y, x));
 
  while (!q.empty()) 
  {
    y = q.front().first;
    x = q.front().second;
    q.pop();
 
    for (int i = 0; i < 4; i++) 
    {
      int Y_Arrival = y + Y_Move[i];
      int X_Arrival = x + X_Move[i];
 
      if (Y_Arrival < 0 || X_Arrival < 0 || Y_Arrival >= N || X_Arrival >= M)
        continue;
      if (map[Y_Arrival][X_Arrival] == 1 && visited[Y_Arrival][X_Arrival] == 0) 
      {
        visited[Y_Arrival][X_Arrival] = true;
        q.push(make_pair(Y_Arrival, X_Arrival));
        path[Y_Arrival][X_Arrival] = path[y][x] + 1;
      }
    }
  }
}
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M;
 
  string input;
  for (int i = 0; i < N; i++) 
  {
    cin >> input;
    for (int j = 0; j < M; j++)
      map[i][j] = input[j] - '0';
  }
}

void print()
{
  cout << path[N - 1][M - 1];
}

int main() 
{
  setting();
  BFS(0, 0);
  print();
}
```

## 토마토
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int M, N, ans;
int map[1001][1001];
bool visited[1001][1001];
int path[1001][1001];
int X_Move[] = { 1, -1, 0, 0 };
int Y_Move[] = { 0, 0, 1, -1 };
queue<pair<int,int>> q;

void BFS() 
{
  while (!q.empty()) 
  {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();
 
    for (int i = 0; i < 4; i++) 
    {
      int X_Arrival = x + X_Move[i];      
      int Y_Arrival = y + Y_Move[i];

 
      if (Y_Arrival < 0 || X_Arrival < 0 || Y_Arrival >= N || X_Arrival >= M)
        continue;
      if (map[Y_Arrival][X_Arrival] == 0 && visited[Y_Arrival][X_Arrival] == 0) 
      {
        visited[Y_Arrival][X_Arrival] = true;
        q.push(make_pair(Y_Arrival, X_Arrival));
        path[Y_Arrival][X_Arrival] = path[y][x] + 1;
      }
    }
  }
}
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);  
  
  cin >> M >> N;
 
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      cin >> map[i][j];
 
  for (int i = 0; i < N; i++) 
    for (int j = 0; j < M; j++)
      if (map[i][j] == 1)
        q.push(make_pair(i, j));
}

void run()
{
  ans = -1;
  for (int i = 0; i < N; i++) 
    for (int j = 0; j < M; j++) 
      if (path[i][j] > ans) 
        ans = path[i][j];
}

void print()
{
  cout << ans;
}

int main() 
{
  setting();
  BFS();

  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      if (map[i][j] == 0 && path[i][j]==0)
      {
        cout << -1;
        return 0;
      }
      
  run();
  print();
}
```

## 숨바꼭질
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int N, K;
bool visited[100001];
int path[100001];
queue<int> q;
 
void BFS(int a) 
{
  path[a] = 0;
  visited[a] = true;
  q.push(a);
 
  while (!q.empty()) 
  {
    int s = q.front();
    if (s == K) break;
    q.pop();
 
    if (visited[s + 1] == 0 && s + 1 >= 0 && s + 1 < 100001) 
    {
      visited[s + 1] = true;
      q.push(s + 1);
      path[s + 1] = path[s] + 1;
    }
    if (visited[s - 1] == 0 && s - 1 >= 0 && s - 1 < 100001) 
    {
      visited[s - 1] = true;
      q.push(s - 1);
      path[s - 1] = path[s] + 1;
    }
    if (visited[s * 2] == 0 && s * 2 >= 0 && s * 2 < 100001) 
    {
      visited[s * 2] = true;
      q.push(s * 2);
      path[s * 2] = path[s] + 1;
    }
  }
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;
}

void print()
{
  cout << path[K];
}

int main() 
{
  setting();

  BFS(N);
 
  print();
}
```

## 벽 부수고 이동하기
```C++
#include<iostream>
#include<string>
#include<queue>
using namespace std;
 
int N, M;
int MAP[1000][1000];
bool Visit[1000][1000][2];
queue<pair<pair<int, int>, pair<int,int>>> Q;
 
int X_Move[] = { 0, 0, 1, -1 };
int Y_Move[] = { 1, -1, 0, 0 };
 

 
int BFS()
{
  Q.push(make_pair(make_pair(0, 0), make_pair(0, 1)));
  Visit[0][0][0] = true;
 
  while (Q.empty() == 0)
  {
    int x = Q.front().first.first;
    int y = Q.front().first.second;
    int B = Q.front().second.first;
    int cnt = Q.front().second.second;
    Q.pop();
 
    if (x == N - 1 && y == M - 1)  return cnt;
    for (int i = 0; i < 4; i++)
    {
      int X_Arrival  = x + X_Move[i];
      int Y_Arrival  = y + Y_Move[i];
 
      if (X_Arrival  >= 0 && Y_Arrival >= 0 && X_Arrival  < N && Y_Arrival < M)
      {
        if (MAP[X_Arrival ][Y_Arrival] == 1 && B == 0)
        {
          Visit[X_Arrival ][Y_Arrival][B+1] = true;
          Q.push(make_pair(make_pair(X_Arrival , Y_Arrival), make_pair(B + 1, cnt + 1)));
        }
        else if (MAP[X_Arrival ][Y_Arrival] == 0 && Visit[X_Arrival ][Y_Arrival][B] == false)
        {
          Visit[X_Arrival ][Y_Arrival][B] = true;
          Q.push(make_pair(make_pair(X_Arrival , Y_Arrival), make_pair(B, cnt + 1)));
        }
      }
    }
  }
  return -1;
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N >> M;
  
  for (int i = 0; i < N; i++)
  {
    string Number;
    cin >> Number;
    for (int j = 0; j < M; j++)
    {
      int tmp = Number[j] - '0';
      MAP[i][j] = tmp;
    }
  }
}

void print()
{
  cout << BFS();
}

int main()
{
  setting();
  print();
}


```

## 나이트의 이동
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int T, L;
int a, b, c, d;
int map[300][300];
bool visited[300][300];
int path[300][300];
int Move_x[] = {1,2,-1,-2,1,2,-1,-2};
int Move_y[] = {2,1,2,1,-2,-1,-2,-1};
queue<pair<int, int>> q;
 
void reset() 
{
  for (int i = 0; i < L; i++) 
  {
    for (int j = 0; j < L; j++) 
    {
      map[i][j] = 0;
      visited[i][j] = 0;
      path[i][j] = 0;
    }
  }
  while (!q.empty()) 
    q.pop();
}

void BFS(int x, int y) 
{
  visited[x][y] = true;
  q.push(make_pair(x, y));
 
  while (!q.empty()) 
  {
    int x = q.front().first;
    int y = q.front().second;
    q.pop();
 
    if (x == c && y == d) break;
 
    for (int i = 0; i < 8; i++) 
    {
      int Arrivla_y = y + Move_y[i];
      int Arrivla_x = x + Move_x[i];
 
      if (Arrivla_x < 0 || Arrivla_y < 0 || Arrivla_x >= L || Arrivla_y >= L)
        continue;
      if (visited[Arrivla_x][Arrivla_y] == 0) 
      {
        visited[Arrivla_x][Arrivla_y] = true;
        q.push(make_pair(Arrivla_x, Arrivla_y));
        path[Arrivla_x][Arrivla_y] = path[x][y] + 1;
      }
    }
  }
}
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL); 
  cin >> T;  
}

void run()
{
  while (T--) 
  {
    reset();
    cin >> L;
    cin >> a >> b >> c >> d;
    BFS(a, b);
    cout << path[c][d] << "\n";
    }
}

int main() 
{
  setting();
  run();
}
```

## 이분 그래프
```C++

```
