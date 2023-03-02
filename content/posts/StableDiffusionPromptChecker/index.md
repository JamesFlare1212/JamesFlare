---
sulg: "sd-prompt-checker"
title: "Stable Diffusion Prompt Checker"
subtitle: ""
date: 2023-03-02T03:19:19+08:00
draft: false
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "Something is hard to find out the mistakes in the Stable Diffusion prompt. I made up a Python program that can format the input prompt, then output to the fixed prompt screen and copyboard."
keywords: ""
license: ""
comment: true
weight: 0

tags:
- Python
- Stable Diffusion
categories:
- Programing
- Sharing

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "Something is hard to find out the mistakes in the Stable Diffusion prompt. I made up a Python program that can format the input prompt, then output to the fixed prompt screen and copyboard."
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

Something is hard to find out the mistakes in the prompt, includes:

- Number of Bracekts
- Non-english Comma

Or formating:

- Spacing

## Checker

I made up a Python program that can format the input prompt, then output to the fixed prompt screen and copyboard.

```py
import re
import pyperclip

# ANSI escape codes for text color
BLUE = '\033[34m'
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

def replace_non_english_chars(prompt):
    # replace non-English commas and brackets with English equivalents
    prompt = prompt.replace("，", ",")  # Chinese comma
    prompt = prompt.replace("【", "[")  # Chinese left bracket
    prompt = prompt.replace("】", "]")  # Chinese right bracket
    prompt = prompt.replace("（", "(")  # Chinese left parenthesis
    prompt = prompt.replace("）", ")")  # Chinese right parenthesis
    prompt = prompt.replace("｛", "{")  # Chinese left brace
    prompt = prompt.replace("｝", "}")  # Chinese right brace
    return prompt

def replace_bad_weights(prompt):
    prompt = prompt.replace(" 1,", ":1.")
    prompt = prompt.replace(" 0,", ":0.")
    #prompt = prompt.replace("1,", ":1.")
    prompt = prompt.replace("0,", ":0.")
    prompt = prompt.replace("0,", ":0.")
    prompt = prompt.replace(" :", ":")
    prompt = prompt.replace(": ", ":")
    prompt = prompt.replace(").", "),")
    prompt = prompt.replace(".(", ",(")
    prompt = prompt.replace(" )", ")")
    prompt = prompt.replace(",)", "),")
    prompt = prompt.replace("].", "],")
    prompt = prompt.replace(".[", ",[")
    prompt = prompt.replace(" ]", "]")
    prompt = prompt.replace(",]", "],")
    prompt = prompt.replace("}.", "},")
    prompt = prompt.replace(".{", ",{")
    prompt = prompt.replace(" }", "}")
    prompt = prompt.replace(",}", "},")
    prompt = prompt.replace(",,", ",")
    return prompt

def prompt_checker(prompt):
    # Step -1: replace non-English commas and brackets with English equivalents
    prompt = replace_non_english_chars(prompt)
    # Step 0: fix bad weights
    prompt = replace_bad_weights(prompt)

    # Step 1: get prompt parts between english commas
    prompt_parts = re.findall("(?<=,)([^,]+)(?=,)", prompt)
    # add back first and last prompt parts with single comma
    prompt_parts.insert(0, prompt.split(",")[0])
    prompt_parts.append(prompt.split(",")[-1])

    # Step 2: remove spaces on both sides of prompt parts
    for i in range(len(prompt_parts)):
        prompt_parts[i] = prompt_parts[i].strip()

    # Step 3: make bracket number on both sides equal
    for i in range(len(prompt_parts)):
        left_parentheses = prompt_parts[i].count("(")
        left_braces = prompt_parts[i].count("{")
        left_brackets = prompt_parts[i].count("[")
        right_parentheses = prompt_parts[i].count(")")
        right_braces = prompt_parts[i].count("}")
        right_brackets = prompt_parts[i].count("]")
        if left_parentheses != right_parentheses:
            max_parentheses = max(left_parentheses, right_parentheses)
            left_diff = max_parentheses - left_parentheses
            right_diff = max_parentheses - right_parentheses
            left_brackets = "(" * left_diff
            right_brackets = ")" * right_diff
            prompt_parts[i] = left_brackets + prompt_parts[i] + right_brackets
        elif left_braces != right_braces:
            max_braces = max(left_braces, right_braces)
            left_diff = max_braces - left_braces
            right_diff = max_braces - right_braces
            left_brackets = "{" * left_diff
            right_brackets = "}" * right_diff
            prompt_parts[i] = left_brackets + prompt_parts[i] + right_brackets
        elif left_brackets != right_brackets:
            max_brackets = max(left_brackets, right_brackets)
            left_diff = max_brackets - left_brackets
            right_diff = max_brackets - right_brackets
            left_brackets = "[" * left_diff
            right_brackets = "]" * right_diff
            prompt_parts[i] = left_brackets + prompt_parts[i] + right_brackets

    # Step 4: join prompt parts with english comma and space
    fixed_prompt = ", ".join(prompt_parts)

    # Step 5: copy fixed prompt to clipboard
    pyperclip.copy(fixed_prompt)

    return fixed_prompt

while True:
    try:
        prompt = input(f"{BLUE}Enter a prompt: {RESET}")
        fixed_prompt = prompt_checker(prompt)
        print(f"{GREEN}Fixed prompt: {RESET}{fixed_prompt}\n")
    except KeyboardInterrupt:
        print(f"{RED}Program interrupted by user. Exiting...{RESET}")
        break
```

