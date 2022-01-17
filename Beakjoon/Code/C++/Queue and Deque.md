# 큐와 덱

## 큐 2
```C++
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int N, num;
string input;
queue <int> q;

int main() 
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;

  for (int i=0; i<N; i++) 
  {
    cin >> input;
    if (input.compare("push") == 0) 
    {
      cin >> num;
      q.push(num);
    }
    else if (input.compare("pop") == 0) 
    {
      if (q.empty())
        cout << -1 << '\n';
      else 
      {
        num = q.front();
        cout << num << '\n';
        q.pop();
      }
    }
    else if (input.compare("size") == 0)
      cout << q.size() << '\n';
    else if (input.compare("empty") == 0)
      cout << q.empty() << '\n';
    else if (input.compare("front") == 0) 
    {
      if (q.empty())
        cout << -1 << '\n';
      else
        cout << q.front() << '\n';
    }
    else if (input.compare("back") == 0) 
    {
      if (q.empty())
        cout << -1 << '\n';
      else
        cout << q.back() << '\n';
    }
  }
}

```

## 카드 2
```C++
#include <iostream>
#include <queue>
using namespace std;

int N;
queue<int> q;

void setting()
{
	cin >> N;
	for (int i=0; i<N; i++) 
    q.push(i+1);
}

void run()
{
	while (q.size() != 1) 
  {
		q.pop();
		q.push(q.front());
		q.pop();
	}
}

int main() 
{
  setting();
  run();
	cout << q.back();
}
```

## 오세푸스 문제 0
```C++
#include <iostream>
#include <queue>
using namespace std;
 
int N, K;
queue<int> q;

void setting()
{
  cin >> N >> K;
  for (int i = 1; i <= N; i++)
    q.push(i);
}

void run()
{
  cout << "<";
  int count = 1;
  while (!q.empty()) 
  {
    if (count % K == 0) 
    {
      int ans = q.front();
      q.pop();
      if (q.empty()) 
        cout << ans << ">";
      else
        cout << ans << ", ";
    }
    else 
    {
      int num = q.front();
      q.pop();
      q.push(num);
    }
    count++;
  }
}

int main() 
{
  setting();
  run();
}
```

## 프린터 큐
```C++
#include <iostream>
#include <queue>
using namespace std;

int T, N, M, num, count;

void setting()
{
  cin >> T;
}

void run()
{
  for (int i=0; i<T; ++i) 
  {
    count = 0;
    cin >> N >> M;
    queue<pair<int, int>> q;
    priority_queue<int> pq;
    for (int j=0; j<N; ++j) 
    {
      cin >> num;
      q.push({j, num});
      pq.push(num);
    }
    while (!q.empty()) 
    {
      int index = q.front().first;
      int value = q.front().second;
      q.pop();
      if (pq.top() == value) 
      {
        pq.pop();
        ++count;
        if (index == M) 
        {
          cout << count << "\n";
          break;
        }
      }
      else q.push({index,value});
    }
  }  
}

int main() 
{
  setting();
  run();
}
```

## 덱
```C++
#include<iostream>
#include<deque>
using namespace std;

int N, num;
string str;
deque<int> d;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N;
}

void run()
{
	for(int i=0; i<N; i++)
  {
		cin >> str;
		if (str == "push_front") 
    {
			cin >> num;
			d.push_front(num);
		}
		else if (str == "push_back") 
    {
			cin >> num;
			d.push_back(num);
		}
		else if (str == "pop_front") 
    {
			if (d.empty())
				cout << -1 << '\n';
			else 
      {
				cout << d.front() << '\n';
				d.pop_front();
			}
		}
		else if (str == "pop_back") 
    {
			if (d.empty())
				cout << -1 << '\n';
			else 
      {
				cout << d.back() << '\n';
				d.pop_back();
			}
		}
		else if (str == "size")
			cout << d.size() << '\n';
		else if (str == "empty") 
    {
			if (d.empty())
				cout << 1 << '\n';
			else
				cout << 0 << '\n';
		}
		else if (str == "front") 
    {
			if (d.empty())
				cout << -1 << '\n';
			else
				cout << d.front() << '\n';
		}

		else if (str == "back") 
    {
			if (d.empty())
				cout << -1 << '\n';
			else
				cout << d.back() << '\n';
		}
	}
}

int main() 
{
  setting();
  run();
}
```

## 회전하는 큐
```C++
#include <iostream>
#include <deque>
#include <vector>
using namespace std;

int N, M, cnt;
deque<int> d;

void setting()
{
  cin >> N >> M;
  for (int i = 1; i <= N; ++i)
    d.push_back(i);
}

void run()
{
  for (int i = 0; i < M; ++i) 
  {
    int num;
    cin >> num;
    int index;
    
    for (int i = 0; i < d.size(); ++i) 
    {
      if (d[i] == num) 
      {
        index = i;
        break;
      }
    }
    
    if (index < d.size() - index) 
    {
      for (;;) 
      {
        if (d.front() == num) 
        {
          d.pop_front();
          break;
        }
        ++cnt;
        d.push_back(d.front());
        d.pop_front();
      }
    }
    else 
    {
      for (;;) 
      {
        if (d.front() == num) 
        {
          d.pop_front();
          break;
        }
        ++cnt;
        d.push_front(d.back());
        d.pop_back();
      }
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

## AC
```C++
#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
using namespace std;

int T, N;
string str, arr;
deque<int> d;


void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> T;
}

void check()
{
  bool error = true;
  bool reverse = true;

  for (int i=0; i<str.length(); i++)
  {
    if (str[i] == 'R')
      reverse = !reverse;
    else
    {
      if (d.empty())
      {
        error = false;
        cout << "error" << "\n";
        break;
      }
      else
      {
        if (reverse)
          d.pop_front();
        else
          d.pop_back();
      }
    }           
  }
    
    if (error)
    {
      if (reverse)
      {
        cout << "[";
        while (!d.empty())
        {
          cout << d.front();
          d.pop_front();
          if (!d.empty())
            cout << ",";

        }
        cout << "]" <<"\n";
      }
      else
      {
        cout << "[";
        while (!d.empty())
        {
          cout << d.back();
          d.pop_back();
          if (!d.empty())
            cout << ",";
        }
        cout << "]" << "\n";
      }
    }
}

void run()
{
  for (int i=0; i<T; i++)
  {
    cin >> str >> N >> arr;
    string tmp;
    for (int i = 0; i < arr.length(); i++)
    {
      if (arr[i] == '[')  continue;
      else if ('0' <= arr[i] && arr[i] <= '9')
        tmp += arr[i];
      else if (arr[i] == ',' || arr[i] == ']')
      {
        if (!tmp.empty())
        {
          d.push_back(stoi(tmp));
          tmp.clear();
        }
      }
    }
    check();
  }
}

int main()
{
  setting();
  run();
}
```
