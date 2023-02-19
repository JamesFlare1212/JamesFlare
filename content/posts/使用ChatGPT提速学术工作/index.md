---
slug: "chatgpt-guide"
title: "使用 ChatGPT 提速日常工作以及示例"
subtitle: ""
date: 2023-02-18T00:34:20+08:00
draft: true
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "在我们的日常学术工作中，我们会遇到各种各样的任务。比如，写作任务，阅读任务，文本处理，代码任务。使用 ChatGPT 可以对传统的工作流造成降维打击。"
keywords: ""
license: ""
comment: true
weight: 0

tags:
- AI
- ChatGPT
categories:
- Tutorials

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "在我们的日常学术工作中，我们会遇到各种各样的任务。比如，写作任务，阅读任务，文本处理，代码任务。使用 ChatGPT 可以对传统的工作流造成降维打击。"
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

{{< admonition type=notification title="Before Read" open=true >}}
这篇文章更多的是解释说明，并没有实际使用 Prompt 的例子。

虽然这些 Prompt 确实被我大量使用，好评！

但是有可能难以理解。如果大家感兴趣，可以提意见，我稍后更新例子。
{{< /admonition >}}

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

***

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

***

如果我们更进一步，给它更多信息，那么我们可以获得更好的效果。

***

简单改写：

> Rewrite and expand on the passage in the style of a college-educated native English speaker. Use simple syntax and idiomatic expressions.

用复杂的句法和词汇改写：

> Rewritete and expand on the passage in the style of an established scholar. Use complex syntax and advanced vocabulary. Make sure the new version is significantly different from the original.

用某某作家/教授的风格改写：

> Rewrite the passage in the style of Steven Pinker.

#### 语法修正

你也可以要求它修正你段落中的错误，并且同时提供修改的原因。

> In the following, I will provide text with mistakes. I want you to answer by doing the following
> 
> \- Display the correction
> 
> \- Display the original text
> 
> \- Provide an explanation for your correction

你当然可以换一种方法提问。

> Please request a paragraph for correction, provide the corrected form, and list each error and how it was corrected.

### AI Writing Tutor

除了传统的思路，我们还能换个角度思考，比如让它告诉你，问题出在哪里。可以让它扮演一位写作老师帮助学生的写作困难，它会给出提升你写作技巧的建议。

> I want you to act as an AI writing tutor. I will provide you with a student who needs help improving their writing and your task is to use artificial intelligence tools, such as natural language processing, to give the student feedback on how they can improve their composition. You should also use your rhetorical knowledge and experience about effective writing techniques in order to suggest ways that the student can better express their thoughts and ideas in written form. My first request is "I need somebody to help me edit my master's thesis."

## Reading Task

阅读也是常见的任务之一，比如

- 概况总结
- 人物特性
- 内容主旨

### Summarize

我们可以让它扮演一个文本分析工具，总结文本内容。

> Act as a text-analysis tool for researchers, students, and professionals, the AI-powered tool will provide quick and accurate answers to questions about a given text. With its advanced NLP techniques, the tool will analyze the context and identify key information, including names, dates, places, and events, providing a clear and concise format for the information. The tool will also be able to understand the tone, style, and themes of the text, allowing users to gain a deeper understanding of the content. Whether for research, studying, or professional use, this tool will be a valuable resource for anyone who needs to understand large amounts of text, making the process more efficient and effective. With its ability to quickly find and present relevant information, users can save time and focus on more important tasks. The tool's user-friendly interface and clear presentation of information will make it accessible to a wide range of users, including those without a background in text analysis.

### Questioning

你可以让它阅读一段文本

> Read this follwing text first:

然后问它关于此文本的内容。不仅如此，你还能要它给出一个 outline，summary，列出不足，列出人物等等。

## Translation

我们可以给它一些背景信息，帮我们翻译。

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

## Text Operation

我想 GraphGPT 是一个很好的例子。

> Given a prompt, extrapolate as many relationships as possible from it and provide a list of updates.
> 
> If an update is a relationship, provide [ENTITY 1, RELATIONSHIP, ENTITY 2]. The relationship is directed, so the order matters.
> 
> If an update is related to a color, provide [ENTITY, COLOR]. Color is in hex format.
> 
> If an update is related to deleting an entity, provide ["DELETE", ENTITY].
> 
> Example:
> prompt: Alice is Bob's roommate. Make her node green.
> updates:
> [["Alice", "roommate", "Bob"], ["Alice", "#00FF00"]]
> 
> prompt:
> updates:

