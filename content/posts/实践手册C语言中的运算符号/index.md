---
slug: c-arithmetic-notation-part-2
title: 实践手册：C 语言中的运算符号 Part 2
subtitle: ""
date: 2023-02-17T00:38:54+08:00
draft: false
author: James
authorLink: https://www.jamesflare.com
authorEmail: jamesflare1212@gmail.com
description: 之前写了一篇关于加减乘除的文章，但是 C 语言的运算符可不止加减乘除。硬要说的话有加法，减法，乘法，除法，取模，自增，自减，赋值，相等，不相等，大于，小于，大于等于，小于等于，逻辑非，逻辑与，逻辑或，按位非，按位与，按位或，按位异或，左移，右移，条件运算符，逗号运算符。
keywords: ""
license: ""
comment: true
weight: 0

tags:
  - C
categories:
  - Programing

hiddenFromHomePage: false
hiddenFromSearch: false

summary: 之前写了一篇关于加减乘除的文章，但是 C 语言的运算符可不止加减乘除。硬要说的话有加法，减法，乘法，除法，取模，自增，自减，赋值，相等，不相等，大于，小于，大于等于，小于等于，逻辑非，逻辑与，逻辑或，按位非，按位与，按位或，按位异或，左移，右移，条件运算符，逗号运算符。
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

## Introduction

之前写了一篇关于加减乘除的文章，

{{< link href="/posts/c-arithmetic-notation" content="实践手册：C 语言中的加减乘除运算" title="在 C 语言中，加减乘除是常见的数学运算，但它们使用的运算符与数学中的略有不同" card=true >}}

但是 C 语言的运算符可不止加减乘除。硬要说的话有加法，减法，乘法，除法，取模，自增，自减，赋值，相等，不相等，大于，小于，大于等于，小于等于，逻辑非，逻辑与，逻辑或，按位非，按位与，按位或，按位异或，左移，右移，条件运算符，逗号运算符。

如果学习编程，最好是从英文开始，因为它的语言精准，而且全世界通用，在互联网中搜索到的相关资料比中文更多，这在有疑问或者 Bug 的时候特别重要。

***

小小分类一下：

### Basic

| Operator | Description |
| --- | --- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| = | Assignment |
| == | Equality |
| != | Inequality |
| > | Greater than |
| < | Less than |

### Normal

| Operator | Description |
| --- | --- |
| >= | Greater Than or Equal to |
| <= | Less Than or Equal to |
| ! | Logical NOT |
| && | Logical AND |
| \| | Logical OR |
| ~ | Bitwise NOT |
| & | Bitwise AND |
| \| | Bitwise OR |
| ^ | Bitwise XOR |
| << | Left shift |
| >> | Right shift |

### Advance

| Operator | Description |
| --- | --- |
| % | Modulo |
| ++ | Increment |
| -- | Decrement |
| ?: | Conditional Operator |
| , | Comma Operator |

## Examples

### Basic

```c
#include <stdio.h>

int main() {
   int a = 21;  // Define variable a and assign it a value of 21
   int b = 10;  // Define variable b and assign it a value of 10
   int c;       // Define variable c

   c = a + b;   // Add variables a and b and assign the result to c
   printf("a + b = %d\n", c );  // Output the result of a + b

   c = a - b;   // Subtract variable b from a and assign the result to c
   printf("a - b = %d\n", c );  // Output the result of a - b

   c = a * b;   // Multiply variables a and b and assign the result to c
   printf("a * b = %d\n", c );  // Output the result of a * b

   c = a / b;   // Divide variable a by b and assign the result to c
   printf("a / b = %d\n", c );  // Output the result of a / b

   c = a % b;   // Calculate the remainder of a divided by b and assign the result to c
   printf("a %% b = %d\n", c ); // Output the result of a % b

   c = a == b;  // Compare whether a is equal to b and assign the result to c
   printf("a == b = %d\n", c ); // Output the result of a == b

   c = a != b;  // Compare whether a is not equal to b and assign the result to c
   printf("a != b = %d\n", c ); // Output the result of a != b

   c = a > b;   // Compare whether a is greater than b and assign the result to c
   printf("a > b = %d\n", c );  // Output the result of a > b

   c = a < b;   // Compare whether a is less than b and assign the result to c
   printf("a < b = %d\n", c );  // Output the result of a < b

   return 0;
}
```

