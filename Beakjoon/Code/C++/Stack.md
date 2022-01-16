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

```

## 괄호
```C++

```

## 균형잡힌 세상
```C++

```

## 스택 수열
```C++

```

## 오큰수
```C++

```