此外，改变叙述人称，风格，顺序，大小写等等，都是基本操作。

***

我另一篇文章 [使用工具以及 ChatGPT 绕过 AI 内容探测](/posts/bypass-ai-detectiontion/) 中的操作

> When it comes to writing content, two factors are crucial, “perplexity” and “burstiness”. Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?

也是一个展现它对文本理解能力很好的例子。

## Coding Task

比如我要它用 Go 写一个画 Sin 图像的程序。

> Show me a go program that can display Sine graph, and explain all functions, packeages, and concepts that had been used. Don't forget to add comments in English as well.

很快就做好了

```go
package main

import (
    "math"
    "gonum.org/v1/plot"
    "gonum.org/v1/plot/plotter"
    "gonum.org/v1/plot/vg"
)

func main() {
    // Create a new plot
    p, err := plot.New()
    if err != nil {
        panic(err)
    }

    // Set the plot title and labels
    p.Title.Text = "Sin Graph"
    p.X.Label.Text = "X"
    p.Y.Label.Text = "Y"

    // Create a new plotter for the sin function
    points := make(plotter.XYs, 0)
    for i := 0; i <= 360; i += 10 {
        rad := float64(i) * math.Pi / 180
        points = append(points, plotter.XY{X: rad, Y: math.Sin(rad)})
    }

    line, err := plotter.NewLine(points)
    if err != nil {
        panic(err)
    }
    p.Add(line)

    // Save the plot to a PNG image file
    if err := p.Save(4*vg.Inch, 4*vg.Inch, "sin.png"); err != nil {
        panic(err)
    }
}
```

***

或者做一个复杂一点的。

> Write a python program that
> 
> 1. Make a PDF file into .txt file
> 2. Slice the .txt file into chunks that each one max to 12000 character
> 3. Output these chunks into a new .txt file

不在话下

```python
import PyPDF2
import os

def pdf_to_text(pdf_file_path):
    # Open the PDF file in read-binary mode
    with open(pdf_file_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Iterate over each page of the PDF and extract its text
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    # Return the extracted text as a string
    return text

def slice_text_into_chunks(text, max_chunk_size):
    # Split the text into chunks of up to max_chunk_size characters
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    return chunks

def output_chunks_to_text_file(chunks, output_file_path):
    # Join the chunks into a single string separated by newline characters
    text = '\n'.join(chunks)

    # Write the text to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(text)

if __name__ == '__main__':
    # Set the paths for the input and output files
    pdf_file_path = 'path/to/input.pdf'
    output_file_path = 'path/to/output.txt'

    # Convert the PDF file to text
    text = pdf_to_text(pdf_file_path)

    # Slice the text into chunks of up to 12000 characters
    max_chunk_size = 12000
    chunks = slice_text_into_chunks(text, max_chunk_size)

    # Output the chunks to a new text file
    output_chunks_to_text_file(chunks, output_file_path)
```

***

反过来操作也是可以的。

````txt
这段代码是干什么的：

```js
fetch("https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?newsong=1&id=7177076625&format=json&inCharset=GB2312&outCharset=utf-8").then(data => data.json()).then(data => {
    console.log(Array.from(data.data.cdlist).flatMap(u => u.songlist).map(m => m.name + " - " + Array.from(m.singer).map(c => c.name).reduce((s1, s2) => s1 + "," + s2)).reduce((s1, s2) => s1 + '\n' + s2))
})
```
````

解释得很好

```txt
这段代码是使用 Fetch API 获取QQ音乐歌单数据并对获取的数据进行处理，最终将歌曲名和歌手名以 "歌曲名 - 歌手名" 的格式打印到控制台中。该代码首先使用 Fetch API 获取数据，然后将获取的 JSON 数据转换为 JavaScript 对象。接着，使用 Array.from 将歌单列表转换为数组，然后使用 flatMap 将所有歌曲放入一个数组中。最后，使用 reduce 将歌曲名和歌手名拼接成字符串，并使用 console.log 打印出来。
```

## Creative

当然，还有一些有趣的应用，比如

### Plagiarism Checker

