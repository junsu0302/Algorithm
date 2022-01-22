# 분할 정복

## 색종이 만들기
```C++
#include <iostream>
using namespace std;

int N;
int paper[128][128];
int blue, white;

void setting()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      cin >> paper[i][j];
}

void run(int y, int x, int size)
{
  int check = paper[y][x];
  for (int i = y; i < y + size; i++)
  {
    for (int j = x; j < x + size; j++)
    {
      if (check == 0 && paper[i][j] == 1)
        check = 2;
      else if (check == 1 && paper[i][j] == 0)
        check = 2;
      if (check == 2)
      {
        run(y, x, size / 2);
        run(y, x + size / 2, size / 2);
        run(y + size / 2, x, size / 2);
        run(y + size / 2, x + size / 2, size / 2);
        return;
      }
    }
  }
  if (check == 0)
    white++;
  else
    blue++;
}
int main()
{
  setting();
  run(0, 0, N);
  cout << white << '\n';
  cout << blue << '\n';
}
```

## 퀴드트리
```C++
#include <iostream>
#include <string>
using namespace std;

int N;
string S;
int arr[64][64];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> N;

  for (int i = 0; i < N; i++)
  {
    cin >> S;
 
    for (int j = 0; j < N; j++)
      arr[i][j] = S[j] - '0';
  }
}

void run(int n, int y, int x)
{
  if (n == 1)
  {
    cout << arr[y][x];
    return;
  }

  bool zero = true, one = true;
  
  for (int i = y; i < y + n; i++)
  {
    for (int j = x; j < x + n; j++)
    {
      if (arr[i][j])
        zero = false;
      else
        one = false;
    }
  }
  if (zero)
    cout << 0;
  else if(one)
    cout << 1;
  else
  {
    cout << "(";
    run(n / 2, y, x);
    run(n / 2, y, x + n / 2); 
    run(n / 2, y + n / 2, x); 
    run(n / 2, y + n / 2, x + n / 2); 
    cout << ")";
  }
}

int main()
{
  setting();
  run(N, 0, 0);
}
```

## 종이의 개수
```C++
#include<iostream>
using namespace std;

int N;
int paper[2188][2188]; 
int ans[3];
int check;

void setting()
{
	cin >> N;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> paper[i][j];
}

void run(int x, int y, int size) 
{
	
	check = paper[x][y];

	for (int i = x; i < x + size; i++)
		for (int j = y; j < y + size; j++)
		{
			if (paper[i][j] != paper[x][y])
			{	
				run(x, y, size / 3);
				run(x + size * 1 / 3, y, size / 3);
				run(x + size * 2 / 3, y, size / 3);
				run(x, y + size * 1 / 3, size / 3);
				run(x + size * 1 / 3, y + size * 1 / 3, size / 3);
				run(x + size * 2 / 3, y + size * 1 / 3, size / 3);
				run(x, y + size * 2 / 3, size / 3);
				run(x + size * 1 / 3, y + size * 2 / 3, size / 3);
				run(x + size * 2 / 3, y + size * 2 / 3, size / 3);
				return;
			}
		}
	ans[paper[x][y] + 1]++;
	return;
}

void print()
{
	for (int i = 0; i < 3; i++) 
    cout << ans[i] << "\n";
}

int main()
{
  setting();
	run(0, 0, N);
  print();
}
```

## 곱셈
```C++
#include <iostream>
using namespace std;

int A, B, C;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);  
  cin >> A >> B >> C;
}

long long run(int A, int B, int C)
{
  if (B == 1) 
    return A;
  else
  {
    long long num = run(A, B / 2, C);
    if (B % 2)
      return ((num*num) % C * A) % C;
    else
      return (num*num) % C;
  }
}

int main()
{
  setting();
  cout << run(A % C, B, C) << "\n";
}
```

