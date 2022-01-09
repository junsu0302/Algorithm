# 정렬

## 수 정렬하기 1
```C++
#include <iostream>
using namespace std;

int main()
{
  int N, num;
  cin >> N;
  int arr[N];
  for(int i=0; i<N; i++)
    cin>>arr[i];

  for(int j=0; j<N-1; j++)
  {
    for(int k=j+1; k<N; k++)
    {
      if(arr[j] > arr[k])
      {
        num = arr[k];
        arr[k] = arr[j];
        arr[j] = num;
      }
    }
  }

  for(int l=0; l<N; l++)
  {
    if(l+1 < N && arr[l] == arr[l+1])
      continue;
    cout << arr[l] << "\n";
  }
}
```

## 수 정렬하기 2
```C++
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

  int N;
  cin >> N;
  int arr[N];
  for (int i=0; i<N; i++)
    cin >> arr[i];

  sort(arr, arr+N); // algorithm의 정렬 함수

  for (int i=0; i<N; i++)
    cout << arr[i] << '\n';
}
```

## 수 정렬하기 3
```C++
#include <iostream>
using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N;
  cin >> N;
  int arr[10001] = {0};
  
  // 카운팅 정렬
  for(int i=0 ; i<N; i++)
  {
    int num;
    cin >> num;
    arr[num] += 1;
  }

  for(int i=1 ; i<=10000; i++)
  {
    for (int j=0; j<arr[i]; j++)
    {
      cout << i << "\n";
    }
  }
}
```

## 통계학 \*
```C++
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() 
{
  int N, num, mode, total = 0;
  int most = -1;
  int number[8001] = {0};
  bool Overlap = false;
  vector<int> arr;
  cin >> N;

  for(int i=0; i<N; i++)
  {
    cin >> num;
    arr.push_back(num);
    total += num;
    number[num+4000]++;
  }
  sort(arr.begin(),arr.end());

  for(int i=0; i<8001; i++)
  {
    if(number[i] == 0)
      continue;
    
    if(number[i] == most)
    {
      if(Overlap)
      {
        mode = i - 4000;
        Overlap = false;
      }
    }

    if(number[i] > most)
    {
      most = number[i];
      mode = i - 4000;
      Overlap = true;
    }
  }
  cout << round((float)total/N) << "\n"; // 산술평균
  cout << arr[arr.size()/2] << "\n"; // 중앙값
  cout << mode << "\n"; // 최빈값(중복 시 두 번째로 작은 값)
  cout << arr.back() - arr.front(); // 범위
}
```

## 소트인사이드
```C++
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
  string N;
  cin >> N;
  sort(N.begin(), N.end(), greater<char>()); // 내림차순
  cout << N;
}
```

## 좌표 정렬하기 1
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
  int N;
  cin >> N;
  vector<vector<int>> arr(N, vector<int>(2,0));
  // 2차원 벡터 정렬
  // vector<vector<int>> arr(N, vector<int>(M,0));
  // N*M 사이즈 벡터를 0으로 초기화
  
  for(int i=0; i<N; i++)
  {
    cin>>arr[i][0];
    cin>>arr[i][1];
  }
  sort(arr.begin(), arr.end());

  for(int j=0; j<arr.size(); j++)
    cout << arr[j][0] << " " << arr[j][1] << '\n';
}

```

## 단어 정렬
```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(string a, string b) 
{
  int i = 0;
  if(a.length() == b.length())
  {
    for(int i=0; i<a.length(); i++)
    {
      if(a[i] != b[i])
        return a[i] < b[i];
    }
  }
  return a.length() < b.length();
}

int main() 
{
  int N;
  string str;
  cin >> N;
  vector<string> arr;

  for(int i=0; i<N; i++)
  {
    cin >> str;
    arr.push_back(str);
  }
  sort(arr.begin(), arr.end(), compare); // 함수를 통한 추가 조건
  
  for(int i=0; i<N; i++)
  {
    if(arr[i] == arr[i+1])
      continue;
    cout << arr[i] << '\n';
  }
}
```

## 나이순 정렬
```C++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct member 
{
	int age;
	string name;
};

bool compare(const member a,const member b) 
{
	return a.age < b.age;
}

int main() 
{
	int n;
	cin >> n;
	vector <member> arr(n);
	
  for (int i=0; i<n; i++) 
  {
		cin >> arr[i].age >> arr[i].name;
	}
	stable_sort(arr.begin(), arr.end(), compare); 
	// 다른 요소들의 정렬 순서가 정렬 전과 같이 그대로 유지되는 정렬
  for (int i=0; i<n; i++) 
  {	
		cout << arr[i].age << " " << arr[i].name << '\n';
	}
}
```

## 좌표 압축
```C++
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int n, num;
  cin >> n;
  vector<int> v(n), cv(n);
  
  for (int i = 0; i < n; i++)
  {
    cin >> num;
    v[i] = num;
    cv[i] = num;
  }
  sort(cv.begin(), cv.end()); //오름차순 정렬
  cv.erase(unique(cv.begin(), cv.end()), cv.end()); // 중복 제거
  
  for (int i = 0; i < n; i++)
  {
    cout << lower_bound(cv.begin(), cv.end(), v[i]) - cv.begin() << ' ';
    // lower_bound(cv.begin(), cv.end(), v[i]) : i번째 요소 값 위치
    // i번째 요소 값 위치에서 cv벡터의 시작 주소값을 뺌
  }
}
```
