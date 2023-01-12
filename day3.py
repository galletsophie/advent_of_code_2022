from util import *

test = prep_input('day3_t.txt')
input = prep_input('day3.txt')


def find_shared_item_type(rucksack_str: str) -> str:
    compartment_cutoff = len(rucksack_str) // 2  # str has even len by default

    for lt in rucksack_str[:compartment_cutoff]:
        if lt in rucksack_str[compartment_cutoff:]:
            return lt


def find_shared_item_priority(shr_item: str) -> int:
    lt_number = ord(shr_item.lower()) - 96
    upper_bonus = shr_item.isupper() * 26
    return lt_number + upper_bonus


def compute_priority_sum(data=input):
    priority_sum = 0
    for rucksack in data:
        shr_item = find_shared_item_type(rucksack)
        shr_item_priority = find_shared_item_priority(shr_item)
        priority_sum += shr_item_priority
    return priority_sum

test_sum = compute_priority_sum(data=test)
result = compute_priority_sum()

# --- Part Two ---
# Could refactor find_shared_item_type() in part I for more elegance and concision

def find_share_item_type_2(three_str_list: list)->str:
    for lt in three_str_list[0]:
        if lt in three_str_list[1] and lt in three_str_list[-1]:
            return lt

def compute_priority_sum2(data=input):
    priority_sum = 0
    for i in range(0, len(data), 3):
        three_rucksacks = data[i:i+3:]
        shr_item = find_share_item_type_2(three_rucksacks)
        shr_item_priority = find_shared_item_priority(shr_item)
        priority_sum += shr_item_priority
    return priority_sum


test_sum = compute_priority_sum2(data=test)
result = compute_priority_sum2()
