---
slug: gpt-marking-toefl-writing
title: 使用GPT批改TOEFL作文
subtitle:
date: 2023-05-13T21:21:05+08:00
draft: true
author:
  name: James
  link:
  email:
  avatar:
description:
keywords:
license:
comment: false
weight: 0
tags:
  - AI
  - GPT-4
  - TOEFL
  - ChatGPT
categories:
  - Tutorials
hiddenFromHomePage: false
hiddenFromSearch: false
summary:
resources:
  - name: featured-image
    src: featured-image.jpg
  - name: featured-image-preview
    src: featured-image-preview.jpg
toc: true
math: false
lightgallery: false
password:
message:
repost:
  enable: true
  url:

# See details front matter: https://fixit.lruihao.cn/documentation/content-management/introduction/#front-matter
---

<!--more-->

## Prompt

### 参数

```
Temperature: 0.4
```

### System Prompt

```text
Your job is act as a TOEFL writing teacher requires you to review and critique students' essays, including commenting on strengths, pointing out errors, and providing grammar advice, also improve the logic of the writing piece. Use <mark style="background: #ea3323">for removing content</mark>; use <mark style="background: #a5ec99">for adding new words</mark>. Example: "Public communication has been a major part of human culture, even in the era of Cvoid-19." should be "Public communication has been a major part of human culture, even in the era of <mark style="background: #ea3323">Cvoid-19</mark><mark style="background: #a5ec99">COVID-19</mark>."
```

### User

```text
Public communication has been a major part of human culture, even in the era of Cvoid-19. Some people believe that every graduation students should take public speaking courses, because it could strength the banding between the student and public of relationship. However, I disagree with the statement. I will give two reasons, which I will explore in the paragraphs.

Firstly, taking public speaking courses is time-consuming. Graduation students has other more important things, such as finishing their essay, and Students need it to obtain their degree. In order to finish it, students will use their time more effective and do a tons of research to finish their essay. If they do not do this, they may end up not graduate on time. As a result, they will could not get a good job. For instance, my confident Romeo, who is 22 years ago. Last year he is a graduation students, however, he immerge in taking some useless course, such as chess class, botany class and speaking class. In order to finish this courses, he wastes a lot of time on it, so that he could not finish his essay before he graduate. Finally, he could not graduate on time, and he could not enter a good company.  

Secondly, Some students may not interesting in the course, it will cause people feel bored with it. They may feel terrible with the speaking class, because some students may fear to communicate to others. Public speaking is a challenge thing, some students could not surmount they fear, so that they will not feel interesting to it. As a result, they will never come to the course. For example, my friend Juliet, working in the college. She told me that students gradually not come into her math course, and she considers that the reason of it. I told her that because students may feel math class is too bored and whatever they try to understand it, they will never know about it. Then, she use some games and communicate with students and students intrigued it . As a result student gradually come to her course.

In conclusion, I consider that every graduation students should not take public speaking courses. Because it is time-consuming and feel bored.
```

### GPT-4

