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

```

## 계단 오르기
```C++

```

## 1로 만들기
```C++

```

## 쉬운 계단 수
```C++

```

## 포도주 시식
```C++

```

## 가장 긴 증가하는 부분 수열
```C++

```

## 전깃줄
```C++

```

## LCS
```C++

```

## 연속합
```C++

```

## 평범한 배낭
```C++

```
