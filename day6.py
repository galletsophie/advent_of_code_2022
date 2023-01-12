import pandas as pd
from util import prep_input

test = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
input = prep_input('day6.txt')[0]


def find_first_marker(input_str: str, chr_count=4) -> int:
    for i in range(len(input_str)):
        chr_stack = input_str[i:i+chr_count]
        ltr_count = sum([chr_stack.count(ltr) for ltr in chr_stack])
        if ltr_count > chr_count:
            continue
        else:
            return i+chr_count


test_marker = find_first_marker(test)
input_marker = find_first_marker(input)

# --- Part Two ---
# Added chr_count arg to above function
test_marker = find_first_marker(test, chr_count=14)
input_marker = find_first_marker(input, chr_count=14)