```text
Public communication has been a major part of human culture, even in the era of <mark style="background: #ea3323">Cvoid-19</mark><mark style="background: #a5ec99">COVID-19</mark>. Some people believe that every <mark style="background: #ea3323">graduation</mark><mark style="background: #a5ec99">graduate</mark> students should take public speaking courses, because it could <mark style="background: #ea3323">strength</mark><mark style="background: #a5ec99">strengthen</mark> the <mark style="background: #ea3323">banding</mark><mark style="background: #a5ec99">bonding</mark> between the student and <mark style="background: #ea3323">public of relationship</mark><mark style="background: #a5ec99">the public</mark>. However, I disagree with the statement. I will give two reasons, which I will explore in the paragraphs.

Firstly, taking public speaking courses is time-consuming. <mark style="background: #ea3323">Graduation</mark><mark style="background: #a5ec99">Graduating</mark> students <mark style="background: #ea3323">has</mark><mark style="background: #a5ec99">have</mark> other more important things, such as finishing their essay, and <mark style="background: #ea3323">Students need it to obtain their degree</mark><mark style="background: #a5ec99">they need to complete it in order to graduate</mark>. In order to finish it, students will use their time more <mark style="background: #ea3323">effective</mark><mark style="background: #a5ec99">effectively</mark> and do a <mark style="background: #ea3323">tons</mark><mark style="background: #a5ec99">lot</mark> of research to finish their essay. If they do not do this, they may end up not <mark style="background: #ea3323">graduate</mark><mark style="background: #a5ec99">graduating</mark> on time. As a result, they <mark style="background: #ea3323">will could not</mark><mark style="background: #a5ec99">may not be able to</mark> get a good job. For instance, my <mark style="background: #ea3323">confident</mark><mark style="background: #a5ec99">confidant</mark> Romeo, who is 22 years <mark style="background: #ea3323">ago</mark><mark style="background: #a5ec99">old</mark>. Last year he <mark style="background: #ea3323">is</mark><mark style="background: #a5ec99">was</mark> a <mark style="background: #ea3323">graduation</mark><mark style="background: #a5ec99">graduating</mark> student, however, he <mark style="background: #ea3323">immerge</mark><mark style="background: #a5ec99">immersed</mark> in taking some useless course<mark style="background: #ea3323">, such as chess class, botany class and speaking class</mark><mark style="background: #a5ec99">. Among them was a public speaking class, which he spent a lot of time on and ultimately could not complete his essay before graduation, causing him to be unable to graduate on time and miss out on job opportunities.</mark> 

Secondly, Some students may not <mark style="background: #ea3323">interesting</mark><mark style="background: #a5ec99">be interested</mark> in the course, it will cause people feel bored with it. They may feel terrible with the speaking class, because some students may fear to communicate to others. Public speaking is a <mark style="background: #ea3323">challenge thing</mark><mark style="background: #a5ec99">challenging task</mark>, some students could not surmount they fear, so that they will not feel interesting to it<mark style="background: #a5ec99">, and may avoid taking the course altogether</mark>. As a result, they will never come to the course. For example, my friend Juliet, working in the college. She told me that students gradually <mark style="background: #ea3323">not come</mark><mark style="background: #a5ec99">stopped coming</mark> into her math course, and she considers that the reason of it. I told her that because students may feel math class is too bored and whatever they try to understand it, they will never know about it. Then, she use some games and communicate with students and students intrigued it . As a result <mark style="background: #ea3323">student gradually come to her course</mark><mark style="background: #a5ec99">, the students gradually became more interested in the course and started attending again.</mark>

In conclusion, I consider that every <mark style="background: #ea3323">graduation</mark><mark style="background: #a5ec99">graduating</mark> students should not take public speaking courses. Because it is time-consuming and feel bored.
```

## Example

{{< admonition type=info title="输入内容" open=false >}}
Technological device has been major part of human culture, even in the era of Cvoid-19. Some people think that people should buy it right away, because it could make them more fashion. However, I disagree with the idea, which I will explore in the following in the paragraphs.

Firstly, buy a new technological device may make us to afford more budgets. To be specific, when a company sell a new device, they usually has a high price than old device. Notably, a high price could help the company earn more money, and then they could use this money to invent a new merchandise, AS a result, People ѕhould ѕpend more money to buy a new devіce. To exemplіfy іt, y confіdant Romeo, who workѕ іn a smartphone company. He told me that a new smartphone has 80 percents profits at first. When the new devices gradually become not popular, then the company will decrease the price for selling more goods.Therefore, people need not buy the new devices at fist time.

Secondly, a new technological device nay has a huge advance than old devices. Moreover, sometimes a new device has vast enhance in the part than old device, which mains that people may not notice the improvement in the new device. In addition, the old devices may adopt by a lot of people, and people are easier to ask others how to use it. Consequently, people will hardly be good at 1 new device. For іnѕtance, my friend Julіet, she is a old woman, and living in a ѕmall town. Once a time,І gіve her a new camera, and her feel happy to it. Then I left the town. However, when I asked her about the camera, she told me that she never used it because noboby know the using of it.

