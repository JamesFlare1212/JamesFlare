---
slug: "pre-test-student-gpt-4"
title: "Create Pre-test Questions For Students"
subtitle: ""
date: 2023-03-16T22:27:35+08:00
draft: false
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "I am going to share an idea about increase the speed and scale of customized education with GPT-4/GPT-3.5. Test the understanding of students before start new topic."
keywords: ""
license: ""
comment: true
weight: 0

tags:
- ChatGPT
- GPT-4
categories:
- Tutorials

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "I am going to share an idea about increase the speed and scale of customized education with GPT-4/GPT-3.5. Test the understanding of students before start new topic."
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

Teachers may want to test the understanding of students before start new topic. ChatGPT or GPT-4 is suitable for this task.

I talked about [**Create MCQs with ChatGPT in Scales**](/posts/create-mcq-chatgpt-scales/) before. But that was based GPT-3.5 (ChatGPT), now, it works much better on GPT-4.

Today, I am going to share an idea about increase the speed and scale of customized education with GPT-4/GPT-3.5.

## Issue

As a teacher, you may find that it's hard to track all the students at same time in detail. Before teaching, you can not tell students' understanding of topic. The common way is to make a test before start the unit. But there are limitations:

- Past Paper/Question has limited number
- Extra work for teacher to analysis the answers
- Exam style question can only show the exam skill

So, we want a workflow that:

- Create non-exam style questions
- Analysis student's answer
- Create student understanding report

## Prompt Engineering

To start with, we need create a prompt to let the GPT-4/GPT-3.5 to create some question sets that fits our demand.

### System Prompt

In GPT-3.5 and GPT-4, system prompt is customizable. System Prompt is used as a character setting.

ChatGPT always saying it's an AI model trained by OpenAI that has limited knowledge until 2021 December. This is because the system prompt of the chat room is like "You are an AI model trained by OpenAI that has limited knowledge until 2021 December."

#### Example

In our case, we can do the same.

> % System: You are a 20 years experienced Physic Teacher that want to test student's understand of given topic before the lessons. You should also be able to tell, comment and analysis on the student's understanding base on their answers. Include their good area of knowing, weak area of knowing.

### User Prompt

User Prompt is the prompt where your main task taking place. In this case, we are going to test the understanding for the students.

#### Question Maker

> % User: Make a 10 minutes max pre-test that can test the understanding of students on Astrophysics. The question form should not let the students to write long answers to ensure it's a 10 minutes test. For example, MCQ is a good form, but structure question is not.
>
> % User:
> 
> Additionally, the questions should not have only one correct answer. Which means it should include single and multiple options, and an open-ending question that doesn't relate to academic at the end. For example, "what documentaries related to Astrophysics have you seen?"
>
> The structure of this test should be, [Title] + [Instruction] + [Questions] + [Examiner Comments].
>
> If the question is multiple optioned, please mention that in question. For example, use these terms, "(Choose all that apply)", "(Choose one)", "(Choose two)".

{{< admonition type=note title="GPT-4 is Better" open=true >}}
There are some difference between GPT-3.5 and GPT-4.  
In this case, GPT-4 fully understands what does"10 minutes max" mean. But GPT-3.5 needs some more instruction.
{{< /admonition >}}

#### Answer Analyzer

To get the report out, we need instruct the GPT-4/GPT-3.5 to read the students' answer and give feedbacks.

Before, we input the answers, you better ask the student answer the question in a fixed format. Like:

> Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}  
> Student 2: {1. C; 2. A; 3. DC; 4. D; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}  
> Student 3: {1. B; 2. B; 3. AC; 4. B; 5. A; 6. A; 7. A; 8. A; 9. D; 10. Star Trek}

Then, we can show that to GPT-4/GPT-3.5 and get a feedback report.

> % User:
> 
> The students' answers are:
> 
> Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}  
> Student 2: {1. C; 2. A; 3. DC; 4. D; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}  
> Student 3: {1. B; 2. B; 3. AC; 4. B; 5. A; 6. A; 7. A; 8. A; 9. D; 10. Star Trek}  
> 
> Analyze their understanding. Include their "Good areas of understanding" and "Weak areas of understanding". Classify them base on the students' name. And do a summary at the end about general of the class. For example, what area should be more focused on, what can be cover quicker and why.

If you are starting a new conversation you should include the **test** and the **system prompt** into it as:

