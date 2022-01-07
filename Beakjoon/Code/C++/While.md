# while 문

## A + B
```C++
#include <iostream>

using namespace std;

int main()
{
  int a, b;
    
  while(cin>>a>>b)
  {
    if(a!=0 || b!=0)
      cout<<a+b<<endl;
    else
      break;
  }
}
```

## 더하기 싸이클
```C++
#include <iostream>

using namespace std;

int main()
{
	int n, n1, n2, n3;
	int count = 1; 
	cin >> n;
	int num =n;

	while(1)
  {
		n1 = n/10; 
		n2 = n%10;
		n3 = n1 + n2;
		n = n2*10 + n3%10;
		if(num == n)
			break;
    else
			count++;
	}
	cout << count << "\n";
}
```
