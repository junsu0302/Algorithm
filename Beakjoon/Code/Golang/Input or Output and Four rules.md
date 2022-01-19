# 입출력과 사칙연산

## Hello World
```GO
package main

import (
  "fmt"
)

func main() {
  fmt.Println("Hello World!")
}

// 특수문자는 '\' 사용
```

## A+B, A-B, A\*B
```GO
package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scanf("%d %d", &a, &b)
  fmt.Println(a+b)
}
```

## A/B
```GO
package main

import (
  "fmt"
)

func main() {
  var a, b float64
  fmt.Scanf("%f %f", &a, &b)
  fmt.Println(a/b)
}
```