## 이항 계수
```C++
#include<iostream>
#include<cmath>
using namespace std;

long long N, K, A, B, half;
long long mod;

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N >> K;
	A = 1;
	for (int i = N; i >= N - K + 1; i--) 
    A = (A * i) % 1000000007;

	B = 1;
	for (int i = 1; i <= K; i++) 
    B = (B * i) % 1000000007;
}

long long run(int x)
{
	if (x == 0) return 1;

	if (x % 2 == 1) return B * run(x - 1) % 1000000007;
	else
	{
		half = run(x / 2);
		return half * half % 1000000007;
	}
}

int main()
{
  setting();
	B = run(1000000005);

	cout << A * B % 1000000007;           
}
```

## 행렬 곱셈
```C++
#include <iostream>
using namespace std;

int N, M, K;
int arr1[101][101];
int arr2[101][101];
int res[101][101];

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++) 
		for (int j = 0; j < M; j++)
			cin>>arr1[i][j];
      
	cin >> M >> K;
	for (int i = 0; i < M; i++)
		for (int j = 0; j < K; j++)
			cin >> arr2[i][j];
}

void run()
{
	for (int i = 0; i < N; i++)
  {
		for (int j = 0; j < K; j++)
    {
			for (int k = 0; k < M; k++)
				res[i][j] += arr1[i][k] * arr2[k][j];
			cout << res[i][j] << " ";
		}
		cout << "\n";
	}
}

int main()
{
  setting();
  run();
}
```

## 행렬 제곱
```C++
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

long long N, B;
long long A[5][5];
long long temp[5][5];
long long ans[5][5];

void print(long long arr[5][5])
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			cout << arr[i][j] << " ";
		cout << "\n";
	}
}

void Matrix_multi(long long X[5][5], long long Y[5][5])
{

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
		{
			temp[i][j] = 0;
			for (int k = 0; k < N; k++)
				temp[i][j] += (X[i][k] * Y[k][j]);

			temp[i][j] %= 1000;
		}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			X[i][j] = temp[i][j];
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

	cin >> N >> B;

  for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			cin >> A[i][j];
		ans[i][i] = 1; 
	}
}

void run()
{
	while (B > 0)
	{
		if (B % 2 == 1)
		{
			Matrix_multi(ans, A);
		}
		Matrix_multi(A, A);
		B /= 2;
	}
}

int main()
{
  setting();
  run();
	print(ans);
}
```

## 피보나치 수 6
```C++
#include <iostream>
using namespace std;
 
long long N;

void Matrix_multi(long long m1[][2], long long m2[][2])
{
  long long arr[2][2];
  long long temp;
 
  for(int i=0;i<2;++i)
  {
      for(int j=0;j<2;++j)
      {
          temp = 0;
          for(int k=0;k<2;++k)
              temp += (m1[i][k] * m2[k][j]);
          arr[i][j] = temp % 1000000007;
      }
  }
 
  for(int i=0;i<2;++i)
      for(int j=0;j<2;++j)
          m1[i][j] = arr[i][j];
 
  return;
}
 
void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run() 
{
  long long arr[2][2] = {1, 1, 1, 0};
  long long ans[2][2] = {1, 0, 0, 1};

  while(N > 0)
  {
    if(N % 2 == 1)
        Matrix_multi(ans, arr);

    N /= 2;
    Matrix_multi(arr, arr);
  }
  cout<< ans[1][0];
}

int main()
{
  setting();
  run();
}
```

## 히스토그램에서 가장 큰 직사각형
```C++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
 
long long N;
vector<long long> v;

long long Max_Area(long long left, long long right) 
{
  long long mid = (left + right)/2;
  long long mid_area = v[mid], height = v[mid];
  long long num_left = mid - 1; 
  long long num_right = mid + 1;
 
  if(left +1 >= right)  return mid_area; 
  
  while(num_left > left || num_right < right) 
  {
    if(num_left <= left || (num_right < right && v[num_left] <= v[num_right])) 
    {
      height = min(v[num_right], height);
      num_right++;
    }
    else 
    {
      height = min(height, v[num_left]);
      num_left--;
    }
    long long width = num_right -1 - num_left; 
    mid_area = max(mid_area, width * height);
    }
    return max(mid_area, max(Max_Area(left, mid), Max_Area(mid, right)));
}

void setting()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
}

void run()
{

    
  v = vector<long long>(N+2);
  v[0] = v[N+1] = 0;
  for(int i = 1; i <= N; i++) 
    cin >> v[i];
}
 
int main() 
{
  while(1) 
  {
    setting();
    if(N == 0)  break;
    run();
    cout << Max_Area(0, N+1) << "\n";
  }
}
```

