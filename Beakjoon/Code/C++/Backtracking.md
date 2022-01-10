# 백트래킹

## N과 M 1
```C++
#include <iostream>
using namespace std;
 
int n, m;
int arr[8] = {0};
bool check[8] = {0};

void function(int a) 
{
  if (a == m) 
  {
    for (int i=0; i<m; i++) 
    {
      cout << arr[i] << " ";
    }
    cout << "\n";
    return;
  }
 
  for (int i=1; i<=n; i++) 
  {
    if (!check[i]) 
    {
      check[i] = true;
      arr[a] = i;
      function(a+1);
      check[i] = false;
    }
  }
}
 
int main() 
{ 
  cin >> n >> m; 
  function(0);
}
```

## N과 M 2
```C++
#include <iostream>
using namespace std;

int n,m;
int arr[8] = {0};
bool check[8] = {0};

void function(int a, int b)
{
  if(b == m)
  {
    for(int i = 0; i < m; i++)
      cout << arr[i] << ' ';
    cout << '\n';
    return;
  }
  
  for(int i=a; i<=n; i++)
  {
    if(!check[i])
    {
      check[i] = true;
      arr[b] = i;
      function(i+1, b+1);
      check[i] = false;
    }
  }
}

int main() 
{
  cin >> n >> m;
  function(1,0);
}
```

## N과 M 3
```C++
#include<iostream>
using namespace std;

int arr[8];
int n, m;

void function(int a)
{
	if (a == m+1)
	{
		for (int i=1; i<=m; i++)
			cout << arr[i] << " ";
		cout << "\n";
    return;
	}

	else
	{
		for (int i=1; i<=n; i++)
		{
			arr[a] = i;
			function(a+1);
		}
	}
}

int main()
{
	cin >> n >> m;
	function(1);
}
```

## N과 M 4
```C++
#include <iostream>
using namespace std;

int n,m;
int arr[8] = {0};
bool check[8] = {0};

void function(int a, int b)
{
  if(b == m)
  {
    for(int i = 0; i < m; i++)
      cout << arr[i] << ' ';
    cout << '\n';
    return;
  }
    
  for(int i=a; i<=n; i++)
  {
    check[i] = true;
    arr[b] = i;
    function(i, b+1);
    check[i] = false;
  }
}

int main() 
{
  cin >> n >> m;
  function(1,0);
}
```

## N-Queen
```C++
#include <iostream>
using namespace std;

int n, result = 0;
int arr[15] = {0};

bool check(int a)
{
  for (int i=1; i<a; i++) 
  {
	  if(arr[a] == arr[i] || a - i == abs(arr[a] - arr[i])) 
		  return false;
  }
return true;
}

void function(int a)
{
  if(a == n+1)
  {
    result++;
    return ;
  }
    
  for(int i=1; i<=n; i++)
  {
    arr[a]=i;
    if(check(a)==true)
      function(a+1);
  }
  return ;
}

int main()
{
  cin >> n;
  function(1);
  cout << result;
}
```

## 스도쿠
```C++
#include <iostream>
using namespace std;

int board[9][9];

// (y,x) 좌표에 n 이 들어갈 수 있는 지 확인
bool check(int y, int x, int n)
{
  for(int i=0; i<9; i++)
  { 
    if(board[y][i]==n) return false;
    if(board[i][x]==n) return false;
  }

  for(int i=(y/3)*3; i<(y/3)*3+3; i++)
    for(int j=(x/3)*3; j<(x/3)*3+3; j++)
      if(board[i][j]==n) return false;

  return true;
}

void solve(int y, int x)
{
  // 좌표 조정
  if(x==9) {y++; x=0;}

  // 스도쿠 끝까지 도달 시
  if(y==9)
  {
    for(int i=0;i<9;i++)
    {
      for(int j=0;j<9;j++)
        cout << board[i][j] << " ";
      cout << "\n";
    }
    exit(0);
  }

  // 이미 채워져있으면 패스
  if(board[y][x]!=0)
  {
    solve(y,x+1);
    return;
  }

  // 백트래킹
  for(int i=1;i<=9;i++)
  {
    if(check(y,x,i))
    {
      board[y][x]=i;
      solve(y,x+1);
      board[y][x]=0;
    }
  }
}

int main()
{
  for(int i=0;i<9;i++)
    for(int j=0;j<9;j++)
      cin >> board[i][j];

  solve(0,0);
}
```

## 연산자 끼워넣기
```C++
#include <iostream>
using namespace std;

int N;
int object[11]; 
int operators[4];
int max_value = -1000000001;
int min_value = 1000000001;

void run(int result, int idx)
{
  if(idx == N)
  {
    if(result > max_value)
      max_value = result;
    if(result < min_value)
      min_value = result;
    return;
  }
  
  for(int i=0; i<4; i++)
  {
    if(operators[i] > 0)
    {
      operators[i]--;
      if(i == 0)
        run(result + object[idx], idx+1);
      else if(i == 1)
        run(result - object[idx], idx+1);
      else if(i == 2)
        run(result * object[idx], idx+1);
      else
        run(result / object[idx], idx+1);
      
      operators[i]++;
    }
  }
  return;
}

int main() 
{
  cin >> N;
  for(int i = 0; i < N; i++)
    cin >> object[i];
  for(int i = 0; i < 4; i++)
    cin >> operators[i];
  
  run(object[0],1);

  cout << max_value << '\n';
  cout << min_value;
}
```

## 스타트와 링크
```C++
#include<iostream>
#include<math.h>
using namespace std;

int stats[21][21];
bool check[22];
int N;
int ans = 1000000000;

void DFS(int x, int pos) // x는 카운트 수, pos는 다음 값
{
	if (x == N/2) // 카운트수가 정원의 1/2이 됐을 때 능력치합 계산
	{
		int start, link;
		start = 0;
		link = 0;

		for (int i=1; i<=N; i++)
		{
			for (int j=1; j<=N; j++)
			{
				if (check[i] == true && check[j] == true) start += stats[i][j];
				if (check[i] == false && check[j] == false) link += stats[i][j];
			}
		}

		int temp = abs(start - link);
		if (ans > temp) ans = temp;

		return;
	}

	for (int i = pos; i < N; i++)
	{
		check[i] = true;
		DFS(x+1, i+1);
		check[i] = false;
	}
}

int main()
{
	cin >> N;

	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			cin >> stats[i][j];

	DFS(0, 1); // 카운트 0회부터 숫자는 1부터 시작

	cout << ans;
}
```
