def format_input(input_txt: str):
    with open(input_txt, 'r') as f:
        lines = f.readlines()
        calory_list = [elt.strip() for elt in lines]
    current_cal_sum = 0
    calory_sums = []
    for cal in calory_list:
        if cal == '':
            calory_sums.append(current_cal_sum)
            current_cal_sum = 0
        else:
            current_cal_sum += int(cal)
    return calory_sums

test_calory_sum = format_input('day1_test.txt')
test_result = max(test_calory_sum)

calory_sum = format_input('day1.txt')
result = max(calory_sum)

# --- Part Two ---
top3_test = sorted(test_calory_sum, reverse=True)[:3]
test_result2 = sum(top3_test)

top3 = sorted(calory_sum, reverse=True)[:3]
result2 = sum(top3)

