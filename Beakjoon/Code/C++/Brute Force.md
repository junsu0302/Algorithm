# 부르트 포스

## 블랙잭
```C++
#include <iostream>
using namespace std;
 
int main() 
{
  int N, M;
  int arr[100];
  int sum = 0;
  int result = 0;
  cin >> N >> M;
    
  for(int i=0; i<N; i++)
    cin >> arr[i];
    
  for(int i=0; i<N-2; i++)
  {
    for(int j=i+1; j<N-1; j++)
    {
      for(int k=j+1; k<N; k++)
      {
        sum = arr[i] + arr[j] + arr[k];
        if(sum<=M && M-sum < M-result)
          result = sum;
      }
    }
  }
  cout << result << '\n';
}
```

## 분해합
```C++
#include <iostream>
using namespace std;

int function(int n) 
{
	int sum = n;
	while (n) 
  {
		sum = sum + n % 10;
		n /= 10;
	}
	return sum;
}

int main() 
{
	int N;
	cin >> N;

	for (int i = 1; i < N; i++) 
  {
		int sum = function(i);
		if (sum == N)
    { 
			cout << i;
      return 0;
    }
  }
	cout << 0;
}
```

## 덩치
```C++
#include <iostream>
using namespace std;

int main() 
{
	int N;
	int arr[51][2] = {0};
	int result[51];
	cin >> N;
	
  for(int i=0; i<N; i++) 
  {
		cin >> arr[i][0] >> arr[i][1];
		result[i] = 1;
	}

	for(int i=0; i<N; i++) 
  {
		for(int j=0; j<N; j++) 
    {
			if(arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1])
				result[i]++;
		}
	}

	for(int i=0; i<N; i++)
		cout << result[i] << " ";
	cout << '\n';
}
```

## 체스판 다시 칠하기
```C++
#include <iostream>
#include <string>

using namespace std;

int main() 
{
	int n, m,count, result;
	cin >> n >> m;

	char chess[n][m];
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			cin >> chess[i][j];

	for(int x=0; x+7<n; x++) 
  {
		for(int y=0; y+7<m; y++) 
    {
			count = 0;
			for(int i=x; i<x+8; i++) 
      {
				for(int j=y; j<y+8; j++) 
        {
					if((i+j)%2 == 0) 
          {
						if(chess[i][j] != 'B') 
							count++;
					}
					else 
          {
						if(chess[i][j] != 'W') 
							count++;
					}
					if(count > result) 
            break;
				}
			}
			if(count < result) 
        result = count;
		}
	}

	for(int x=0; x+7<n; x++) 
  {
		for(int y=0; y+7 < m; y++) 
    {
			count = 0;
			for(int i=x; i<x+8; i++) 
      {
				for(int j=y; j<y+8; j++) 
        {
					if((i+j)%2 == 0) 
          {
						if(chess[i][j] != 'W') 
							count++;
					}
					else 
          {
						if(chess[i][j] != 'B')
							count++;
					}
					if(count > result) 
            break;
				}
			}
			if(count < result) 
        result = count;
		}
	}
	cout << result;
}
```

## 영화감독 숌
```C++
#include<iostream>
using namespace std;

int main()
{
	int N, num, count, result;
	cin >> N;

	count = 0;
  result = 0;

	while(count != N)
	{
		result++;
		num = result;

		while(num != 0)
		{
			if (num%1000 == 666) 
			{
				count++;
				break;
			}
			else 
        num /= 10;
		}
	}
	cout << result;
}
```