扮演一个查重工具，还挺有意思的，准确性未知。

> I want you to act as a plagiarism checker. I will write you sentences and you will only reply undetected in plagiarism checks in the language of the given sentence, and nothing else. Do not write explanations on replies. My first sentence is "For computers to behave like humans, speech recognition systems must be able to process nonverbal information, such as the emotional state of the speaker."

### Composer

给你的歌词编写乐曲。

> I want you to act as a composer. I will provide the lyrics to a song and you will create music for it. This could include using various instruments or tools, such as synthesizers or samplers, in order to create melodies and harmonies that bring the lyrics to life. My first request is "I have written a poem named “Hayalet Sevgilim” and need music to go with it."

### Math Teacher

扮演一位数学老师，给你详细解释数学问题。

> I want you to act as a math teacher. I will provide some mathematical equations or concepts, and it will be your job to explain them in easy-to-understand terms. This could include providing step-by-step instructions for solving a problem, demonstrating various techniques with visuals or suggesting online resources for further study. My first request is "I need help understanding how probability works."

### Midjourney Prompt Generator

当你用 Midjourney 创作图像时，困难会遇到一些困难，但是我们可以让 ChatGPT 帮助你把自然语言描述的图像，转化成 Midjourney 擅长理解的 Prompt。

> I want you to act as a prompt generator for Midjourney's artificial intelligence program. Your job is to provide detailed and creative descriptions that will inspire unique and interesting images from the AI. Keep in mind that the AI is capable of understanding a wide range of language and can interpret abstract concepts, so feel free to be as imaginative and descriptive as possible. For example, you could describe a scene from a futuristic city, or a surreal landscape filled with strange creatures. The more detailed and imaginative your description, the more interesting the resulting image will be. Here is your first prompt: "A field of wildflowers stretches out as far as the eye can see, each one a different color and shape. In the distance, a massive tree towers over the landscape, its branches reaching up to the sky like tentacles."

### Smart Domain Name Generator

当你给公司，组织，博客注册域名的时候是不是犯难过？那不如直接让 ChatGPT 给你建议。

> I want you to act as a smart domain name generator. I will tell you what my company or idea does and you will reply me a list of domain name alternatives according to my prompt. You will only reply the domain list, and nothing else. Domains should be max 7-8 letters, should be short but unique, can be catchy or non-existent words. Do not write explanations. Reply "OK" to confirm.

## Tips

在构造自己的 Prompt 时，最重要的是你要提供足够的信息，然后是精准的用词，最后是例子。

你是 xxx，你的任务是 xxx，把 xxx 进行 xxx，你要 xxx，你不要 xxx，如果 xxx，那么 xxx，例子：xxx。如果你明白，那就 xxx。

***

如果在进行文本处理，那么你应该对各种词汇和思路有充足的理解。

类型，outline，list，detailed，capable，filled，replace，informative，shorten，rewrite，summarize；

描述，creative，formal，nature，enjoy，request；

情景，email，article，reflection，summary，review，script；

角色，AI，teacher，developer，doctor，translator，debater，coach，student，examiner；

***

给出流程也是很重要的，最好是以列表呈现。

1. 从 xxx 提取 xxx
2. 把 xxx 进行 xxx
3. 重复第 x 步 x 次
4. 输出 xxx 的 xxx

## End

最后，我想说，只要思想不滑坡，办法总比困难多。最怕的是你不知道如何表达你的想法，这样谁都帮不了你。

{{< admonition type=tip title="After Reading" open=true >}}
整篇文章有些浅尝辄止，一些细节内容我不希望赘述。

大家有疑问可以在下方讨论，你需要一个 GitHub 账号。
{{< /admonition>}}

## Reference

1. [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
2. [ChatGPT 中文调教指南](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)
3. [把英语作文修改到美国大学教授水平？](https://www.bilibili.com/video/BV1eD4y1J7bC/)
4. [The Best Text Analysis Tool](https://discord.com/channels/974519864045756446/1074328960088952983)
5. [Help with Correcting Writing Errors](https://discord.com/channels/974519864045756446/1076305058423124028)
6. [GraphGPT](https://github.com/varunshenoy/graphgpt)
7. [使用工具以及 ChatGPT 绕过 AI 内容探测](/posts/bypass-ai-detectiontion/)