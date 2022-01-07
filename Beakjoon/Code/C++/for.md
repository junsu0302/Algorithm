# for문

## 구구단
```C++
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    
    for(int i=1; i<=9; i++)
    {
        cout<<n<<" * "<<i<<" = "<<n*i<<'\n';
    }
}
```

## A+B 3
```C++
#include <iostream>

using namespace std;

int main()
{
    int n, a, b;
    cin>>n;

    for(int i = 0; i < n; i++)
    {
        cin >> a >> b;
        cout << a+b <<endl;
    }
}
```

## 합
```C++
#include<iostream>
 
using namespace std;
 
int main()
{
  int n;
  int sum = 0;
 
  cin >> n;
 
  for (int i = 1; i <= n; i++)
  {
      sum += i;
  }
  cout << sum;
}
```

## 빠른 A+B
[참고자료](https://www.acmicpc.net/board/view/22716)
```C++
#include <iostream> 

using namespace std; 

int main() 
{ 
  cin.tie(NULL); 
  ios::sync_with_stdio(false); 
  // 빠른 입출력 지원
  // 단 cin, cout만 사용 가능

  int k; 
  cin >> k; 
  
  for (int i = 0; i < k; i++) 
  { 
    int A, B; 
    cin >> A >> B; 
    cout << A + B << '\n'; 
  } 
}
```

## N 찍기
```C++
#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;
    
  for(int i = 1; i <= n; i++)
  {
      cout << i << '\n'; // cout << i << endl의 빠른 버전
      // endl은 띄어쓰기를 진행하면서 버퍼를 초기화하기 때문에 시간이 오래걸림
      // \n은 띄어쓰기만 하기 때문에 훨씬 빠름
  }
}
```

## 별 찍기 1
```C++
#include <iostream> 

using namespace std; 

int main() 
{ 
  int n;
  cin >> n;
  
  for (int i = 0; i < n; i++)
  { 
    for (int j = 0; j < i+1; j++)
      cout << "*"; 
    cout << "\n";
  }
}
```

## 별 찍기 2
```C++
#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) 
  {
		for (int j = 0; j < n - i; j++)
			cout << " ";
		for (int j = 0; j < i; j++)
			cout << "*";
		cout << '\n';
	}
}
```

## X보다 작은 수
```C++
#include <iostream>

using namespace std;

int main()
{
  int N, X;
  cin >> N >> X;    
  int arr[N];

  for(int i=0; i<N; i++)
    cin>>arr[i];

  for(int j = 0; j < N; j++)
  	if(arr[j] < X)
      cout<<arr[j]<<" ";
}
```
