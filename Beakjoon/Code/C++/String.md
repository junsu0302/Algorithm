# 문자열

## 아스키코드
```C++
#include <iostream> 
using namespace std; 

int main() 
{ 
  char c; 
  cin >> c; 
  cout << (int)c;
}
```

## 숫자의 합
```C++
#include<iostream>
using namespace std;
 
int main()
{
  int n;
  int sum = 0;
  char c;
 
  cin >> n;
 
  for (int i=0; i<n; i++)
  {
    cin >> c;
    sum += (int)c - 48; // 아스키 코드상 0 -> 48
  }
  cout << sum;
}
```

## 알파벳 찾기
```C++
#include <iostream>
#include <string>
using namespace std;
 
int main() 
{
  string s;
  cin >> s;
  int result = 0;

  for (char a = 'a'; a <= 'z'; a++) 
  {
    result = s.find(a);
    // string.find(char) -> 문자열에서 해당 문자 개수 출력
    cout << result << " ";
  }
}

```

## 문자열 반복
```C++
#include <iostream>
#include <string>
using namespace std;
 
int main()
{
  int n;
  cin >> n;

  for(int i=0; i<n; i++)
  {
    int num;
    string s;
    cin >> num;
    cin >> s;
 
    for(int j=0; j<s.length(); j++)
    {
      for(int k=0; k<num; k++)
      {
        cout << s[j];
      }
    }
    cout << "\n";
  }
}
```

## 단어 공부
```C++
#include <iostream> 
using namespace std; 

int arr[26], count =0; 
string s; //아스키코드 : 대문자 65~90, 소문자 97~122 

int main() 
{ 
  cin >> s;
  for(int i=0; i<s.length(); i++) 
  { 
    if(s[i]<97)
      arr[(int)s[i] - 65]++;
    else
      arr[(int)s[i] - 97]++;
  } 

  int max = 0, idx=0; 
  for(int i=0; i<26; i++) 
  { 
    if(max < arr[i]) 
    { 
      max = arr[i]; 
      idx = i; 
    } 
  }
  for(int i=0; i<26; i++) 
  { 
    if(max == arr[i]) 
      count++; 
  }
  if(count > 1) 
    cout << "?"; 
  else 
    cout << (char)(idx+65); 
}

```

## 단어의 개수
```C++
#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string s;
    getline(cin, s); // 라인 전체를 저장
    int count = 1;

    for(int i=0; i<s.length(); i++)
    {
      if(s[i] == ' ')
        count++;
    }
    if(s[0] == ' ')
        count--;
    if(s[s.length()-1] == ' ')
        count--;

    cout << count;
}
```

## 상수
```C++

```

## 다이얼
```C++

```

## 크로아티아 알파벳
```C++

```

## 그룹 단어 체커
```C++

```
