# 우선순위 큐

## 최대 힙
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int N;
priority_queue<int> pq;
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run()
{
  for (int i = 0; i < N; i++)
  {
    int num;
    cin >> num;

    if (num == 0)
    {
      if (pq.empty())
        cout << 0 << "\n";
      else 
      {
        cout << pq.top() << "\n";
        pq.pop();
      }
    }
    else
      pq.push(num);
  }  
}

int main()
{
  setting();
  run();
}
```

## 최소 힙
```C++
#include<iostream>
#include<queue>
#include<functional> //greater 사용
using namespace std;
 
int N;
priority_queue<int, vector<int>, greater<int> > pq;
//<data tape, container type, 정렬 기준>

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run()
{
  int num;
  
  for (int i = 0;i < N;i++) 
  {
    cin >> num;
    if (num)
      pq.push(num);
    else 
    {
      if (pq.empty())
        cout << 0 << "\n";
      else 
      {
        cout << pq.top() << "\n";
        pq.pop();
      }      
    }
  }  
}

int main() 
{
  setting();
  run();
}
```

## 절댓값 힙
```C++
#include<iostream>
#include<queue>
#include<functional>
using namespace std;
 
int N;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run()
{
  int num;
  
  for (int i = 0;i < N;i++) 
  {
    cin >> num;
    if (num) 
    {
      pq.push({ abs(num), num });
    }
    else 
    {
      if (pq.empty())
        cout << 0 << "\n";
      else 
      {
        cout << pq.top().second << "\n";
        pq.pop();
      }
    }
  }
}

int main() 
{
  setting();
  run();
}
```

## 가운데를 말해요
```C++
#include<iostream>
#include<queue>
using namespace std;

int N, K;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run()
{
  priority_queue<int> max;
  priority_queue<int,vector<int>,greater<int>> min;

  for (int i=0; i<N; i++)
  {
    int size;
    cin >> K;
    if (max.size() == min.size()) 
      max.push(K);
    else
      min.push(K);
    
    if (!max.empty()&&!min.empty()&&max.top()>min.top()) 
    {
      int max_val, min_val;
      max_val = max.top();
      min_val = min.top();
      max.pop();
      min.pop();
      max.push(min_val);
      min.push(max_val);
    }
    cout << max.top() << '\n';
  }
}

int main() 
{
  setting();
  run();
}
```
