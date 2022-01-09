# 재귀

## 팩토리얼
```C++
#include <iostream>
using namespace std;

int factorial(int n) 
{
	if (n <= 1)
		return 1;
	else
		return n * factorial(n - 1);
}

int main() 
{
	int n;
	cin >> n;
	cout << factorial(n) << '\n';
}
```

## 피보나치 수 
```C++
#include <iostream>
using namespace std;

int fibonaci(int n) 
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return fibonaci(n - 1) + fibonaci(n - 2);
}

int main() 
{
	int n;
	cin >> n;
	cout << fibonaci(n) << '\n';
}
```

## 별 찍기
```C++
#include <iostream>
using namespace std;

void star(int i, int j, int num)
{
  if((i/num)%3 == 1 && (j/num)%3 == 1) 
    cout << ' ';
  else
  {
    if(num/3 == 0)
      cout << '*';
    else
      star(i, j, num/3);
  }
}

int main() 
{
  int n;
  cin >> n;
  for(int i=0; i<n; i++)
  {
    for(int j=0; j<n; j++)
      star(i, j, n);
    cout << '\n';
  }
}
```

## 하노이 탑 이동 순서
```C++
#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int start, int mid, int end, int n) 
{
	if (n == 1) 
		cout << start << " " << end<< "\n";
	else 
  {
		hanoi(start, end, mid, n - 1);
		cout << start << " " << end << "\n";
		hanoi(mid, start, end, n - 1);
	}
}

int main() 
{
	int n;
	cin >> n;
	cout << (int)pow(2, n) - 1 << '\n';
	hanoi(1, 2, 3, n);
}
```
