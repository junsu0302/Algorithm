# 이분 탐색

## 수 찾기
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int arr[100000];

void binarySearch(int check)
{
  int start = 0;
  int end = N-1;
  int mid;

  while(end>=start)
  {
    mid =(start+end)/2;
    if(arr[mid] == check)
    {
      cout << 1 << "\n";
      return;
    }
    else if(arr[mid] > check)
      end = mid - 1;
    else
      start = mid + 1;
  }
  cout << 0 << "\n";
  return;
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  int tmp;

  for(int i=0;i<N;i++)
  {
      cin >> tmp;
      arr[i]=tmp;
  }
  sort(arr,arr+N);

}

void run()
{
  cin>>M;
  int tmp;
  for(int i=0;i<M;i++)
  {
    cin >> tmp;
    binarySearch(tmp);
  }
}

int main()
{
  setting();
  run();
}
```

## 숫자 카드
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	int N, M;
	
	cin >> N;
	vector<int>card(N, 0);

	for (int i = 0; i < N; ++i)
		cin >> card[i];

	cin >> M;
	sort(card.begin(), card.end());

	int num = 0;
	for (int i = 0; i < M; ++i) 
  {
		cin >> num;
		cout << upper_bound(card.begin(), card.end(), num)
			- lower_bound(card.begin(), card.end(), num) << " ";
	}		
}
```

## 랜선 자르기
```C++
#include<iostream>
using namespace std;

int K, N, ans;
int line[10000];
int MAX = 0;
long long mid, high, low;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> K >> N;
	
	for (int i = 0; i < K; i++)
	{
		cin >> line[i];
		if (MAX < line[i]) 
      MAX = line[i];
	}
	low = 1;
	high = MAX;
}

void run()
{
	while (low <= high)
	{
		mid = (low + high) / 2;
		int cnt = 0;
		for (int i = 0; i < K; i++)
			cnt += line[i] / mid;

		if (cnt >= N) 
    {
			low = mid + 1;
			if (ans < mid) 
        ans = mid;
		}
		else 
			high = mid - 1;
	}
}

void print()
{
	cout << ans;
}

int main()
{
  setting();
  run();
  print();
}

```

## 나무 자르기
```C++
#include <iostream>
using namespace std;

int N;
long long M;
long long trees[1000000];

bool check(int height) 
{
	int num = 0;
	for (int i = 0; i < N; i++) 
  {
		if (trees[i] >= height)
			num += (trees[i] - height);
		if (num >= M) return true;
	}
	return false;
}

void setting()
{
	ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> N >> M;
	for (int i = 0; i < N; i++)
		cin >> trees[i];
}

int run() 
{
	int left = 0, right = 1000000000;
	int mid, num;
	while (left <= right) 
  {
		mid = (left + right) / 2;
		if (check(mid)) 
    {
			num = mid;
			left = mid + 1;
		}
		else
			right = mid - 1;
	}
	return num;
}

int main() 
{
  setting();
	cout << run();
}
```

## 공유기 설치
```C++
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 200000;
int N, C, ans;
int house[MAX];

bool possible(int dist)
{
  int cnt = 1;
  int prev = house[0];

  for(int i=1; i<N; i++)
  {
    if (house[i] - prev >= dist)
    {
      cnt++;
      prev = house[i];
    }
  }

  if (cnt >= C)
    return true;
  return false;
}

void setting()
{
  cin >> N >> C;

  for (int i = 0; i < N; i++)
    cin >> house[i];

  sort(house, house + N);
}

void run()
{
  int low = 1, high = house[N - 1] - house[0];

  while (low <= high)
  {
    int mid = (low + high) / 2;

    if (possible(mid))
    {
      ans = max(ans, mid);
      low = mid + 1;
    }
    else
      high = mid - 1;
  }
}

void print()
{
  cout << ans;
}

int main()
{
  setting();
  run();
  print();
}
```

## K번째 수
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K, ans;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;
}

void run()
{
  int low = 1, high = K;

  while (low <= high)
  {
    int cnt = 0;
    int mid = (low + high) / 2;

    for (int i = 1; i <= N; i++)
      cnt += min(mid / i, N);

    if (cnt < K)
      low = mid + 1;
    else
    {
      ans = mid;
      high = mid - 1;
    }
  }
}

void print()
{
  cout << ans;
}

int main()
{
  setting();
  run();
  print();
}

```

## 가장 긴 증가하는 부분 수열
```C++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
 
int n;
vector<int> v;
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n;
  v.push_back(0);
}

void run()
{
  int num;
  for (int i = 0; i < n; i++) 
  {
    cin >> num;
    if (num > v.back()) 
        v.push_back(num);
    else 
    {
      int index = lower_bound(v.begin(), v.end(), num) - v.begin();
      v[index] = num;
    }
  }
}

void print()
{
  cout << v.size() - 1;
}

int main() 
{
  setting();
  run();
  print();
}
```
