---
slug: "go-arithmetic-notation"
title: "实践手册：Go 语言中的运算符号"
date: 2023-02-17T00:20:39+08:00
draft: true
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: ""
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

summary: ""
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

Go 语言中的运算符有许多种。

| 运算符 | 描述 |
| --- | --- |
| + | 加法 |
| - | 减法 |
| * | 乘法 |
| / | 除法 |
| % | 取模 |
| & | 按位与 |
| \| | 按位或 |
| ^ | 按位异或 |
| << | 左移 |
| >> | 右移 |
| &^ | 按位清除 |

## 例子

1. `+`：加法运算符。用于将两个数相加，或者将字符串连接起来。

    ```go
    a := 2
    b := 3
    c := a + b // c = 5

    s1 := "hello"
    s2 := "world"
    s3 := s1 + s2 // s3 = "helloworld"
    ```

1. `-`：减法运算符。用于将一个数减去另一个数。

    ```go
    a := 5
    b := 3
    c := a - b // c = 2
    ```

1. `*`：乘法运算符。用于将两个数相乘。

    ```go
    a := 2
    b := 3
    c := a * b // c = 6
    ```

1. `/`：除法运算符。用于将一个数除以另一个数。

    ```go
    a := 6
    b := 3
    c := a / b // c = 2
    ```

1. `%`：取模运算符。用于求一个数除以另一个数的余数。

    ```go
    a := 7
    b := 3
    c := a % b // c = 1
    ```

1. `&`：按位与运算符。用于将两个数按位与操作。

    ```go
    a := 0b1010 // 十进制为10
    b := 0b1100 // 十进制为12
    c := a & b  // c = 0b1000，即十进制为8
    ```

1. `|`：按位或运算符。用于将两个数按位或操作。

    ```go
    a := 0b1010 // 十进制为10
    b := 0b1100 // 十进制为12
    c := a | b  // c = 0b1110，即十进制为14
    ```

1. `^`：按位异或运算符。用于将两个数按位异或操作。

    ```go
    a := 0b1010 // 十进制为10
    b := 0b1100 // 十进制为12
    c := a ^ b  // c = 0b0110，即十进制为6
    ```

1. `<<`：左移运算符。用于将一个数的二进制表示向左移动指定的位数。

    ```go
    a := 0b1010 // 十进制为10
    b := 2
    c := a << b // c = 0b101000，即十进制为40
    ```

1. `>>`：右移运算符。用于将一个数的二进制表示向右移动指定的位数。

    ```go
    a := 0b1010 // 十进制为10
    b := 2
    c := a >> b // c = 0b10，即十进制为2
    ```

1. `&^`：按位清除运算符。用于将一个数的二进制表示中指定位置清零。

    ```go
    a := 0b1010 // 十进制为10
    b := 0b1100 // 十进制为12
    c := a &^ b // c = 0b0010，即十
    ```

以下是完整的例子

