# 4779 칸토어 집합

import sys

"""
함수
def cantor(n):
    if n == 0:
        return "-"
    result = cantor(n-1)
    space = " " * 3 ** (n-1)
    result = result + space + result

    return result

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        result = cantor(n)
        print(result)
"""

"""
for 문
"""
for line in sys.stdin:
  result = "-"
  for i in range(int(line)):
    result = result + " " * len(result) + result

  print(result)
