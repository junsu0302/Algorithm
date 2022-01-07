# If 문

## 두 수 비교하기
```C++
#include <iostream>

using namespace std;

int main() 
{
  int a, b;

  while(1)
  {
    cin >> a >> b;
  
    if(-10000<a&&a<10000&&-10000<b&&b<10000) // -10000 < a,b < 10000
      break;
    else
      continue;
  }
	if (a > b)
		cout << ">";
	else if (a < b)
		cout << "<";
	else
		cout << "==";
}
```

## 시험성적
```C++
#include <iostream>

using namespace std;

int main() 
{
    int a;
    cin>>a;
    
    if(a >= 90 && a <= 100)
        cout<<"A";
    else if(a >= 80 && a < 90)
        cout<<"B";
    else if(a >= 70 && a < 80)
        cout<<"C";
    else if(a >= 60 && a < 70)
        cout<<"D";
    else
        cout<<"F";    
}
```

## 윤년
```C++
#include <iostream>

using namespace std;

int main()
{
    int a;
    cin>>a;

    if(a % 400 == 0)
      cout << 1;
    else
      if(a % 4 == 0 && a % 100 != 0)
            cout<<1;
        else
            cout<<0;
}
```

## 사분면 고르기
```C++
#include <iostream>

using namespace std;

int main()
{
  int x, y;
  cin >> x >> y;

  if(x > 0)
    if(y > 0)
      cout<<1;
    else
      cout<<4;
  else
    if(y > 0)
      cout<<2;
    else
      cout<<3;      
}
```

## 알람 시계
```C++
#include <iostream>

using namespace std;

int main()
{
  int h, m;
  
  while(1)
  {
    cin >> h >> m;
  
    if(0<=h&&h<=23&&0<=m&&m<=59)
      break;
    else
      continue;
  }
  
  if(m < 45)
  {
    m += 15;
    h--;
  }
  else
    m -= 45;
  if(h < 0)
    h = 23;

  cout << h << " "<< m;
}
```
