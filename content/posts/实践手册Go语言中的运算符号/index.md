---
slug: "go-arithmetic-notation"
title: "实践手册：Go 语言中的运算符号"
date: 2023-02-17T00:20:39+08:00
draft: false
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "操作符是编程语言的基本构件，Go也不例外。我将探讨 Go 中不同类型的运算符，以及如何使用它们来操作和比较数值。从基本的算术运算符到更高级的位运算符和逻辑运算符，我们将涵盖您在Go中开始使用运算符所需要知道的一切。"
keywords: ""
license: ""
comment: true
weight: 0

tags:
- Go
categories:
- Programing

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "操作符是编程语言的基本构件，Go也不例外。我将探讨 Go 中不同类型的运算符，以及如何使用它们来操作和比较数值。从基本的算术运算符到更高级的位运算符和逻辑运算符，我们将涵盖您在Go中开始使用运算符所需要知道的一切。"
resources:
- name: featured-image
  src: featured-image.jpg
- name: featured-image-preview
  src: featured-image-preview.jpg

toc:
  enable: true
math:
  enable: false
lightgallery: false
seo:
  images: []

repost:
  enable: true
  url: ""

# See details front matter: https://fixit.lruihao.cn/theme-documentation-content/#front-matter
---

<!--more-->

## 前言

Go 语言中的运算符有许多种，

- 算术运算符：加法 `+`、减法 `-`、乘法 `*`、除法 `/`、取模 `%`
- 自增/自减运算符：自增 `++`、自减 `--`
- 赋值运算符：赋值 `=`、加法赋值 `+=`、减法赋值 `-=`、乘法赋值 `*=`、除法赋值 `/=`、取模赋值 `%=`、左移赋值 `<<=`、右移赋值 `>>=`、按位与赋值 `&=`、按位异或赋值 `^=`、按位或赋值 `|=`、按位清零赋值 `&^=`
- 比较运算符：相等 `==`、不相等 `!=`、大于 `>`、小于 `<`、大于等于 `>=`、小于等于 `<=`
- 逻辑运算符：逻辑非 `!`、逻辑与 `&&`、逻辑或 `||`
- 位运算符：按位非 `~`、按位与 `&`、按位或 `|`、按位异或 `^`、左移 `<<`、右移 `>>`、按位清零 `&^`
- 其他运算符：条件运算符 `?:`、逗号运算符 `,`

做个表格归纳一下。

### Arithmetic Operators

| Operator | Description |
| --- | --- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Remainder |

### Bitwise Operators

| Operator | Description |
| --- | --- |
| & | Bitwise AND |
| \| | Bitwise OR |
| ^ | Bitwise XOR |
| << | Left shift |
| >> | Right shift |
| &^ | Bit clear |

### Comparison Operators

| Operator | Description |
| --- | --- |
| == | Equal to |
| != | Not equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

### Logical Operators

| Operator | Description |
| --- | --- |
| && | Logical AND |
| \| | Logical OR |
| ! | Logical NOT |

### Assignment Operators

| Operator | Description |
| --- | --- |
| = | Simple assignment |
| += | Addition assignment |
| -= | Subtraction assignment |
| *= | Multiplication assignment |
| /= | Division assignment |
| %= | Remainder assignment |
| <<= | Left shift assignment |
| >>= | Right shift assignment |
| &= | Bitwise AND assignment |
| ^= | Bitwise XOR assignment |
| \|= | Bitwise OR assignment |
| &^= | Bit clear assignment |

### Miscellaneous Operators

| Operator | Description |
| --- | --- |
| ++ | Increment |
| -- | Decrement |
| * | Pointer to |
| & | Address of |
| <- | Channel send/receive |
| == nil | Nil check |

## Example

### Arithmetic Operators

```go
package main

import "fmt"

func main() {
    a := 10
    b := 3

    // Addition
    c := a + b
    fmt.Printf("%d + %d = %d\n", a, b, c)

    // Subtraction
    c = a - b
    fmt.Printf("%d - %d = %d\n", a, b, c)

    // Multiplication
    c = a * b
    fmt.Printf("%d * %d = %d\n", a, b, c)

    // Division
    c = a / b
    fmt.Printf("%d / %d = %d\n", a, b, c)

    // Remainder
    c = a % b
    fmt.Printf("%d %% %d = %d\n", a, b, c)
}
```

Outputs:

```txt
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3
10 % 3 = 1
```

In this example, we declare two variables `a` and `b` with the values 10 and 3, respectively. We then perform arithmetic operations on these variables using the `+`, `-`, `*`, `/`, and `%` operators, storing the results in the variable `c` and printing them to the console with `fmt.Printf()`. We also include comments explaining each operation.

### Bitwise Operators

```go
package main

import "fmt"

func main() {
    a := 0b1010
    b := 0b1100

    // Bitwise AND
    c := a & b
    fmt.Printf("%b & %b = %b\n", a, b, c)

    // Bitwise OR
    c = a | b
    fmt.Printf("%b | %b = %b\n", a, b, c)

    // Bitwise XOR
    c = a ^ b
    fmt.Printf("%b ^ %b = %b\n", a, b, c)

    // Left shift
    c = a << 1
    fmt.Printf("%b << 1 = %b\n", a, c)

    // Right shift
    c = a >> 1
    fmt.Printf("%b >> 1 = %b\n", a, c)

    // Bit clear
    c = a &^ b
    fmt.Printf("%b &^ %b = %b\n", a, b, c)
}
```

Output:

```txt
1010 & 1100 = 1000
1010 | 1100 = 1110
1010 ^ 1100 = 110
1010 << 1 = 10100
1010 >> 1 = 101
1010 &^ 1100 = 10
```

