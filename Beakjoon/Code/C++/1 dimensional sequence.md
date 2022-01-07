# 1차원 배열

## 최대, 최소
```C++
#include <iostream>

using namespace std;

int main()
{
	int n;
	cin>>n;
	
	int list[n];
	int min = 1000000;
	int max = -1000000;
	
	for(int i=0; i<n; i++)
  {
		cin >> list[i];
		if(min > list[i])
    {
			min = list[i];
		}
		if(max < list[i])
    {
			max = list[i];
		}
	}
	
	cout << min << " " << max << "\n";
}
```

## 최댓값
```C++
#include <iostream>

using namespace std;

int main() 
{
	int num[9];
	int maxvalue = 0, maxindex = 0;

	for (int i = 0; i < 9; i++) 
  {
		cin >> num[i];
		if (maxvalue < num[i]) 
    {
			maxvalue = num[i];
			maxindex = i;
		}
	}
	cout << maxvalue << "\n" << maxindex + 1;
}
```

## 숫자의 개수
```C++
#include<iostream>

using namespace std;
 
int main()
{
    int a, b, c;
    int arr[10] = {0};
    
    cin >> a >> b >> c; 
    
    int num = a*b*c;
    
    while(num > 0)
    {
      arr[num % 10]++;
      num /= 10;
    }
    
    for(int i=0; i<10; i++)
      cout << arr[i] << "\n";
}
```

## 나머지
```C++
#include <iostream>

using namespace std;

int main() 
{
	int num;
	int arr[42] = {0};
	int count = 0;

	for (int i = 0; i < 10; i++) 
  {
		cin >> num;
		arr[num % 42]++;
	}

	for (int i = 0; i < 42; i++) 
  {
		if (arr[i] != 0)
			count++;
	}
	cout << count << "\n";
}
```

## 평균
```C++
#include <iostream>

using namespace std;

int main() 
{
	int n;
	int arr[1000];
	int max = 0;
	double result = 0;
	cin >> n;

	for (int i = 0; i < n; i++) 
  {
		cin >> arr[i];
		if (arr[i] > max)
			max = arr[i];
		result += arr[i];
	}
	result = (result / max * 100) / n;

	cout.precision(10);
	cout << result << "\n";
}
```

## OX퀴즈
```C++
#include <iostream> 

using namespace std; 

int main() 
{ 
  int n; 
  cin >> n;

  while(n--) 
  { 
    int score=0, result=0; 
    string s; 
    cin >> s; 
    
    for(int i=0; i<s.length(); i++) 
    {
      if(s[i]=='O') 
      { 
        score++; 
        result += score; 
      } 
    else 
      score=0; 
    }
    cout << result << "\n"; 
  } 
}
```

## 평균은 넘겠지
```C++
#include <iostream>

using namespace std;

int main() 
{
	int count, n, avg, num;
	int arr[1000] = {0};
	double result;

	cin >> count;
	for (int i = 0; i < count; i++) 
  {
		cin >> n;
    avg = 0;
		num = 0;

		for (int j = 0; j < n; j++) 
    {
			cin >> arr[j];
			avg = avg + arr[j];
		}
		avg = avg / n;

		for (int j = 0; j < n; j++) 
    {
			if (arr[j] > avg)
				num++;
		}
		result = (double)num / n * 100;

    cout << fixed;
		cout.precision(3);
		cout << result << "%" << "\n";
	}
}
```
