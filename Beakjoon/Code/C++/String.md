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
#include <iostream>
#include <string>
using namespace std;

int main() 
{
	string a, b;
	cin >> a >> b;

	string s;

	for (int i = 2; i >= 0; i--) 
  {
		if (a[i] > b[i]) 
    {
			s = a; 
      break;
		}
		else if (a[i] < b[i]) 
    {
			s = b; 
      break;
		}
	}
	cout << s[2] << s[1] << s[0];
}
```

## 다이얼
```C++
#include <iostream>
#include <string>

using namespace std;

int main() 
{
	string s;
	cin >> s;
	int n = 0;

	for (int i = 0; i < s.length(); i++) 
  {
		if (s.at(i) >= 'A' && s.at(i) <= 'C')
			n += 3;
		else if (s.at(i) >= 'D' && s.at(i) <= 'F')
			n += 4;
		else if (s.at(i) >= 'G' && s.at(i) <= 'I')
			n += 5;
		else if (s.at(i) >= 'J' && s.at(i) <= 'L')
			n += 6;
		else if (s.at(i) >= 'M' && s.at(i) <= 'O')
			n += 7;
		else if (s.at(i) >= 'P' && s.at(i) <= 'S')
			n += 8;
		else if (s.at(i) >= 'T' && s.at(i) <= 'V')
			n += 9;
		else if (s.at(i) >= 'W' && s.at(i) <= 'Z')
			n += 10;
	}
  cout << n;
}
```

## 크로아티아 알파벳
```C++
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() 
{
  vector<string> v = {"c=","c-","dz=","d-","lj","nj","s=","z="};
  int idx;
  string s;
  cin >> s;

  for(int i = 0; i < v.size(); i++)
  {
    while(1)
    {
      if(s.find(v[i]) == string::npos)
        break;
      s.replace(s.find(v[i]), v[i].length(), "a");
    }
  }
  cout << s.length();
}
```

## 그룹 단어 체커
```C++
#include <iostream>
using namespace std;

int main()
{	
	int n;
	int count = 0;
	string s;
	cin >> n;

	for(int i=0; i<n; i++)
  {
		cin >> s;
		bool check = true;
		
		for(int j=0; j<s.length(); j++)
    {
			for(int k=0; k<j; k++)
      {
				if(s[j] != s[j-1] && s[j] == s[k])
        {
					check = false;
					break;			
				}				
			}
		}
		if(check) count++;
	}
	cout << count;
}
```
