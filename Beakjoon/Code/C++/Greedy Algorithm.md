# 그리디 알고리즘

## 동전 0
```C++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, k, result = 0;
vector<int> v(10);

int cmp(int a, int b) 
{
	return a > b;
}

void setting()
{
  cin >> n >> k;
	for(int i=0; i<n; i++) 
		cin >> v[i];
}

void run()
{
  sort(v.begin(), v.end(), cmp);
	for (int i = 0; i < n; i++) 
  {
		while (k - v[i] >= 0) 
    {
			result++;
			k -= v[i];
		}
	}
}

int main() 
{	
	setting();
  run();
  cout << result << '\n';
}
```

## 회의실 배정
```C++
#include <iostream> 
#include <vector> 
#include <algorithm> 
using namespace std; 

int N; 
int cnt=1; 
vector<pair<int,int>> v; 

bool compare(pair<int,int> a,pair<int,int> b) 
{ 
  if(a.second == b.second) 
    return a.first < b.first;
  else 
    return a.second <b.second; 
} 

void setting()
{
  cin>> N; 
  for(int i=0;i<N;i++) 
  { 
    int x,y; 
    cin >> x>>y; 
    v.push_back({x,y}); 
  } 
}

void run()
{
  sort(v.begin(), v.end(), compare); 
  int now = v[0].second; 
  for (int i=1;i<N;i++) 
  { 
    if (now <=v[i].first) 
    { 
      cnt++; 
      now=v[i].second; 
    } 
  } 
}

int main() 
{ 
  setting();
  run();
  cout << cnt; 
}
```

## ATM
```C++
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1000;

int N, ans;
int person[1000];
void setting()
{
  cin >> N;
  for(int i=0; i<N; i++)
    cin >> person[i];
}

void run()
{
  sort(person, person + N);

  for(int i=0; i<N; i++)
    for(int j=0; j<=i; j++)
      ans += person[j];
}

int main()
{
  setting();
  run();
  cout << ans;
}
```

## 잃어버린 괄호
```C++
#include <iostream>
#include <string>
using namespace std;

string N, num;
int ans;
bool check;

void setting()
{
  cin >> N;
}

void run()
{
  for (int i = 0; i <= N.size(); i++) 
  {      
    if(N[i] == '-' || N[i] == '+' || i==N.size()) 
    {
      if (check) 
      {
        ans -= stoi(num);
        num = "";
      }
      else 
      {
        ans += stoi(num);
        num = "";
      }
    }
    else
      num += N[i];
 
    if(N[i] == '-')
      check = true;    
  }  
}

int main() 
{
  setting();
  run();
  cout << ans;
}
```

## 주유소
```C++
#include <iostream>
using namespace std;

int n;
pair<long long,long long> input[100000];
long long ans;

void setting()
{
	cin >> n;
	for (int i = 0; i < n - 1; i++)
		cin >> input[i].first;
	for (int i = 0; i < n; i++)
		cin >> input[i].second;
}

void run()
{
	int i = 0;
	ans = input[i].first * input[i].second;
	for (int j=1; j<n; j++) 
  {
		if (input[i].second > input[j].second)
			i = j;
		ans += input[j].first * input[i].second;
	}
}

int main() 
{
  setting();
  run();
	cout << ans;
}
```
