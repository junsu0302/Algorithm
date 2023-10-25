# String Algorithm

문자열 알고리즘(String Algorithm)은 문자열 데이터를 검색, 변환, 정렬, 비교 등의 작업을 수행하기 위해 사용되는 알고리즘이다.

문자열 알고리즘의 종류는 다음과 같다.
- Brute Force : 문자열을 한 글자씩 비교
- KMP(Knuth-Morris-Pratt) Algorithm : 부분 문자열을 효율적으로 탐색
  - 동작 원리 : 미리 접두사 함수를 계산하여 패턴의 이동거리 결정
  - 활용 사례 : 부분 문자열 검색
- Boyer-Moore Algorithm : 패턴을 빠르게 찾는데 특화
  - 동작 원리 : 좋거나 나쁜 접미사 규칙을 사용하여 패턴의 이동거리 결정
  - 활용 사례 : 빠른 문자열 검색
- Manacher Algorithm : 문자열에서 가장 긴 팰린드롬 부분 문자열 탐색
  - 동작 원리 : 중심 확장 기법 사용
  - 활용 사례 : 팰린드롬 문자열 검색
- Z Algorithm : 문자열 내 각 위치에서 시작하는 가장 긴 공통 접두사 길이 계산
  - 동작 원리 : z 함수를 사용하여 검색
  - 활용 사례 : 문자열 검색, 부분 문자열 검색, 유사성 비교
- Suffix Array : 문자열 내의 모든 접미사를 사전식 순서대로 정렬 후 저장
  - 동작 원리 : 접미사 정렬
  - 활용 사례 : 문자열 검색, 문자열 압축, 데이터 압축, 시퀀스 비교
- Aho-Corasick Algorithm : 여러 문자열 패턴을 동시에 검색
  - 동작 원리 : Trie를 사용하여 여러 패턴을 사전에 구축한 후 입력의 패턴 검색
  - 활용 사례 : 문자열 검색, 텍스트 분석, 키워드 추출
 
# 찾기
`Platinum 5` `1786`
```python
from sys import stdin

input = stdin.readline

class StringAlgorithm:
  def __init__(self):
    None

  def LPS(self, pattern): # KMP 알고리즘을 위해 패턴 탐색
    # Longest Prefix Suffix (투 포인터 활용)
    table = [0 for _ in range(len(pattern))]
  
    rignt = 0
    for left in range(1, len(pattern)):
      while rignt > 0 and pattern[left] != pattern[rignt]:
        rignt = table[rignt-1]
  
      if pattern[left] == pattern[rignt] :
        rignt += 1
        table[left] = rignt
  
    return table
  
  def KMP(self, word, pattern): 
    table = self.LPS(pattern) # LPS 통해 전처리된 테이블 불러오기
    results = []
    count = 0
  
    rignt = 0
    for left in range(len(word)):
      while rignt > 0 and word[left] != pattern[rignt] :
        rignt = table[rignt-1]
      if word[left] == pattern[rignt]:
        if rignt == len(pattern)-1 :
          results.append(left-len(pattern)+2)
          rignt = table[rignt]
          count += 1
        else:
          rignt += 1

    return count, results

  def solution(self, word, pattern):
    count, result = self.KMP(word, pattern)

    print(count)
    for element in result:
      print(element)
    
if __name__ == "__main__":
  T = input().rstrip()
  P = input().rstrip()
  kmp = StringAlgorithm()
  kmp.solution(T, P)
```

# 광고
`Platinum 4` `1305`
```python
from sys import stdin

input = stdin.readline

class StringAlgorithm:
  def __init__(self):
    None

  def LPS(self, pattern): 
    PI = [0 for _ in range(len(pattern))]
  
    rignt = 0
    for left in range(1, len(pattern)):
      while rignt > 0 and pattern[left] != pattern[rignt]:
        rignt = PI[rignt-1]
  
      if pattern[left] == pattern[rignt] :
        rignt += 1
        PI[left] = rignt
  
    return len(pattern) - PI[-1]

  def solution(self, pattern):
    result = self.LPS(pattern)
    print(result)
    
if __name__ == "__main__":
  L = int(input())
  pattern = input().rstrip()
  kmp = StringAlgorithm()
  kmp.solution(pattern)
```

# 개미굴
`Gold 3` `14725`
```python

```

# 문자열 집합
`Silver 3` `14425`
```python

```

# 휴대폰 자판
`Platinum 4` `5670`
```python

```
