# 분할 정복

## 색종이 만들기
```C++
#include <iostream>
using namespace std;

int N;
int paper[128][128];
int blue, white;

void setting()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      cin >> paper[i][j];
}

void run(int y, int x, int size)
{
  int check = paper[y][x];
  for (int i = y; i < y + size; i++)
  {
    for (int j = x; j < x + size; j++)
    {
      if (check == 0 && paper[i][j] == 1)
        check = 2;
      else if (check == 1 && paper[i][j] == 0)
        check = 2;
      if (check == 2)
      {
        run(y, x, size / 2);
        run(y, x + size / 2, size / 2);
        run(y + size / 2, x, size / 2);
        run(y + size / 2, x + size / 2, size / 2);
        return;
      }
    }
  }
  if (check == 0)
    white++;
  else
    blue++;
}
int main()
{
  setting();
  run(0, 0, N);
  cout << white << '\n';
  cout << blue << '\n';
}
```

## 퀴드트리
```C++
#include <iostream>
#include <string>
using namespace std;

int N;
string S;
int arr[64][64];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> N;

  for (int i = 0; i < N; i++)
  {
    cin >> S;
 
    for (int j = 0; j < N; j++)
      arr[i][j] = S[j] - '0';
  }
}

void run(int n, int y, int x)
{
  if (n == 1)
  {
    cout << arr[y][x];
    return;
  }

  bool zero = true, one = true;
  
  for (int i = y; i < y + n; i++)
  {
    for (int j = x; j < x + n; j++)
    {
      if (arr[i][j])
        zero = false;
      else
        one = false;
    }
  }
  if (zero)
    cout << 0;
  else if(one)
    cout << 1;
  else
  {
    cout << "(";
    run(n / 2, y, x);
    run(n / 2, y, x + n / 2); 
    run(n / 2, y + n / 2, x); 
    run(n / 2, y + n / 2, x + n / 2); 
    cout << ")";
  }
}

int main()
{
  setting();
  run(N, 0, 0);
}
```

## 종이의 개수
```C++

```

## 곱셈
```C++

```

## 이항 계수
```C++

```

## 행렬 제곱
```C++

```

## 피보나치 수 6
```C++

```

## 히스토그램에서 가장 큰 직사각형
```C++

```

## 가장 가까운 두 점
```C++

```
