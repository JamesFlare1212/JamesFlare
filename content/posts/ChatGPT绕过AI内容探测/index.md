---
slug: "bypass-ai-detectiontion"
title: "使用工具以及 ChatGPT 绕过 AI 内容探测"
subtitle: ""
date: 2023-02-18T14:11:55+08:00
draft: false
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "现在或许有不少号称可以探测AI生成内容的工具或者服务，如果被探测出 AI 内容会怎么样？以及，如何避免被探测？"
keywords: ""
license: ""
comment: true
weight: 0

tags:
- AI
categories:
- Tutorials

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "现在或许有不少号称可以探测AI生成内容的工具或者服务，如果被探测出 AI 内容会怎么样？以及，如何避免被探测？"
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

现在或许有不少号称可以探测AI生成内容的工具或者服务，比如

- [Content at Scale](https://contentatscale.ai/ai-content-detector/)
- [Writer.com](https://writer.com/ai-content-detector/)
- [Copyleaks](https://copyleaks.com/features/ai-content-detector)
- [Crossplag](https://crossplag.com/ai-content-detector/)
- [Corrector](https://corrector.app/ai-content-detector/)
- [Sapling AI](https://sapling.ai/utilities/ai-content-detector)
- [OpenAI](https://platform.openai.com/ai-text-classifier)
- [Originality AI](https://originality.ai/)

或许有人要担心了，我的内容被逮住了怎么办？

首先要理清两个问题：如果被探测出 AI 内容会怎么样？以及，如何避免被探测？

### What IF

**Q：如果被探测出AI内容会怎么样？**

个人认为，这不是一个太大的问题。内容探测告诉你的是此内容是 AI **生成**的概率，先不谈工具本身是否准确，次要的是，如果你使用 AI 从 0 到 1 完全生成一篇论文，本身说明你不想得一个高分。现阶段 AI 生成的论文只能说能看，但是没有什么意义，而且在小众领域搞不好一本正经的胡说八道。

除非你的评分标准里，有说，高于多少 AI 生成概率作业就判 0 分，或者超过多少概率扣分，否则我认为没有什么好藏着的。你写的内容好，用它来润色润色又如何（其实这种情况你大概率不用管这个问题，探测分数不会高的）。总不能我这个高级研究内容用了 AI 帮助我增强表达，修正语法后就变得一文不值了吧。

还有一种情况是 SEO，我后面会说。

**Q：如何避免被探测？**

你要是说，我就是想浑水摸鱼。比如什么什么东西没做好，被领导要求写个 8000 字反思，恰巧这个领导还懂些皮毛，会用点工具看看你这个下属是不是用的 AI 来忽悠自己。你和他辩论写这东西的意义，想必他也不会听，这种行为就是恶心人。那么，只能另辟蹊径了。

### Application

除了上述的情况，还有可能，比如你是做内容的，而且大量使用 AI 生成内容，恰巧你对搜索引擎什么的排面还有点要求。虽然还没有直接证据说会因为内容是 AI 生成的而降低排名，但是你想防范于未然。

### Limitation

摘自 [OpenAI](https://openai.com/blog/new-ai-classifier-for-indicating-ai-written-text/) 的说明

> 我们的分类器有一些重要的局限性。它不应作为主要的决策工具，而应作为确定一段文本来源的其他方法的补充。
> 
> - 在短文本（1,000个字符以下）上，分类器非常不可靠。甚至在较长的文本上，分类器有时也会错误地标记。
> - 有时，人工编写的文本会被我们的分类器错误地但自信地标记为AI编写的文本。
> - 我们建议仅将分类器用于英文文本。它在其他语言上的表现要差得多，并且在代码上不可靠。
> - 非常可预测的文本无法可靠地识别。例如，无法预测前1,000个质数的列表是由人工编写还是AI编写，因为正确答案总是相同的。
> - AI编写的文本可以进行编辑以逃避分类器。像我们这样的分类器可以根据成功的攻击进行更新和重新训练，但未来是否有检测优势尚不清楚。
> - 基于神经网络的分类器在其训练数据之外的数据上往往校准不良。对于与我们训练集中的文本非常不同的输入，分类器有时会非常自信地做出错误的预测。

## Quillbot

这是一般的思路，Quillbot 可以帮你重新组织语言，添加同义词等。不过请对修改结果进行测试，可以用开头的那些工具。使用不同的模式和设定来得到最好的效果。

但是这种方法没有下面的一种效果好，或者，戏剧性。可以把这种方法混合使用。

## ChatGPT

在此之前我们要知道这些工具是怎么探测出内容是 AI 写的。答案是 复杂度（perplexity）和爆发性（burstiness）。具体一点，人类可能在写到高兴的内容时添加一些细节，这样句子就一边长一边短了。但是 AI 则期望保持长度一致，内容也比较平淡。

此外，AI 太完美了，导致没有半点语法错误，这超过了人类的范畴，不过主要的原因还是上面的那个。

知道了原因，那么我们教 ChatGPT 做这件事吧。

> When it comes to writing content, two factors are crucial, "perplexity" and "burstiness". Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?

写完可以使用开头的工具验证一下。

### Orignal Text

```txt
As a large language model trained by OpenAI, ChatGPT has the potential to revolutionize the real estate industry by providing instant and accurate information to homebuyers and sellers, agents, and brokers. With its vast knowledge base, natural language processing capabilities, and ability to learn and adapt to new data, ChatGPT can provide an unprecedented level of support and insight to all parties involved in real estate transactions.

One of the key ways ChatGPT can help revolutionize the real estate industry is by providing instant information to homebuyers and sellers. With its ability to understand and interpret natural language, ChatGPT can answer questions and provide relevant information about properties, neighborhoods, and the buying and selling process itself. This can save time and effort for both buyers and sellers, who can quickly get the information they need without having to spend hours researching or contacting real estate agents.

In addition to providing information to buyers and sellers, ChatGPT can also assist real estate agents and brokers in a number of ways. For example, it can help agents quickly analyze market trends and provide insights into which properties are likely to sell quickly or for the best price. It can also help agents manage their schedules and communications with clients, allowing them to focus on building relationships and closing deals.

Overall, ChatGPT has the potential to revolutionize the real estate industry by providing faster, more accurate, and more personalized support to all parties involved in buying and selling homes. Whether you’re a homebuyer or seller, agent or broker, ChatGPT can help you navigate the complex world of real estate with greater ease and confidence than ever before.
```

### Rewrited Text

```txt
As an AI-powered system, ChatGPT holds immense potential to instigate a revolution in the real estate industry by offering instantaneous and accurate information to homebuyers, sellers, agents, and brokers. Equipped with a massive knowledge base, natural language processing capabilities, and an innate capacity to learn and adapt to new data, ChatGPT presents an unparalleled level of support and insight to all parties involved in real estate transactions.

The provision of instant information is a prime means by which ChatGPT can aid in revolutionizing the real estate industry. Through its prowess in comprehending and interpreting natural language, ChatGPT can answer questions and provide pertinent information about properties, neighborhoods, and the buying and selling process, thereby obviating the need for protracted research or communication with real estate agents. This capability can save buyers and sellers significant time and effort while also allowing them to receive the necessary information with ease and immediacy.

Apart from supporting buyers and sellers, ChatGPT can also lend a hand to real estate agents and brokers in various ways. For instance, it can help agents expeditiously analyze market trends and deliver insights into which properties are likely to sell quickly or for the best price. Additionally, ChatGPT can aid agents in managing their schedules and interactions with clients, empowering them to concentrate on building relationships and securing deals.

All in all, ChatGPT’s exceptional qualities equip it to spearhead a transformation in the real estate industry, endowing it with the capacity to provide faster, more accurate, and personalized support to all parties involved in buying and selling homes. Whether one is a homebuyer or seller, agent or broker, ChatGPT can assist in navigating the labyrinthine world of real estate with unprecedented ease and confidence, ushering in a new era of innovation and efficiency in the industry.
```

完整对话示例见文尾。

## End

我认为，对于任何重要的写作，比如正儿八经的科研，法律文书等等。使用 AI 随手生成一堆内容然后发布是非常不负责的行为。

首先，现阶段 AI 创作的内容是已有信息的综合，不会拓宽人类知识的边界。

其次，现阶段 AI 的边界就是可信度。你让它写一封邮件，那你扫一眼就能验证其可靠性，但是比如是一个你不知道的法律条文呢，你和别人能够承受搞错带来的后果吗？AI 能代替你坐牢吗？

就算是其他不重要的应用，我觉得还能能不灌水就不灌水，要是互联网充满这样的内容，那么预料质量就不会好，未来训练新的模型效果也不会好。对于这种问题，希望大家有自己的格局和价值观判断。

## Example

以下是一个 ChatGPT 的例子。

### 原始输出

***

Model: Default

***

> I'm going to give you some information before asking you to write an article. Do you understand?

***

Yes, I understand. You can provide me with any information you would like me to use in the article.

***

> When it comes to writing content, two factors are crucial, "perplexity" and "burstiness". Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?

***

Yes, I understand. I will keep the concepts of perplexity and burstiness in mind when writing the article to ensure that the content has the desired level of complexity and variation.

***

> Use the concepts written previously, rewrite this article with a high degree of perplexity and burstiness: 
> 
> As a large language model trained by OpenAI, ChatGPT has the potential to revolutionize the real estate industry by providing instant and accurate information to homebuyers and sellers, agents, and brokers. With its vast knowledge base, natural language processing capabilities, and ability to learn and adapt to new data, ChatGPT can provide an unprecedented level of support and insight to all parties involved in real estate transactions.
> 
> One of the key ways ChatGPT can help revolutionize the real estate industry is by providing instant information to homebuyers and sellers. With its ability to understand and interpret natural language, ChatGPT can answer questions and provide relevant information about properties, neighborhoods, and the buying and selling process itself. This can save time and effort for both buyers and sellers, who can quickly get the information they need without having to spend hours researching or contacting real estate agents.
> 
> In addition to providing information to buyers and sellers, ChatGPT can also assist real estate agents and brokers in a number of ways. For example, it can help agents quickly analyze market trends and provide insights into which properties are likely to sell quickly or for the best price. It can also help agents manage their schedules and communications with clients, allowing them to focus on building relationships and closing deals.
> 
> Overall, ChatGPT has the potential to revolutionize the real estate industry by providing faster, more accurate, and more personalized support to all parties involved in buying and selling homes. Whether you're a homebuyer or seller, agent or broker, ChatGPT can help you navigate the complex world of real estate with greater ease and confidence than ever before.

***

As an AI-powered system, ChatGPT holds immense potential to instigate a revolution in the real estate industry by offering instantaneous and accurate information to homebuyers, sellers, agents, and brokers. Equipped with a massive knowledge base, natural language processing capabilities, and an innate capacity to learn and adapt to new data, ChatGPT presents an unparalleled level of support and insight to all parties involved in real estate transactions.

The provision of instant information is a prime means by which ChatGPT can aid in revolutionizing the real estate industry. Through its prowess in comprehending and interpreting natural language, ChatGPT can answer questions and provide pertinent information about properties, neighborhoods, and the buying and selling process, thereby obviating the need for protracted research or communication with real estate agents. This capability can save buyers and sellers significant time and effort while also allowing them to receive the necessary information with ease and immediacy.

Apart from supporting buyers and sellers, ChatGPT can also lend a hand to real estate agents and brokers in various ways. For instance, it can help agents expeditiously analyze market trends and deliver insights into which properties are likely to sell quickly or for the best price. Additionally, ChatGPT can aid agents in managing their schedules and interactions with clients, empowering them to concentrate on building relationships and securing deals.

All in all, ChatGPT's exceptional qualities equip it to spearhead a transformation in the real estate industry, endowing it with the capacity to provide faster, more accurate, and personalized support to all parties involved in buying and selling homes. Whether one is a homebuyer or seller, agent or broker, ChatGPT can assist in navigating the labyrinthine world of real estate with unprecedented ease and confidence, ushering in a new era of innovation and efficiency in the industry.

***

### 评论

最后输出的文章在开头所有的工具中都通过了测试，几乎是 100% Human 的结果，即便是 OpenAI 自己提供的，答案也是：

The classifier considers the text to be **unclear if it is** AI-generated.

而我自己写的一段测试，也就 80% 到 90% Human 的水平。不禁让我想到一个毕业生的吐槽，他毕业做了个检测图片是不是 AI 生成的算法，还好做得早，再晚两年就毕业不了了。