输出结果如下：

```txt
a + b = 31
a - b = 11
a * b = 210
a / b = 2
a % b = 1
a == b = 0
a != b = 1
a > b = 1
a < b = 0
```

### Normal

```c
#include <stdio.h>

int main() {
   int a = 5;  // Define variable a and assign it a value of 5
   int b = 20; // Define variable b and assign it a value of 20
   int c;      // Define variable c

   // Greater than or equal to operator
   if ( a >= b ) {
      printf("a is greater than or equal to b\n" );
   } else {
      printf("a is less than b\n" );
   }

   // Less than or equal to operator
   if ( b <= a ) {
      printf("b is less than or equal to a\n" );
   } else {
      printf("b is greater than a\n" );
   }

   // Logical NOT operator
   if ( !(a && b) ) {
      printf("a and b are not true\n" );
   } else {
      printf("a and b are true\n" );
   }

   // Logical AND operator
   if ( a && b ) {
      printf("a and b are true\n" );
   } else {
      printf("a and b are not true\n" );
   }

   // Logical OR operator
   if ( a || b ) {
      printf("a or b is true\n" );
   } else {
      printf("a and b are not true\n" );
   }

   // Bitwise NOT operator
   c = ~a;    /* Invert the bits of a */
   printf("~a = %d\n", c );

   // Bitwise AND operator
   c = a & b; /* Bitwise AND of a and b */
   printf("a & b = %d\n", c );

   // Bitwise OR operator
   c = a | b; /* Bitwise OR of a and b */
   printf("a | b = %d\n", c );

   // Bitwise XOR operator
   c = a ^ b; /* Bitwise XOR of a and b */
   printf("a ^ b = %d\n", c );

   // Left shift operator
   c = a << 2; /* Shift the bits of a two places to the left */
   printf("a << 2 = %d\n", c );

   // Right shift operator
   c = a >> 2; /* Shift the bits of a two places to the right */
   printf("a >> 2 = %d\n", c );

   return 0;
}
```

输出结果如下：

```txt
a is less than b
b is greater than a
a and b are not true
a and b are true
a or b is true
~a = -6
a & b = 4
a | b = 21
a ^ b = 17
a << 2 = 20
a >> 2 = 1
```

### Advance

```c
#include <stdio.h>

int main() {
   int a = 21;  // Define variable a and assign it a value of 21
   int b = 10;  // Define variable b and assign it a value of 10
   int c;       // Define variable c

   // Modulo operator
   c = a % b;   // Calculate the remainder of a divided by b and assign the result to c
   printf("a %% b = %d\n", c ); // Output the result of a % b

   // Increment operator
   c = a++;     // Assign the value of a to c and then increment a
   printf("a++ = %d\n", c );    // Output the result of a++

   // Decrement operator
   c = a--;     // Assign the value of a to c and then decrement a
   printf("a-- = %d\n", c );    // Output the result of a--

   // Conditional operator
   c = a > b ? a : b;   // If a is greater than b, assign the value of a to c, otherwise assign the value of b to c
   printf("a > b ? a : b = %d\n", c ); // Output the result of a > b ? a : b

   // Comma operator
   c = (a = 5, b = 7, a + b);   // Assign 5 to a, 7 to b, and then calculate a + b and assign the result to c
   printf("(a = 5, b = 7, a + b) = %d\n", c); // Output the result of (a = 5, b = 7, a + b)

   return 0;
}
```

输出结果如下：

```txt
a % b = 1
a++ = 21
a-- = 22
a > b ? a : b = 21
(a = 5, b = 7, a + b) = 12
```