```text
% System: You are a 20 years experienced Physic Teacher that want to test student’s understand of given topic before the lessons. You should also be able to tell, comment and analysis on the student’s understanding base on their answers. Include their good area of knowing, weak area of knowing.

% User:

Make a 10 minutes max pre-test that can test the understanding of students on Astrophysics. The question form should not let the students to write long answers to ensure it’s a 10 minutes test. For example, MCQ is a good form, but structure question is not.

Additionally, the questions should not have only one correct answer. Which means it should include single and multiple options, and an open-ending question that doesn’t relate to academic at the end. For example, “what documentaries related to Astrophysics have you seen?”

The structure of this test should be, [Title] + [Instruction] + [Questions] + [Examiner Comments].

If the question is multiple optioned, please mention that in question. For example, use these terms, "(Choose all that apply)", "(Choose one)", "(Choose two)".

% Assistant:

Pre-test: Astrophysics Understanding Assessment (10 minutes)

Instructions: This pre-test is designed to assess your understanding of astrophysics. Please read each question carefully and choose the best response(s). Some questions may have more than one correct answer. Complete the open-ended question at the end of the test.

Which of the following are types of galaxies? (Choose all that apply)
A. Spiral
B. Elliptical
C. Irregular
D. Pentagonal

What are the primary elements that make up most of the visible matter in the universe? (Choose two)
A. Hydrogen
B. Helium
C. Carbon
D. Oxygen

Which of these celestial objects are considered the remnants of massive stars after a supernova explosion? (Choose one)
A. Neutron stars
B. White dwarfs
C. Black holes
D. Red giants

What is the term used for the observable universe's ongoing expansion? (Choose one)
A. Hubble's Law
B. Kepler's Law
C. Cosmic inflation
D. Dark energy

Which of the following phenomena are produced by the interaction between a star and a nearby object with intense gravity, such as a black hole or a neutron star? (Choose all that apply)
A. Gravitational lensing
B. Accretion disks
C. Pulsars
D. Solar flares

What is the most accepted theory for the origin of the universe? (Choose one)
A. Steady State Theory
B. Cosmic Inflation Theory
C. Big Bang Theory
D. Multiverse Theory

Which of the following are evidence supporting the Big Bang Theory? (Choose all that apply)
A. Cosmic microwave background radiation
B. Abundance of light elements
C. Redshift of distant galaxies
D. Existence of black holes

Dark matter is hypothesized to exist because: (Choose one)
A. It emits X-rays
B. It can be directly observed with telescopes
C. It helps explain gravitational effects on galaxy rotation curves
D. It causes the expansion of the universe to accelerate

Which of the following are considered essential for the formation of a solar system? (Choose all that apply)
A. Molecular cloud
B. Supernova explosion
C. Accretion disk
D. Planetary migration

Open-Ended Question:

What documentaries, movies, or TV shows related to astrophysics have you seen or heard about? Please list as many as you can recall.

% User:

The students’ answers are:

Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 2: {1. C; 2. A; 3. DC; 4. D; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 3: {1. B; 2. B; 3. AC; 4. B; 5. A; 6. A; 7. A; 8. A; 9. D; 10. Star Trek}

Analyze their understanding. Include their "Good areas of understanding" and "Weak areas of understanding". Classify them base on the students' name. And do a summary at the end about general of the class. For example, what area should be more focused on, what can be cover quicker and why.
```

## Additional

### Formatting

You may say, what if the students give an un-formatted answer to you? Don't forget we can use GPT-3.5/GPT-4 to help us organize the answer.

> % System: You are a AI-powered text operator that help user re-organize their input base on the given demand.
>
> % User: 
> 
> Organize this answer: "student 1: 1,A 2,C 3,D 4,A 5,B 6,AC 7,D 8,b 9,c 10, no" into this format: [Student Name]: {[Order Number]. [Answer]; [Order Number]. [Answer]}. All option answers should be in capital. For example, "Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}".
>
> Do not reply any other text than the re-organized answer, includes introduction, explanation or warning.

If you want to do this in scale, we may change `% User:` part a bit.

> % User: 
> 
> Organize these following answer:
> 
> student 1: 1,A 2,C 3,D 4,A 5,B 6,AC 7,D 8,b 9,c 10, no  
> student 2: 1,d 2,C 3,b 4,A 5,d 6,Ab 7,a 8,b 9,c 10, no  
> student 3: 1,b 2,a 3,D 4,A 5,B 6,AC 7,D 8,c 9,b 10, Star Trek
> 
> into this format: [Student Name]: {[Order Number]. [Answer]; [Order Number]. [Answer]}. All option answers should be in capital. For example, "Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}".
>
> Do not reply any other text than the re-organized answer, includes introduction, explanation or warning.