It works like

```txt
Enter a prompt: (((crystals texture Hair)))，{{{{{extremely detailed CG}}}}},{{8k_wallpaper}},{{{{Crystalline purple gemstone gloves}}}},((beautiful detailed Glass hair)),((Glass shaped texture hand)),((Crystallize texture body)),Gem body,Hands as clear as jewels,Crystallization of clothes,((crystals texture skin)),sparkle, lens flare, light leaks, Broken glass，{{{{Detailed Glass shaped clothes}}}}， ((masterpiece)), (((best quality))), ((ultra-detailed)), ((illustration)), ((disheveled hair)), ((frills)), (1 girl), (solo), dynamic angle, big top sleeves, floating, beautiful detailed gemstone sky, gemstone sea, beautiful detailed eyes, overexposure, side blunt bangs, hairs between eyes, ribbons, bowties, buttons, bare shoulders, (((small breast))), pleated skirt, crystals texture flowers， ((Detailed crystallized clothing)),(gemstone of body)，solo focus,{{{{{{{{Iridescence and rainbow hair:2.5}}}}}}},{{{{{{detailed cute anime face}}}}}},{{loli}},{{{{{watercolor_(medium)}}}},(((masterpiece))),(((clock))),(((red))),(((blood))),finely detail,Depth of field,Blood drop,Blood fog
Fixed prompt: (((crystals texture Hair))), {{{{{extremely detailed CG}}}}}, {{8k_wallpaper}}, {{{{Crystalline purple gemstone gloves}}}}, ((beautiful detailed Glass hair)), ((Glass shaped texture hand)), ((Crystallize texture body)), Gem body, Hands as clear as jewels, Crystallization of clothes, ((crystals texture skin)), sparkle, lens flare, light leaks, Broken glass, {{{{Detailed Glass shaped clothes}}}}, ((masterpiece)), (((best quality))), ((ultra-detailed)), ((illustration)), ((disheveled hair)), ((frills)), (1 girl), (solo), dynamic angle, big top sleeves, floating, beautiful detailed gemstone sky, gemstone sea, beautiful detailed eyes, overexposure, side blunt bangs, hairs between eyes, ribbons, bowties, buttons, bare shoulders, (((small breast))), pleated skirt, crystals texture flowers, ((Detailed crystallized clothing)), (gemstone of body), solo focus, {{{{{{{{Iridescence and rainbow hair:2.5}}}}}}}}, {{{{{{detailed cute anime face}}}}}}, {{loli}}, {{{{{watercolor_(medium)}}}}}, (((masterpiece))), (((clock))), (((red))), (((blood))), finely detail, Depth of field, Blood drop, Blood fog
```

You can copy the source code into a .py file.

## File

Or you can download it.

{{< link href="promptChecker.py" content="promptChecker.py" title="Download for promptChecker.py" download="promptChecker.py" card=true >}}

I tested with Python3.10.6 on Windows 11 only.

## Before Running

Make sure you have `pyperclip` installed.

```shell
pip install pyperclip
```

Or remove the copyboard function on Line 69

```py
    # Step 5: copy fixed prompt to clipboard
    pyperclip.copy(fixed_prompt)
```

and `import` of `pyperclip`

```py
import pyperclip
```

Welcome to give feedbacks and issues to help me improve!