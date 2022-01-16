# 

## 스택
```C++
#include <iostream>
#include <stack>
#include <string>
using namespace std;

struct Stack 
{
  int data[10000];
  int size;
    
  Stack() 
  {
    size = 0;
  }
    
  void push(int num) 
  {
    data[size] = num;
    size += 1;
  }
    
  bool empty() 
  {
    if (size == 0)   return true;
    else   return false;
  }
    
  int pop() 
  {
    if (empty())   return -1;
    else 
    {
      size -= 1;
      return data[size];
    }
  }
    
  int top() 
  {
    if (empty())   return -1;
    else   return data[size-1];
  }
};

int n;
Stack s;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n;
}

void run()
{
  for(int i=0; i<n; i++)
  {
    string input;
    cin >> input;
        
    if (input == "push") 
    {
      int num;
      cin >> num;
      s.push(num);
    } 
    else if (input == "top") 
      cout << (s.empty() ? -1 : s.top()) << '\n';
    else if (input == "size") 
      cout << s.size << '\n';
    else if (input == "empty") 
      cout << s.empty() << '\n';
    else if (input == "pop") 
    {
      cout << (s.empty() ? -1 : s.top()) << '\n';
      if (!s.empty()) 
        s.pop();
    }
  }
}

int main() 
{
  setting();
  run();
}
```

## 제로
```C++
#include <iostream>
#include <stack>
using namespace std;

int K, N;
int sum = 0;
stack<int> s;

void setting()
{
  cin >> K;
  for (int i = 0; i < K; i++) 
  {
    cin >> N;
    if (N != 0)
      s.push(N);
    else
      s.pop();
  }
}

void run()
{
  int size = s.size();
  for (int i = 0; i < size; i++) 
  {
    sum += s.top();
    s.pop();
  }
}

int main() 
{
  setting();
  run();
  cout << sum;
}
```

## 괄호
```C++
#include <iostream>
#include <string>
#include <stack>
using namespace std;

int T;
string N;

void setting()
{
  cin >> T;
}

void run() 
{
	for(int i=0; i<T; i++)
  {
		cin >> N;
    stack<char> s;
    string ans = "YES";
		for (int i = 0; i < N.length(); i++) 
    {
			if (N[i] == '(')
				s.push(N[i]);
			else if(!s.empty() && N[i] == ')' && s.top() == '(')
				s.pop();
			else 
      {
				ans = "NO";
				break;
			}
		}
		if(!s.empty()) 
      ans = "NO";

		cout << ans << "\n";
	}
}

int main()
{
  setting();
  run();
}
```

## 균형잡힌 세상
```C++
#include <iostream>
#include <string>
#include <stack>
using namespace std;
 
int main() 
{
  while (1)
  {
    string input;
    getline(cin, input);
 
    if (input == ".")
      break;
 
    stack<char> s;
    bool check = 0;

    for(int i = 0; i < input.length(); i++) 
    {
      char c = input[i];
                
      if((c == '(') || (c == '[')) 
        s.push(c);
      else if(c == ')') 
      {
        if(!s.empty() && s.top() == '(') 
          s.pop();
        else 
        {
          check = 1;
          break;
        }
      }
      else if(c == ']') 
      {
        if(!s.empty() && s.top() == '[') 
          s.pop();
        else 
        {
          check = 1;
            break;
        }
      }
    }
 
    if(check==0 && s.empty()) 
      cout << "yes" << "\n";
    else 
      cout << "no" << "\n"; 
  }
}
```

## 스택 수열
```C++
#include <iostream>
#include <stack>
using namespace std;

int T, N;
int cnt = 1;
stack<int> s;
string op;

void setting()
{
  cin >> T;
}

int main()
{
  setting();

  for(int i=0; i<T; i++)
  {
    cin >> N;

    if (cnt <= N)
    {
      while (cnt <= N)
      {
        s.push(cnt);
        op += '+';
        cnt++;
      }
      s.pop();
      op += '-';
    }
    else
    {
      if (s.top() < N)
      {
        cout << "NO";
        return 0;
      }
      else
      {
        s.pop();
        op += '-';
      }
    }
  }
  for (int j = 0; j < op.length(); j++)
    cout << op[j] << "\n";
}

```

## 오큰수
```C++
#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;

int N;
stack<int> s;
int ans[1000001];
int arr[1000001];

void setting()
{
	cin >> N;
	for (int i=0; i<N; i++)
		cin >> arr[i];
}

void run()
{
	for (int i=N-1; i>=0; i--)
	{
		while(!s.empty() && s.top() <= arr[i])
			s.pop();

		if (s.empty()) 
      ans[i] = -1;
		else 
      ans[i] = s.top();

		s.push(arr[i]);
	}
}

int main()
{
  setting();
  run();
	for (int i=0; i<N; i++)
		cout << ans[i] << " ";
}

```
