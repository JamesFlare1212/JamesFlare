---
slug: "c-arithmetic-notation-part-2"
title: "实践手册：C 语言中的运算符号 Part 2"
subtitle: ""
date: 2023-02-17T00:38:54+08:00
draft: true
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "之前写了一篇关于加减乘除的文章，但是 C 语言的运算符可不止加减乘除。硬要说的话有加法，减法，乘法，除法，取模，自增，自减，赋值，相等，不相等，大于，小于，大于等于，小于等于，逻辑非，逻辑与，逻辑或，按位非，按位与，按位或，按位异或，左移，右移，条件运算符，逗号运算符。"
keywords: ""
license: ""
comment: false
weight: 0

tags:
- draft
categories:
- draft

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "之前写了一篇关于加减乘除的文章，但是 C 语言的运算符可不止加减乘除。硬要说的话有加法，减法，乘法，除法，取模，自增，自减，赋值，相等，不相等，大于，小于，大于等于，小于等于，逻辑非，逻辑与，逻辑或，按位非，按位与，按位或，按位异或，左移，右移，条件运算符，逗号运算符。"
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

之前写了一篇关于加减乘除的文章，

{{< link href="/posts/c-arithmetic-notation" content="实践手册：C 语言中的加减乘除运算" title="在 C 语言中，加减乘除是常见的数学运算，但它们使用的运算符与数学中的略有不同" card=true >}}

但是 C 语言的运算符可不止加减乘除。硬要说的话有加法，减法，乘法，除法，取模，自增，自减，赋值，相等，不相等，大于，小于，大于等于，小于等于，逻辑非，逻辑与，逻辑或，按位非，按位与，按位或，按位异或，左移，右移，条件运算符，逗号运算符。

但是总不能一口气讲完把，这次介绍另外几个。

| 运算符 | 描述 |
| --- | --- |
| % | 取模 |
| & | 取地址 |
| \| | 按位或 |
| ^ | 按位异或 |
| << | 左移 |
| >> | 右移 |
| ~ | 按位取反 |

## 例子