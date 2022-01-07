## 입출력과 사칙연산

### Hello word!
```C++
#include <iostream>

int main() 
{
  std::cout << "Hello World!";
} 
// 띄어쓰기 \n
// 특수문자 출력 시 '\', 수식 출력 시 '%%' 사용
```

### A+B, A-B, A\*B
```C++
#include <iostream>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    cout << a+b;    
}
```

### A/B
```C++
#include <iostream>

using namespace std;

int main()
{
    double a,b;
    
    while(1)
    {    
        cin >> a >> b;        
        if(b != 0) // 나누는 값이 0이 아니어야함
            break;
        else
            continue;
    }
    
    cout.precision(10); // 정수포함 10번째 자리수까지
    cout << a/b;    
}
```

### 사칙연산
```C++
#include <iostream>

using namespace std;

int main()
{
    int a,b;
    
    while(1)
    {    
        cin >> a >> b;        
        if(1 <= a && b <= 10000 && b != 0)
            break;
        else
            continue;
    }
    
    cout<<a+b<<endl;
    cout<<a-b<<endl;
    cout<<a*b<<endl;
    cout<<a/b<<endl;
    cout<<a%b<<endl;     
}
```

### 곱셈
```C++
#include <iostream>

using namespace std;

int main()
{
	int a, b;

  while(1)
  {
    cin >> a >> b;
    
    if(a < 1000 && b < 1000 && b != 0)
      break;
    else
      continue;
  }

	cout << a * (b % 10) << '\n';
	cout << a*((b / 10)%10) << '\n';
	cout << a * (b / 100) << '\n';
	cout << a * b << '\n';
}
```
