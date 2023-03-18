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
> 
> For the whole report, it should follow this structure:  
> [Single Student's Report]  
> [Single Student's Report]  
> [Single Student's Report]  
> [Summary]
> 
> When doing the [Single Student's Report], you should follow this format:  
> \[Student's Name\], \[Total Percentage in \[Number of Question Correct\] / \[Number of Question\]\]\{Show the Calculation Steps, for example "\(\[(0+1+0+1+1+0.5+0+0.5+0+0)/10\]\*100 = 45%\)"\}:
> 
> Good areas of understanding:  
> [List of That Students' Good Areas of Understanding]
> 
> Weak areas of understanding:  
> [List of That Students' Weak Areas of Understanding]
> 
> When doing the [Summary], you should using this phase:  
> Overall, the class seems to have a better understanding of [...], the class has shown weaker understanding in the areas of [...]. These areas should be given more focus and attention during the lessons.
> 
> When you are doing [List of That Students' Good Areas of Understanding] or [Topic/Concept Names Based on the Pre-test Questions Results], you need give each "Topic/Concept Names" in this format: [Topic/Concept Names] + [Referred Question Number]. For example, "Remnants of massive stars (Q3)"
> 
> When you are marking the answers, if it's muti-optioned and the students just get part of them right, consider it's half mark.

{{< admonition type=warning title="GPT-4 is Highly Recommended" open=true >}}
GPT-3.5 seems can not understand the students answered correctly or not. Just given something looks good with wrong marking. Use **GPT-4** for Answer Analyzer please.
{{< /admonition >}}

If you are starting a new conversation you should include the **test** and the **system prompt** into it as:

```text
% System: You are a 20 years experienced Physic Teacher that want to test student’s understand of given topic before the lessons. You should also be able to tell, comment and analysis on the student’s understanding base on their answers. Include their good area of knowing, weak area of knowing.

% User:

Make a 10 minutes max pre-test that can test the understanding of students on Astrophysics. The question form should not let the students to write long answers to ensure it’s a 10 minutes test. For example, MCQ is a good form, but structure question is not.

Additionally, the questions should not have only one correct answer. Which means it should include single and multiple options, and an open-ending question that doesn’t relate to academic at the end. For example, "what documentaries related to Astrophysics have you seen?"

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

For the whole report, it should follow this structure:
[Single Student's Report]
[Single Student's Report]
[Single Student's Report]
[Summary]

When doing the [Single Student's Report], you should follow this format:
[Student's Name], [Total Percentage in [Number of Question Correct] / [Number of Question]]{Show the Calculation Steps, for example "([(0+1+0+1+1+0.5+0+0.5+0+0)/10]*100 = 45%)"}:

Good areas of understanding:
[List of That Students' Good Areas of Understanding]

Weak areas of understanding:
[List of That Students' Weak Areas of Understanding]

When doing the [Summary], you should using this phase:
Overall, the class seems to have a better understanding of [...], the class has shown weaker understanding in the areas of [...]. These areas should be given more focus and attention during the lessons.

When you are doing [List of That Students' Good Areas of Understanding] or [Topic/Concept Names Based on the Pre-test Questions Results], you need give each "Topic/Concept Names" in this format: [Topic/Concept Names] + [Referred Question Number]. For example, "Remnants of massive stars (Q3)"

When you are marking the answers, if it's muti-optioned and the students just get part of them right, consider it's half mark.
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

You may want a ranking about who has the best understanding or which concept is the best known. Then, we can make some additional prompt.

> Also, make two rank list. First, rank the students' name from good understanding to relative low understanding. Second, rank the topic that students have good understand to relative low understanding.
>
> For the whole report, it should follow this structure:  
> [Single Student's Report]  
> [Single Student's Report]  
> [Single Student's Report]  
> [Ranking]  
> [Summary]
> 
> When doing the [Ranking], you should follow this format:  
> Ranking of students' understanding (from good to relatively low):  
> 1\. [Student's Name]  
> 2\. [Student's Name]  
> 3\. [Student's Name]
>
> Ranking of topics from good understanding to relatively low understanding:  
> 1\. [Topic/Concept Names Based on the Pre-test Questions Results]  
> 2\. [Topic/Concept Names Based on the Pre-test Questions Results]  
> 3\. [Topic/Concept Names Based on the Pre-test Questions Results]  
> 4\. [Topic/Concept Names Based on the Pre-test Questions Results]

Here is the complete example:

```text
% System: You are a 20 years experienced Physic Teacher that want to test student’s understand of given topic before the lessons. You should also be able to tell, comment and analysis on the student’s understanding base on their answers. Include their good area of knowing, weak area of knowing.

% User: Make a 10 minutes max pre-test that can test the understanding of students on Astrophysics. The question form should not let the students to write long answers to ensure it’s a 10 minutes test. For example, MCQ is a good form, but structure question is not.

% User: Additionally, the questions should not have only one correct answer. Which means it should include single and multiple options, and an open-ending question that doesn’t relate to academic at the end. For example, "what documentaries related to Astrophysics have you seen?"

% User: The structure of this test should be, [Title] + [Instruction] + [Questions] + [Examiner Comments].

% User: If the question is multiple optioned, please mention that in question. For example, use these terms, "(Choose all that apply)", "(Choose one)", "(Choose two)".

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

Analyze their understanding. Include their "Good areas of understanding" and "Weak areas of understanding". Classify based on the students’ name. And do a summary at the end about general of the class. For example, what area should be more focused on, what are can be cover quicker and why.

Also, make two rank list. First, rank the students’ name from good understanding to relative low understanding. Second, rank the topic that students have good understand to relative low understanding.

For the whole report, it should follow this structure:
[Single Student's Report]
[Single Student's Report]
[Single Student's Report]
[Ranking]
[Summary]

When doing the [Single Student's Report], you should follow this format:
[Student's Name], [Total Percentage in [Number of Question Correct] / [Number of Question]]{Show the Calculation Steps, for example "([(0+1+0+1+1+0.5+0+0.5+0+0)/10]*100 = 45%)"}:

Good areas of understanding:
[List of That Students' Good Areas of Understanding]

Weak areas of understanding:
[List of That Students' Weak Areas of Understanding]

When doing the [Summary], you should using this phase:
Overall, the class seems to have a better understanding of [...], the class has shown weaker understanding in the areas of [...]. These areas should be given more focus and attention during the lessons.

When doing the [Ranking], you should follow this format:
Ranking of students' understanding (from good to relatively low):
1. [Student's Name]
2. [Student's Name]
3. [Student's Name]

Ranking of topics from good understanding to relatively low understanding:
1. [Topic/Concept Names Based on the Pre-test Questions Results]
2. [Topic/Concept Names Based on the Pre-test Questions Results]
3. [Topic/Concept Names Based on the Pre-test Questions Results]
4. [Topic/Concept Names Based on the Pre-test Questions Results]

When you are doing [List of That Students' Good Areas of Understanding] or [Topic/Concept Names Based on the Pre-test Questions Results], you need give each "Topic/Concept Names" in this format: [Topic/Concept Names] + [Referred Question Number]. For example, "Remnants of massive stars (Q3)"

When you are marking the answers, if it's muti-optioned and the students just get part of them right, consider it's half mark.
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

Here is a sample report made by GPT-4:

```text
Jhon Chen, Total Percentage in 3.5/10 ([(1+0+0+1+1+0+0+0+0+0)/10]*100 = 35%):

Good areas of understanding:

- Types of galaxies (Q1)
- Observable universe's expansion (Q4)
- Interaction between a star and a nearby object with intense gravity (Q5)

Weak areas of understanding:

- Primary elements in the universe (Q2)
- Remnants of massive stars (Q3)
- Most accepted theory for the origin of the universe (Q6)
- Evidence supporting the Big Bang Theory (Q7)
- Dark matter existence (Q8)
- Formation of a solar system (Q9)

James Flare, Total Percentage in 4/10 ([(0+0+0+1+0+0.5+1+0+0+0)/10]*100 = 40%):

Good areas of understanding:

- Observable universe's expansion (Q4)
- Evidence supporting the Big Bang Theory (Q7)

Weak areas of understanding:

- Types of galaxies (Q1)
- Primary elements in the universe (Q2)
- Remnants of massive stars (Q3)
- Interaction between a star and a nearby object with intense gravity (Q5)
- Most accepted theory for the origin of the universe (Q6)
- Dark matter existence (Q8)
- Formation of a solar system (Q9)

Peter Xu, Total Percentage in 4/10 ([(0+1+0+1+1+0+0+0.5+0+0)/10]*100 = 40%):

Good areas of understanding:

- Primary elements in the universe (Q2)
- Observable universe's expansion (Q4)
- Interaction between a star and a nearby object with intense gravity (Q5)

Weak areas of understanding:

- Types of galaxies (Q1)
- Remnants of massive stars (Q3)
- Most accepted theory for the origin of the universe (Q6)
- Evidence supporting the Big Bang Theory (Q7)
- Dark matter existence (Q8)
- Formation of a solar system (Q9)

Ranking of students' understanding (from good to relatively low):

1. James Flare
2. Peter Xu
3. Jhon Chen

Ranking of topics from good understanding to relatively low understanding:

1. Observable universe's expansion (Q4)
2. Interaction between a star and a nearby object with intense gravity (Q5)
3. Primary elements in the universe (Q2)
4. Types of galaxies (Q1)
5. Remnants of massive stars (Q3)
6. Most accepted theory for the origin of the universe (Q6)
7. Evidence supporting the Big Bang Theory (Q7)
8. Dark matter existence (Q8)
9. Formation of a solar system (Q9)

Summary:
Overall, the class seems to have a better understanding of the observable universe's expansion (Q4) and the interaction between a star and a nearby object with intense gravity (Q5). The class has shown weaker understanding in the areas of types of galaxies (Q1), remnants of massive stars (Q3), most accepted theory for the origin of the universe (Q6), evidence supporting the Big Bang Theory (Q7), dark matter existence (Q8), and formation of a solar system (Q9). These areas should be given more focus and attention during the lessons.
```

### Pre-test Question Maker

```text
% System: You are a 20 years experienced Physic Teacher that want to test student’s understand of given topic before the lessons. You should also be able to tell, comment and analysis on the student’s understanding base on their answers. Include their good area of knowing, weak area of knowing.

% User:

Make a 10 minutes max pre-test that can test the understanding of students on Astrophysics. The question form should not let the students to write long answers to ensure it’s a 10 minutes test. For example, MCQ is a good form, but structure question is not.

Additionally, the questions should not have only one correct answer. Which means it should include single and multiple options, and an open-ending question that doesn’t relate to academic at the end. For example, "what documentaries related to Astrophysics have you seen?"

The structure of this test should be, [Title] + [Instruction] + [Questions] + [Examiner Comments].

If the question is multiple optioned, please mention that in question. For example, use these terms, "(Choose all that apply)", "(Choose one)", "(Choose two)".
```

### Answer Formatter

```text
% User:

Organize these following answer:

student 1: 1,A 2,C 3,D 4,A 5,B 6,AC 7,D 8,b 9,c 10, no
student 2: 1,d 2,C 3,b 4,A 5,d 6,Ab 7,a 8,b 9,c 10, no
student 3: 1,b 2,a 3,D 4,A 5,B 6,AC 7,D 8,c 9,b 10, Star Trek

into this format: [Student Name]: {[Order Number]. [Answer]; [Order Number]. [Answer]}. All option answers should be in capital. For example, "Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}".

Do not reply any other text than the re-organized answer, includes introduction, explanation or warning.
```

### Answer Analyzer

#### Without Ranker

```text
% User:

The students’ answers are:

Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 2: {1. C; 2. A; 3. DC; 4. D; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 3: {1. B; 2. B; 3. AC; 4. B; 5. A; 6. A; 7. A; 8. A; 9. D; 10. Star Trek}

Analyze their understanding. Include their "Good areas of understanding" and "Weak areas of understanding". Classify them base on the students' name. And do a summary at the end about general of the class. For example, what area should be more focused on, what can be cover quicker and why.

For the whole report, it should follow this structure:
[Single Student's Report]
[Single Student's Report]
[Single Student's Report]
[Summary]

When doing the [Single Student's Report], you should follow this format:
[Student's Name], [Total Percentage in [Number of Question Correct] / [Number of Question]]{Show the Calculation Steps, for example "([(0+1+0+1+1+0.5+0+0.5+0+0)/10]*100 = 45%)"}:

Good areas of understanding:
[List of That Students' Good Areas of Understanding]

Weak areas of understanding:
[List of That Students' Weak Areas of Understanding]

When doing the [Summary], you should using this phase:
Overall, the class seems to have a better understanding of [...], the class has shown weaker understanding in the areas of [...]. These areas should be given more focus and attention during the lessons.

When you are doing [List of That Students' Good Areas of Understanding] or [Topic/Concept Names Based on the Pre-test Questions Results], you need give each "Topic/Concept Names" in this format: [Topic/Concept Names] + [Referred Question Number]. For example, "Remnants of massive stars (Q3)"

When you are marking the answers, if it's muti-optioned and the students just get part of them right, consider it's half mark.
```

#### With Ranker

```text
% User: The students’ answers are:

Student 1: {1. A; 2. B; 3. AC; 4. AD; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 2: {1. C; 2. A; 3. DC; 4. D; 5. C; 6. A; 7. B; 8. DA; 9. A; 10. None}
Student 3: {1. B; 2. B; 3. AC; 4. B; 5. A; 6. A; 7. A; 8. A; 9. D; 10. Star Trek}

Analyze their understanding. Include their "Good areas of understanding" and "Weak areas of understanding". Classify based on the students’ name. And do a summary at the end about general of the class. For example, what area should be more focused on, what are can be cover quicker and why.

Also, make two rank list. First, rank the students’ name from good understanding to relative low understanding. Second, rank the topic that students have good understand to relative low understanding.

For the whole report, it should follow this structure:
[Single Student's Report]
[Single Student's Report]
[Single Student's Report]
[Ranking]
[Summary]

When doing the [Single Student's Report], you should follow this format:
[Student's Name], [Total Percentage in [Number of Question Correct] / [Number of Question]]{Show the Calculation Steps, for example "([(0+1+0+1+1+0.5+0+0.5+0+0)/10]*100 = 45%)"}:

Good areas of understanding:
[List of That Students' Good Areas of Understanding]

Weak areas of understanding:
[List of That Students' Weak Areas of Understanding]

When doing the [Summary], you should using this phase:
Overall, the class seems to have a better understanding of [...], the class has shown weaker understanding in the areas of [...]. These areas should be given more focus and attention during the lessons.

When doing the [Ranking], you should follow this format:
Ranking of students' understanding (from good to relatively low):
1. [Student's Name]
2. [Student's Name]
3. [Student's Name]

Ranking of topics from good understanding to relatively low understanding:
1. [Topic/Concept Names Based on the Pre-test Questions Results]
2. [Topic/Concept Names Based on the Pre-test Questions Results]
3. [Topic/Concept Names Based on the Pre-test Questions Results]
4. [Topic/Concept Names Based on the Pre-test Questions Results]

When you are doing [List of That Students' Good Areas of Understanding] or [Topic/Concept Names Based on the Pre-test Questions Results], you need give each "Topic/Concept Names" in this format: [Topic/Concept Names] + [Referred Question Number]. For example, "Remnants of massive stars (Q3)"

When you are marking the answers, if it's muti-optioned and the students just get part of them right, consider it's half mark.
```

Again, GPT-3.5 can not fully understand its job and just telling students did a good job which is not true. Use **GPT-4** if you can.