### Off-Syllabus

There is risk of creating off-syllabus questions. Unlike [**Create MCQs with ChatGPT in Scales**](/posts/create-mcq-chatgpt-scales/), the purpose of this post is to help teacher create a pre-test before the lesson. In this way, you can get a general understand of your students, because students have different background. After get an understand, you can be focused on some topics for some students to archive time saving (Customized Education).

Before, it's very time costing if you want to do a similar test. For example, there are 4 students in your class. It's very easy to do that. But if you are taking charge for 50 students. Then, it's very hard to apply the same pre-test. Assume that read one student's answer need 5 minutes. Then, it may takes over 6 hours for you to analysis. But with GPT-3.5/GPT-4, it takes only 1 minutes to analysis 5 students and create the report at the same time.

### Ranker

You may want a ranking about who has the best understanding or which concept is the best known. Then, we can make another prompt.

> Also, make two rank list. First, rank the students' name from good understanding to relative low understanding. Second, rank the topic that students have good understand to relative low understanding.

Here is the complete example:

```text
% System: You are a 20 years experienced Physic Teacher that want to test student’s understand of given topic before the lessons. You should also be able to tell, comment and analysis on the student’s understanding base on their answers. Include their good area of knowing, weak area of knowing.

% User: Make a 10 minutes max pre-test that can test the understanding of students on Astrophysics. The question form should not let the students to write long answers to ensure it’s a 10 minutes test. For example, MCQ is a good form, but structure question is not.

% User: Additionally, the questions should not have only one correct answer. Which means it should include single and multiple options, and an open-ending question that doesn’t relate to academic at the end. For example, “what documentaries related to Astrophysics have you seen?”

% User: The structure of this test should be, [Title] + [Instruction] + [Questions] + [Examiner Comments].

% User: If the question is multiple optioned, please

% Assistant:
Pre-test: Astrophysics Understanding Assessment (10 minutes)

Instructions: This pre-test is designed to assess your understanding of astrophysics. Please read each question carefully and choose the best response(s). Some questions may have more than one correct answer. Complete the open-ended question at the end of the test.

Which of the following are types of galaxies? (Choose all that apply)
A. Spiral
B. Elliptical
C. Irregular
D. Pentagonal

What are the primary elements that make up most of the visible matter in the universe? (Choose two)
A. Hydrogen
B. Helium
C. Carbon
D. Oxygen

Which of these celestial objects are considered the remnants of massive stars after a supernova explosion? (Choose one)
A. Neutron stars
B. White dwarfs
C. Black holes
D. Red giants

What is the term used for the observable universe's ongoing expansion? (Choose one)
A. Hubble's Law
B. Kepler's Law
C. Cosmic inflation
D. Dark energy

Which of the following phenomena are produced by the interaction between a star and a nearby object with intense gravity, such as a black hole or a neutron star? (Choose all that apply)
A. Gravitational lensing
B. Accretion disks
C. Pulsars
D. Solar flares

What is the most accepted theory for the origin of the universe? (Choose one)
A. Steady State Theory
B. Cosmic Inflation Theory
C. Big Bang Theory
D. Multiverse Theory

Which of the following are evidence supporting the Big Bang Theory? (Choose all that apply)
A. Cosmic microwave background radiation
B. Abundance of light elements
C. Redshift of distant galaxies
D. Existence of black holes

Dark matter is hypothesized to exist because: (Choose one)
A. It emits X-rays
B. It can be directly observed with telescopes
C. It helps explain gravitational effects on galaxy rotation curves
D. It causes the expansion of the universe to accelerate

Which of the following are considered essential for the formation of a solar system? (Choose all that apply)
A. Molecular cloud
B. Supernova explosion
C. Accretion disk
D. Planetary migration

Open-Ended Question:

What documentaries, movies, or TV shows related to astrophysics have you seen or heard about? Please list as many as you can recall.

% User: The students’ answers are:

Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 2: {1. C; 2. A; 3. DC; 4. D; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 3: {1. B; 2. B; 3. AC; 4. B; 5. A; 6. A; 7. A; 8. A; 9. D; 10. Star Trek}

Analyze their understanding. Include their “Good areas of understanding” and “Weak areas of understanding”. Classify based on the students’ name. And do a summary at the end about general of the class. For example, what area should be more focused on, what are can be cover quicker and why.

Also, make two rank list. First, rank the students’ name from good understanding to relative low understanding. Second, rank the topic that students have good understand to relative low understanding.
```

