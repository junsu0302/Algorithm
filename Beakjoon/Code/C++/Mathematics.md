# 수학

## 손익분기점
```C++
#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    int n = 1;
    cin>> a >> b >> c;

    if(b >= c)
      cout << -1;
    else
      cout << a/(c-b) + 1;
}
```

## 벌집
```C++
#include <iostream>
using namespace std;

int main() 
{
    int n;
    cin >> n;
    int i = 0;
    
    for(int num=2; num <= n; i++)
      num += 6 * i;
    if(n == 1) 
      i=1;
    cout << i;
}
```

## 분수찾기
```C++
#include <iostream>
using namespace std;

int main() 
{
  int n;
  cin >> n;

  int i = 1;
  while (n > i) 
  {
    n -= i;
    i++;
  }
  if (i % 2 == 1)
    cout << i+1-n << '/' << n;
  else
    cout << n << '/' << i+1-n;
}
```

## 달팽이는 올라가고 싶다
```C++
#include <iostream>
using namespace std;

int main() 
{
	int a, b, v;
	cin >> a >> b >> v;

	int i = 1 + (v-a)/(a-b);

  if((v-a)%(a-b) != 0)
  {
    i++;
    cout << i;
  }
  else if(a >= v)
    cout << "1";
  else
    cout << i;
}
```

## ACM 호텔
```C++
#include <iostream>
using namespace std;

int main() 
{
  int num;
  cin >> num;
  int h,w,n;

  for(int i=0; i<num; i++)
  {
    cin>> h >> w >> n;
    int H, W;
    H = n%h;
    W = n/h;
    
    if(H > 0)
      W++;
    else
      H = h;
    cout<<H * 100 + W<<'\n';
  }
}
```

## 부녀회장이 될테야
```C++
#include <iostream>
using namespace std;

int function(int a, int b)
{
  if(b == 1)
    return 1;
  if(a == 0)
    return b;
  return (function(a-1, b) + function(a, b-1));
}

int main() 
{
  int t, k, n;
  cin >> t;

  for(int i=0; i<t; i++)
  {
    cin >> k >> n;
    cout << function(k, n) << '\n';
  }
}
```

## 설탕 배달
```C++
#include <iostream>
using namespace std;

int main() 
{
  int n;
  cin >> n;
  int num = 0;

  while(n>=0) 
  {
    if (n%5 == 0) 
    {
      num += n/5;
      cout << num;
      return 0;
    }
	n -= 3; 
	num++;
  }
  cout << -1;
}
```

## 큰 수 A + B
```C++
#include <iostream>
#include <string>
using namespace std;

int main()
{
  string n1,n2,result; // 수가 크기 때문에, 문자열로 입력받음
  cin >> n1 >> n2;
  int lift = 0;
  int size1=n1.size();
  int size2=n2.size();
  
  while(size1>0 || size2>0)
  {
    int char1 = 0;
    if(size1 > 0)
    {
      char1 = n1[--size1] - '0'; // char -> int
    }
    int char2 = 0;
    if(size2 > 0)
    {
      char2 = n2[--size2] - '0'; // char -> int
    }

    int add = char1 + char2 + lift;  
    lift = add/10;
    add %= 10;
    result += add + '0'; // int -> char
  }

  if(lift > 0)
    result += lift + '0'; // int -> char
  for(int i=result.length()-1; i>=0; i--)
    cout << result[i];
}
```

## Fly me to the Alpha Centauri
```C++
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  int t;
  cin >> t;
	
  for(int i=0; i<t; i++)
  {
    float x, y;
    cin >> x >> y;
    float len = y-x; // 두 지점 사이의 거리
    float n1 = sqrt(len); // 거리의 제곱근
    int n2 = round(sqrt(len)); // 거리의 제곱근을 반올림

    if(n1 <= n2) 
      cout << n2*2-1 << "\n"; 
	else 
      cout << n2*2 << "\n"; 
  }
}
```

## 소수 찾기
```C++
#include <iostream>
using namespace std;

int main()
{
  int t;
  int count, result = 0;
  cin >> t;

  int arr[t];

  for(int i=0; i<t; i++)
  {
    cin >> arr[i];

    for (int j=1; j<=arr[i]; j++)
    {
      if (arr[i]%j == 0)
        count++;
    }
    if (count == 2)
      result++;

    count = 0;
  }
  cout << result;
}
```

## 소인수분해
```C++
#include <iostream>
using namespace std;
 
int main() 
{
  int n;
  cin >> n;
 
  for (int i=2; i<=n; i++) 
  {
    while(n%i == 0) 
    {
      cout << i << "\n";
      n /= i;
    }
  }
}
```


