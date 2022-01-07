# 함수

## 정수 N개의 합
```C++
#include <iostream>
#include <vector>
using namespace std;

long long sum(vector<int>& a) 
{
  long long  result = 0;
  for(int i = 0; i < a.size(); i++) 
    result += a[i];
  return result;
}
```

## 셀프 넘버
```C++
#include <iostream>
using namespace std;

int main() 
{
	int arr[10000] = {0};
  int n;

	for (int i = 0; i < 10000; i++) 
  {
		if (i < 10)
			arr[i + i] = 1;
		else if (i < 100)
			arr[i + i / 10 + i % 10] = 1;
		else if (i < 1000)
			arr[i + i / 100 + i % 100 / 10 + i % 10] = 1;
		else if (i < 10000)
    {
			n = i + i / 1000 + i % 1000 / 100 + i % 100 / 10 + i % 10;
			if (n < 10000)
				arr[n] = 1;
    // 런타임에러 : 정해진 배열의 index값 이상을 참조하는 경우
    // arr[i + i / 1000 + i % 1000 / 100 + i % 100 / 10 + i % 10] = 1;은 런타임에러 발생
    // index 최댓값이 10000이기 때문에 10000을 넘기지 못하게 if문 추가
    }
  }
	for (int i = 1; i < 10000; i++) 
  {
		if (arr[i] == 0)
			cout << i << "\n";
	}
}
```

## 한수
```C++
#include <iostream>
using namespace std;

int main(void)
{
  int n = 0;
  cin >> n;

  if(n < 100)
    cout << n;
  else
  {
    int count = 99;
    for(int i=100; i <= n; i++)
    {
      int n1, n2, n3;
      n1 = i % 10;
      n2 = i / 10 % 10;
      n3 = i / 100;
      if(n3-n2 == n2-n1)
        count++;
    }
    cout << count;
  }
}
```
