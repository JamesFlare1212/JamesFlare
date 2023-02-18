---
slug: "chatgpt-guide"
title: "使用 ChatGPT 提速日常工作以及示例"
subtitle: ""
date: 2023-02-18T00:34:20+08:00
draft: true
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: ""
keywords: ""
license: ""
comment: false
weight: 0

tags:
- AI
- ChatGPT
categories:
- Tutorials

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

## Introduction

在我们的日常学术工作中，我们会遇到各种各样的任务。

比如

- 写作任务
- 阅读任务
- 文本处理
- 代码任务

## Writing Task

首先，写作任务有很多，比如

- 论文写作
- 语法润色

### 论文写作

**Q：对于论文的写作，该不该，或者说能不能使用这个软件？**

我的回答是，这是大势所趋，是必然，所有人都应该乘早学会使用这样的工具。它拥有远超人类的对文字的精准理解，能够帮你省去很多不必要的精力，你可能用过 Grammarly 这样的修改语法的工具。但是它本身并不能真正意义上理解文本的内容，也就不可能帮你重新组织语言，而这对 ChatGPT 而言，是小菜一碟。

**Q：什么是浪费时间的行为？**

如果你想要让它给你从 0 到 1 写一篇好论文，那是不现实的，效果也不会好。

**Q：什么是提高效率的行为？**

水课程论文和对论文进行深度修改润色。比如你要交了，发现还有一堆错误，然后和导师一起改，花了时间可能还有些改不出来，要让别人改。这时候，几周的工作量可能你半天就能做完了。

**Q：用这个写作业，写论文是不是学术不端？**

不是。首先，课程论文不用 ChatGPT 你也是东拼西凑，不想写的人总有理由。其次润色论文本身也是合规的，甚至也有不少相关的业务，重要的不应该是你的内容吗，在这个方面 ChatGPT 让你的论文的可读性大大提升。

可能你会说老师说了不让你用，那么这时候我觉得你要有自己的判断，我认为技术是无罪的，你也该想想是否完全理解了它的本质。

**Q：它的好处是什么？**

提升论文的逻辑性，突出重点。这大概率是学生最大的问题，你可能写了一堆东西不知道自己在写什么，一段内容东西堆一起，老师读了云里雾里看不懂。都看不下去了还怎么给你评分。

让用词更准确，内容更丰富。它可以修正细微的语法错误，用词更丰富。

论文扩写，降重。这也不好说，要是你扔了一堆垃圾进去，没准还变短了。

#### 润色

如果你要获得一个好的回答，你要先学会问问题。

比如你希望它帮你改进你段落的逻辑，修正一些错误那么可以这样。

> 请改写以下段落，让其更有逻辑，重点更加突出：

或者

> Please rewrite the following paragraphs to make them more logical and focused:

***

如果你希望它帮你改进你段落的逻辑，修正一些错误的同时再增加一点细节和内容，那么可以这样。

> 请改写以下段落，让用词更加准确，内容更加丰富：

或者

> Please rewrite the following paragraphs to make the wording more accurate and informative:

***

如果你想提升你段落中的词汇水平，那么可以像这样。

> I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations. My first sentence is "xxx"

#### 语法修正

你也可以要求它修正你段落中的错误，并且同时提供修改的原因。

> In the following, I will provide text with mistakes. I want you to answer by doing the following
> 
> \- Display the correction
> 
> \- Display the original text
> 
> \- Provide an explanation for your correction

## Reading Task

### Summarize

> Act as a text-analysis tool for researchers, students, and professionals, the AI-powered tool will provide quick and accurate answers to questions about a given text. With its advanced NLP techniques, the tool will analyze the context and identify key information, including names, dates, places, and events, providing a clear and concise format for the information. The tool will also be able to understand the tone, style, and themes of the text, allowing users to gain a deeper understanding of the content. Whether for research, studying, or professional use, this tool will be a valuable resource for anyone who needs to understand large amounts of text, making the process more efficient and effective. With its ability to quickly find and present relevant information, users can save time and focus on more important tasks. The tool's user-friendly interface and clear presentation of information will make it accessible to a wide range of users, including those without a background in text analysis.

### Questioning

## Translation

> 从现在开始，你将扮演一位世界顶级的翻译大师，你的母语是英语和中文，并且充当我的翻译助理。我说的每句话，你都应该以“中文”和“英文”的形式展现给我，谢谢。

你也可以根据自己的需要，组织构建更复杂的语句。

`````txt
从现在开始，你将扮演一位世界顶级的翻译大师，你的母语是英语和中文，并且充当我的翻译助理。我说的每句话，你都应该当作需要翻译的内容，把其中的英文内容翻译成中文。请在一个文本类型代码块内输出你的任何回复，同时使用\`\`\`\`txt来启用你的代码块，而不是\`\`\`或者其他任何东西，也不要直接输出回答，你的回答必须包裹在一个\`\`\`\`txt开头，以及\`\`\`\`结尾的文本类型代码块里。具体格式如下：

````txt
[你的翻译结果]
````

以下是一个例子，当我输入：

````txt
# Basic Rules

The most simple rules are so-called _"Basic rules"._ They are used to block requests to specific URLs. Or to unblock it, if there is a special marker "@@" at the beginning of the rule. The basic principle for this type of rules is quite simple: you have to specify the address and additional parameters that limit or expand the scope of the rule.
````

时，你应该回答：

````txt
# 基本规则

最简单的规则被称为“基本规则”。它们用于阻止特定 URL 的请求。或者如果规则开头有特殊标记“@@”，则用于取消阻止。这种类型规则的基本原则非常简单：您必须指定地址和额外的参数，以限制或扩展规则的范围。
````

所有的要求在现在和以后的所有对话中都适用，请不要忘记。如果你明白了我以上的要求，把以下内容当成我第二次输入并且输出你的回答：

````txt
# Basic Rules

```
Hello World!
```

The most simple rules are so-called _"Basic rules"._ They are used to block requests to specific URLs. Or to unblock it, if there is a special marker "@@" at the beginning of the rule. The basic principle for this type of rules is quite simple: you have to specify the address and additional parameters that limit or expand the scope of the rule.
````
`````