## 가장 가까운 두 점
```C++
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int MAX = 2000000000;
int N;
vector<pair<int, int>> arr;

// low번째 점과 high번째 점 사이 거리를 구한다
int Distance(int low, int high)
{
	int lowX = arr[low].first, lowY = arr[low].second;
	int highX = arr[high].first, highY = arr[high].second;
	
	int disX = highX - lowX, disY = highY - lowY;
	
	return disX * disX + disY * disY;
}

// 가장 가까운 두 점의 거리를 구하는 재귀함수를 이분 탐색을 통해 구현한다
int BinarySearch(int low, int high)
{
	// 기저 조건은 처음과 끝 숫자의 차이가 1인 경우다
	if(low == high)
		return MAX;
	
	if(low + 1 >= high)
		return Distance(low, high);
	
	int Distance_Min = Distance(low, high);
	int num = 0, mid = (low + high) / 2;
	
	// 왼쪽 영역의 최소 거리를 구하고
	if((num = BinarySearch(low, mid)) < Distance_Min)
		Distance_Min = num;
	// 오른쪽 영역의 최소 거리를 구하여 둘 중 최솟값을 찾는다
	if((num = BinarySearch(mid + 1, high)) < Distance_Min)
		Distance_Min = num;
	
	vector<pair<int, int>> v;
	// 중간 영역에서 기준선과 x값의 차이의 제곱이 최솟값 이하인 영역의 점들을 찾는다
	int lineX = arr[mid].first;
	// 왼쪽 영역
	for(int i=mid; i>=low; i--)
  {
		int x = arr[i].first;
    int num = lineX - x;
		if(Distance_Min <= num * num) break;
		v.push_back({arr[i].second, arr[i].first});
	}
	// 오른쪽 영역
	for(int i=mid+1; i<=high; i++)
  {
		int x = arr[i].first;
    int num = lineX - x;
		if(Distance_Min <= num * num) break;
		v.push_back({arr[i].second, arr[i].first});
	}
	
	int len = v.size();
	// 아무 점도 못찾았으면 최솟값을 반환한다
	if(len == 0) return Distance_Min;
	// y값에 대해 정렬한다
	sort(v.begin(), v.end());
	
	for(int i=0; i<len; i++)
  {
		int iX = v[i].second;
    int iY = v[i].first;
		for(int j=i+1; j<len; j++)
    {
			int jX = v[j].second;
      int jY = v[j].first;
			int Distance_X = jX - iX;
      int Distance_Y = jY - iY;
			// 두 점의 y좌표의 차이를 제곱한 값이 최솟값 이상이면 loop를 멈춘다
			if(Distance_Min <= Distance_Y * Distance_Y) break;
			// 두 점의 x좌표의 차이를 제곱한 값이 최솟값 이상이면 건너뛴다
			if(Distance_Min <= Distance_X * Distance_X) continue;
			
			int num = Distance_X * Distance_X + Distance_Y * Distance_Y;
			if(num < Distance_Min)
				Distance_Min = num;
		}
	}
	return Distance_Min;
}

int main(){
	cin >> N;
	
	arr = vector<pair<int, int>>(N);
	
	for(int i=0; i<N; i++)
    cin >> arr[i].first >> arr[i].second;
	
	sort(arr.begin(), arr.end());
	
	cout << BinarySearch(0, N-1);
}
```