## 소수 구하기
```C++
#include <iostream>
#include <cmath>

using namespace std;

int main() 
{
  int n, m, num;
  cin>> n >> m;
  for(int i=n; i<=m; i++)
  {
    // 에라토스테네스의 체
    //수의 제곱근까지만 나누어보는 방법
    // O(N*log(log(N)))
    num = sqrt(i);
    if(num == 1 && i != 1)
    {
      cout<<i<<'\n';
      continue;
    }
    if(i%2)
    {      
      for(int j=2; j<=num; j++)
      {
        if(!(i%j))
          break;
        if(j == num)
          cout<<i<<'\n';
      }
    }
  }
}
```


## 베르트랑 공준
```C++
#include <iostream>
#include <cmath>
using namespace std;

int main() 
{
  int n, root, count;  
  while(1)
  {
    int n, num;
    cin >> n;    
    if(!n)
      break;

    count = 0;
    
    for(int i=n+1; i<=n*2; i++)
    {
      num = sqrt(i);
      if(num == 1 && i != 1)
      {
        count++;
        continue;
      }
      if(i%2)
      {
        for(int j=2; j<=num; j++)
        {
          if(!(i%j))
            break;
          if(j == num)
          {
            count++;
          }
        }
      }
    }
    cout<< count << '\n';
  }  
}
```


## 골드바흐의 추측
```C++
#include <iostream>
#include <cmath>
using namespace std;

bool test(int i) 
{
  int num;
  num = sqrt(i);
  if (num == 1 && i != 1) 
  {
    return true;
  }
  if (i%2) 
  {
    for (int j=2; j<=num; j++) 
    {
      if (!(i%j))
        return false;
      if (j == num) 
        return true;
    }
  }
}

int main() 
{
  int t;
  cin >> t;

  for (int i=0; i<t; i++) 
  {
    int n;
    cin >> n;

    for (int j=n/2; j>=2; j--) 
    {
      if (test(j) && test(n-j)) 
      {
        cout << j << " " << n-j << '\n';
        break;
      }
    }
  }
}
```


## 직사각형에서 탈출
```C++
#include <iostream>
using namespace std;

int main() 
{
	int x, y, w, h;
	int result;
	cin >> x >> y >> w >> h;

	result = x;
	if (w-x < result)
		result = w-x;
	if (y < result)
		result = y;
	if (h-y < result)
		result = h-y;

	cout << result << '\n';
}
```


## 네 번째 점
```C++
#include <iostream>
using namespace std;

int main()
{
  int x1, x2, x3, y1, y2, y3;
  cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

  if(x1 == x2)
    cout << x3 << " ";
  else if(x1 == x3)
    cout << x2 << " ";
  else 
    cout << x1 << " ";

  if(y1 == y2)
    cout << y3;
  else if(y1 == y3)
    cout << y2;
  else 
    cout << y1;
}
```


## 직각삼각형
```C++
#include <iostream>
using namespace std;

int main() 
{
  while (1) 
  {
    int x, y, z;
    cin >> x >> y >> z;
    int num = 0;

    if (x == 0 && y == 0 && z == 0)
      return 0;

    if (x > y) 
    {
      num = y;
      y = x;
      x = num;
    }
    if (y > z) 
    {
      num = z;
      z = y;
      y = num;
	}

    if (z*z == x*x + y*y)
      cout << "right" << "\n";
    else
      cout << "wrong" << "\n";
  }
}
```


## 택시 기하학
```C++
#include <iostream>
#define PI 3.1415926535897932
using namespace std;

int main() 
{
  double r;
  cin >> r;

  cout << fixed;
  cout.precision(6);
  cout << r*r*PI << "\n" << 2*r*r << "\n";
}
```


## 터렛
```C++
#include <iostream>
using namespace std;

int main() 
{
  int x1, y1, r1, x2, y2, r2, d, d1, d2, t;
  cin >> t;

  for(int i=0; i<t; i++)
  {
    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
    d = (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2);
    d1 = (r1-r2) * (r1-r2);
    d2 = (r1+r2) * (r1+r2);
    if(d == 0)
    {
      if(d1 == 0)
        cout << "-1" << '\n';
      else
        cout << "0" << '\n';
    }
    else if (d == d1 || d == d2)
      cout << "1" << '\n';
    else if (d1 < d && d < d2)
      cout << "2" << '\n';
    else
      cout << "0" << '\n';
  }
}
```
