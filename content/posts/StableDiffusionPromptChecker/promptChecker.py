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

def prompt_checker(prompt):
    # Step 0: replace non-English commas and brackets with English equivalents
    prompt = replace_non_english_chars(prompt)

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