In this example, we declare two variables `a` and `b` with the values `0b1010` and `0b1100`, respectively, which are binary literals that represent the numbers 10 and 12 in base 10. We then perform bitwise operations on these variables using the `&`, `|`, `^`, `<<`, `>>`, and `&^` operators, storing the results in the variable `c` and printing them to the console with `fmt.Printf()`. We also include comments explaining each operation.

### Comparison Operators

```go
package main

import "fmt"

func main() {
    a := 10
    b := 3

    // Equal to
    c := a == b
    fmt.Printf("%d == %d = %t\n", a, b, c)

    // Not equal to
    c = a != b
    fmt.Printf("%d != %d = %t\n", a, b, c)

    // Less than
    c = a < b
    fmt.Printf("%d < %d = %t\n", a, b, c)

    // Greater than
    c = a > b
    fmt.Printf("%d > %d = %t\n", a, b, c)

    // Less than or equal to
    c = a <= b
    fmt.Printf("%d <= %d = %t\n", a, b, c)

    // Greater than or equal to
    c = a >= b
    fmt.Printf("%d >= %d = %t\n", a, b, c)
}
```

Output:

```txt
10 == 3 = false
10 != 3 = true
10 < 3 = false
10 > 3 = true
10 <= 3 = false
10 >= 3 = true
```

In this example, we declare two variables `a` and `b` with the values 10 and 3, respectively. We then perform comparison operations on these variables using the `==`, `!=`, `<`, `>`, `<=`, and `>=` operators, storing the results in the variable `c` and printing them to the console with `fmt.Printf()`. We also include comments explaining each operation.


### Logical Operators

```go
package main

import "fmt"

func main() {
    a := true
    b := false

    // Logical AND
    c := a && b
    fmt.Printf("%t && %t = %t\n", a, b, c)

    // Logical OR
    c = a || b
    fmt.Printf("%t || %t = %t\n", a, b, c)

    // Logical NOT
    c = !a
    fmt.Printf("!%t = %t\n", a, c)
}
```

Output:

```txt
true && false = false
true || false = true
!true = false
```

In this example, we declare two boolean variables `a` and `b` with the values `true` and `false`, respectively. We then perform logical operations on these variables using the `&&`, `||`, and `!` operators, storing the results in the variable `c` and printing them to the console with `fmt.Printf()`. We also include comments explaining each operation.

### Assignment Operators

```go
package main

import "fmt"

func main() {
    a := 10

    // Simple assignment
    b := a
    fmt.Printf("b = %d\n", b)

    // Addition assignment
    a += 5
    fmt.Printf("a += 5 -> a = %d\n", a)

    // Subtraction assignment
    a -= 2
    fmt.Printf("a -= 2 -> a = %d\n", a)

    // Multiplication assignment
    a *= 3
    fmt.Printf("a *= 3 -> a = %d\n", a)

    // Division assignment
    a /= 2
    fmt.Printf("a /= 2 -> a = %d\n", a)

    // Remainder assignment
    a %= 3
    fmt.Printf("a %%= 3 -> a = %d\n", a)

    // Left shift assignment
    a <<= 2
    fmt.Printf("a <<= 2 -> a = %d\n", a)

    // Right shift assignment
    a >>= 1
    fmt.Printf("a >>= 1 -> a = %d\n", a)

    // Bitwise AND assignment
    a &= 5
    fmt.Printf("a &= 5 -> a = %d\n", a)

    // Bitwise XOR assignment
    a ^= 10
    fmt.Printf("a ^= 10 -> a = %d\n", a)

    // Bitwise OR assignment
    a |= 15
    fmt.Printf("a |= 15 -> a = %d\n", a)

    // Bit clear assignment
    a &^= 12
    fmt.Printf("a &^= 12 -> a = %d\n", a)
}
```

Output:

```txt
b = 10
a += 5 -> a = 15
a -= 2 -> a = 13
a *= 3 -> a = 39
a /= 2 -> a = 19
a %= 3 -> a = 1
a <<= 2 -> a = 4
a >>= 1 -> a = 2
a &= 5 -> a = 0
a ^= 10 -> a = 10
a |= 15 -> a = 15
a &^= 12 -> a = 3
```

In this example, we declare a variable `a` with the value `10`. We then perform various assignment operations on `a` using the `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`, and `&^=` operators, storing the results in the variable `a` and printing them to the console with `fmt.Printf()`. We also include comments explaining each operation.

### Miscellaneous Operators

```go
package main

import "fmt"

func main() {
    // Increment
    a := 5
    a++
    fmt.Printf("a++ -> a = %d\n", a)

    // Decrement
    a--
    fmt.Printf("a-- -> a = %d\n", a)

    // Pointer to
    b := &a
    fmt.Printf("&a -> b = %p\n", b)

    // Address of
    c := *b
    fmt.Printf("*b -> c = %d\n", c)

    // Channel send/receive
    ch := make(chan int)
    go func() {
        ch <- 5
    }()
    fmt.Printf("<-ch -> %d\n", <-ch)

    // Nil check
    var d *int
    if d == nil {
        fmt.Println("d is nil")
    } else {
        fmt.Println("d is not nil")
    }
}
```

Output:

```txt
a++ -> a = 6
a-- -> a = 5
&a -> b = 0xc000012098
*b -> c = 5
<-ch -> 5
d is nil
```

In this example, we demonstrate various operators in Go with comments in English. We declare variables and channels as necessary, and perform operations using the `++`, `--`, `*`, and `&` operators. We also include a nil check for the `*int` pointer type, using the `==` operator to compare to `nil`. Finally, we include a channel send/receive example using the `<-` operator.