```go
package main

import "fmt"

func main() {
	// 加法运算符
	a := 2
	b := 3
	c := a + b
	fmt.Println(c) // 输出 5

	// 减法运算符
	d := 5
	e := 3
	f := d - e
	fmt.Println(f) // 输出 2

	// 乘法运算符
	g := 2
	h := 3
	i := g * h
	fmt.Println(i) // 输出 6

	// 除法运算符
	j := 6
	k := 3
	l := j / k
	fmt.Println(l) // 输出 2

	// 取模运算符
	m := 7
	n := 3
	o := m % n
	fmt.Println(o) // 输出 1

	// 按位与运算符
	p := 0b1010    // 十进制为 10
	q := 0b1100    // 十进制为 12
	r := p & q     // 十进制为 8
	fmt.Println(r) // 输出 8

	// 按位或运算符
	s := 0b1010    // 十进制为 10
	t := 0b1100    // 十进制为 12
	u := s | t     // 十进制为 14
	fmt.Println(u) // 输出 14

	// 按位异或运算符
	v := 0b1010    // 十进制为 10
	w := 0b1100    // 十进制为 12
	x := v ^ w     // 十进制为 6
	fmt.Println(x) // 输出 6

	// 左移运算符
	y := 0b1010    // 十进制为 10
	z := y << 2    // 左移 2 位，十进制为 40
	fmt.Println(z) // 输出 40

	// 右移运算符
	a1 := 0b1010    // 十进制为 10
	b1 := a1 >> 2   // 右移 2 位，十进制为 2
	fmt.Println(b1) // 输出 2

	// 按位清除运算符
	c1 := 0b1010    // 十进制为 10
	d1 := 0b1100    // 十进制为 12
	e1 := c1 &^ d1  // 按位清除，十进制为 2
	fmt.Println(e1) // 输出 2

	// 自增和自减运算符
	f1 := 5
	f1++            // 自增
	fmt.Println(f1) // 输出 6

	g1 := 5
	g1--            // 自减
	fmt.Println(g1) // 输出 4

	// 关系运算符
	h1 := 2
	i1 := 3
	fmt.Println(h1 > i1)  // 输出 false
	fmt.Println(h1 < i1)  // 输出 true
	fmt.Println(h1 == i1) // 输出 false
	fmt.Println(h1 != i1) // 输出 true

	// 逻辑运算符
	j1 := true
	k1 := false
	fmt.Println(j1 && k1) // 输出 false
	fmt.Println(j1 || k1) // 输出 true
	fmt.Println(!j1)      // 输出 false

	// 位运算符
	l1 := 0b1010              // 十进制为 10
	m1 := 0b1100              // 十进制为 12
	fmt.Printf("%b\n", ^l1)   // 输出二进制的按位取反，即 0b11111111111111111111111111110101
	fmt.Printf("%b\n", l1&m1) // 输出二进制的按位与，即 0b1000
	fmt.Printf("%b\n", l1|m1) // 输出二进制的按位或，即 0b1110
	fmt.Printf("%b\n", l1^m1) // 输出二进制的按位异或，即 0b0110

	// 赋值运算符
	n1 := 2
	n1 += 3         // 等价于 n1 = n1 + 3
	fmt.Println(n1) // 输出 5

	o1 := 5
	o1 -= 3         // 等价于 o1 = o1 - 3
	fmt.Println(o1) // 输出 2

	p1 := 2
	p1 *= 3         // 等价于 p1 = p1 * 3
	fmt.Println(p1) // 输出 6

	q1 := 6
	q1 /= 3         // 等价于 q1 = q1 / 3
	fmt.Println(q1) // 输出 2

	r1 := 7
	r1 %= 3         // 等价于 r1 = r1 % 3
	fmt.Println(r1) // 输出 1

	s1 := 0b1010    // 十进制为 10
	s1 &= 0b1100    // 等价于 s1 = s1 & 0b1100，十进制为 8
	fmt.Println(s1) // 输出 8

	t1 := 0b1010    // 十进制为 10
	t1 |= 0b1100    // 等价于 t1 = t1 | 0b1100，十进制为 14
	fmt.Println(t1) // 输出 14

	u1 := 0b1010    // 十进制为 10
	u1 ^= 0b1100    // 等价于 u1 = u1 ^ 0b1100，十进制为 6
	fmt.Println(u1) // 输出 6

	v1 := 0b1010    // 十进制为 10
	v1 <<= 2        // 等价于 v1 = v1 << 2，十进制为 40
	fmt.Println(v1) // 输出 40

	w1 := 0b1010    // 十进制为 10
	w1 >>= 2        // 等价于 w1 = w1 >> 2，十进制为 2
	fmt.Println(w1) // 输出 2

	// 其他运算符
	x1 := "hello"
	y1 := "world"
	z1 := x1 + y1   // 字符串拼接
	fmt.Println(z1) // 输出 "helloworld"
}
```