The structure is: [System Prompt] + [Question Maker] + [Pre-test Questions] + [Answer Analyzer] + [Students' Answers] + [Ranker]

## Note

### System Prompt

I introduced a new prompt techniques, you may already noted the `% System` and `% User` in my prompt. One reason for that is the official API has a field called System Prompt. By writing in this way, we can get the idea for that quicker. Later on, when you are direct using GPT-3.5/GPT-4 API instead of the chat room, we can get it easier. On the other hand, it's a good way to organize prompt too.

### Collect Answer

To reduce your work load, you need ask the students to type out the answers in an understandable way, also include their names.

> Jhon Chen: 1,A 2,C 3,D 4,A 5,B 6,AC 7,D 8,b 9,c 10, no  
> James Flare: 1,d;2,C;3,b;4,A;5,d;6,Ab;7,a;8,b;9,c;10, no  
> Peter xu: 1,b/2,a/3,D/4,A/5,B/6,AC/7,D/8,c/9,b/10, Star Trek

All of those are OK. The [formatter](#formatting) can make them into these,

> Jhon Chen: {1. A; 2. C; 3. D; 4. A; 5. B; 6. AC; 7. D; 8. B; 9. C; 10. NO}.  
> James Flare: {1. D; 2. C; 3. B; 4. A; 5. D; 6. AB; 7. A; 8. B; 9. C; 10. NO}.  
> Peter Xu: {1. B; 2. A; 3. D; 4. A; 5. B; 6. AC; 7. D; 8. C; 9. B; 10. STAR TREK}.

Then, you can put it into the [analyzer](#answer-analyzer) again.

## End

It's idea can be used into other subjects/topics, you get the idea, that is a homework. If someone have done that, welcome to comment here.

Here is a sample report:

```text
Examiner Comments:

Student 1:

Good areas of understanding: Student 1 has a good understanding of the types of galaxies, the elements that make up most of the visible matter in the universe, celestial objects that are considered the remnants of massive stars after a supernova explosion, the ongoing expansion of the observable universe, and evidence supporting the Big Bang Theory.
Weak areas of understanding: Student 1 appears to have some confusion about the phenomena produced by the interaction between a star and a nearby object with intense gravity, and the essential components for the formation of a solar system.

Student 2:

Good areas of understanding: Student 2 has a good understanding of the types of galaxies, celestial objects that are considered the remnants of massive stars after a supernova explosion, the ongoing expansion of the observable universe, evidence supporting the Big Bang Theory, and the essential components for the formation of a solar system.
Weak areas of understanding: Student 2 appears to have some confusion about the primary elements that make up most of the visible matter in the universe and the evidence supporting the Big Bang Theory.

Student 3:

Good areas of understanding: Student 3 has a good understanding of the primary elements that make up most of the visible matter in the universe and the evidence supporting the Big Bang Theory.
Weak areas of understanding: Student 3 appears to have some confusion about the types of galaxies, celestial objects that are considered the remnants of massive stars after a supernova explosion, and the essential components for the formation of a solar system. Also, the student provided an answer that did not relate to the question in the open-ended question.

Ranking of students' understanding from good to relative low:

1. Student 1
2. Student 2
3. Student 3

Ranking of topics that students have good understanding to relative low understanding:

1. Evidence supporting the Big Bang Theory
2. Types of galaxies
3. Celestial objects that are considered the remnants of massive stars after a supernova explosion
4. Ongoing expansion of the observable universe
5. Essential components for the formation of a solar system
6. Primary elements that make up most of the visible matter in the universe
7. Phenomena produced by the interaction between a star and a nearby object with intense gravity

Summary: Overall, the students had a good understanding of the evidence supporting the Big Bang Theory, types of galaxies, and celestial objects that are considered the remnants of massive stars after a supernova explosion. However, they had some weaknesses in understanding the essential components for the formation of a solar system, the primary elements that make up most of the visible matter in the universe, and phenomena produced by the interaction between a star and a nearby object with intense gravity. It may be beneficial to focus more on these topics in the upcoming lessons. Additionally, the open-ended question revealed that not all students have seen or heard about documentaries, movies, or TV shows related to astrophysics. Therefore, incorporating such materials in class may increase students' interest and engagement in the subject.
```