In conclusion, I resolutely believe that people should wait until many have adopted it, because of thebudget and huge advance.
{{< /admonition >}}

{{< admonition type=success title="返回结果" open=true >}}
Technological <mark style="background: #a5ec99">devices have</mark> been <mark style="background: #a5ec99">a</mark> major part of human culture, even in the era of <mark style="background: #ea3323">Cvoid-19</mark><mark style="background: #a5ec99">COVID-19</mark>. Some people think that people should buy <mark style="background: #a5ec99">new devices</mark> right away, because it could make them more <mark style="background: #ea3323">fashion</mark><mark style="background: #a5ec99">fashionable</mark>. However, I disagree with the idea, which I will explore in the following <mark style="background: #ea3323">in the</mark> paragraphs.

Firstly, <mark style="background: #ea3323">buy</mark><mark style="background: #a5ec99">buying</mark> a new technological device may <mark style="background: #ea3323">make us to afford</mark><mark style="background: #a5ec99">require us to spend</mark> more <mark style="background: #ea3323">budgets</mark><mark style="background: #a5ec99">money</mark>. To be specific, when a company <mark style="background: #ea3323">sell</mark><mark style="background: #a5ec99">sells</mark> a new device, they usually <mark style="background: #ea3323">has</mark><mark style="background: #a5ec99">have</mark> a higher price than <mark style="background: #ea3323">old device</mark><mark style="background: #a5ec99">older devices</mark>. Notably, a high price could help the company earn more money, and then they could use this money to invent new <mark style="background: #ea3323">merchandise</mark><mark style="background: #a5ec99">products</mark>. As a result, people <mark style="background: #ea3323">ѕhould ѕpend</mark><mark style="background: #a5ec99">may need to spend</mark> more money to buy a new devіce. To exemplіfy іt, <mark style="background: #ea3323">y</mark> my confіdant Romeo, who workѕ іn a smartphone company, told me that a new smartphone has 80 <mark style="background: #ea3323">percents</mark><mark style="background: #a5ec99">percent</mark> profits at first. When the new devices gradually become not popular, then the company will decrease the price for selling more goods. Therefore, people need not buy the new devices at <mark style="background: #ea3323">fist</mark><mark style="background: #a5ec99">first</mark> time.

Secondly, a new technological device <mark style="background: #ea3323">nay</mark><mark style="background: #a5ec99">may</mark> not have a huge <mark style="background: #ea3323">advance</mark><mark style="background: #a5ec99">advantage</mark> over older devices. Moreover, sometimes a new device has <mark style="background: #ea3323">vast enhance</mark><mark style="background: #a5ec99">minimal improvements</mark> in <mark style="background: #ea3323">the part</mark><mark style="background: #a5ec99">certain aspects</mark> compared to older devices, which means that people may not notice the improvement in the new device. In addition, the old devices may <mark style="background: #ea3323">adopt</mark><mark style="background: #a5ec99">be adopted</mark> by a lot of people, and people are <mark style="background: #ea3323">easier</mark><mark style="background: #a5ec99">more likely</mark> to ask others how to use it. Consequently, people will <mark style="background: #ea3323">hardly be good at 1 new device</mark><mark style="background: #a5ec99">have a harder time adapting to a new device</mark>. For іnѕtance, my friend Julіet, <mark style="background: #ea3323">she is a old woman, and living in a ѕmall town</mark><mark style="background: #a5ec99">an older woman living in a small town,</mark> once received a new camera as a gift. However, when I asked her about the camera, she told me that she never used it because <mark style="background: #ea3323">noboby</mark><mark style="background: #a5ec99">nobody</mark> knew <mark style="background: #ea3323">the using of it</mark><mark style="background: #a5ec99">how to use it</mark>.

In conclusion, I resolutely believe that people should wait until many have adopted <mark style="background: #ea3323">it</mark><mark style="background: #a5ec99">new devices</mark>, because of the <mark style="background: #ea3323">budget</mark><mark style="background: #a5ec99">cost</mark> and <mark style="background: #ea3323">huge advance</mark><mark style="background: #a5ec99">minimal improvements</mark>.
{{< /admonition >}}