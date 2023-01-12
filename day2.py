from util import prep_input

move_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
move_pts_dict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
result_dict = {'Draw': 3, 'Win': 6, 'Lose': 0} #easier for pt II


def decrypt(round_str: str, dict=move_dict) -> list:
    """ Transform an input line into a list of two strings, move names. ex: 'A Z' -> ['Rock', 'Scissors']
    modif for part two: use different dict
    """
    for letter, score in dict.items():
        round_str = round_str.replace(letter, score)
    round_moves = round_str.split(' ')
    return round_moves


def compute_my_score(round_moves: list) -> int:
    """ Return my score for decrypted line"""
    [opp_move, my_move] = round_moves
    my_score = move_pts_dict[my_move]
    if my_move == opp_move:
        my_score += result_dict['Draw']
    elif round_moves in [['Scissors', 'Rock'], ['Rock', 'Paper'], ['Paper', 'Scissors']]:
        my_score += result_dict['Win']
    return my_score


test_input = prep_input('day2_t.txt')
puzzle_input = prep_input('day2.txt')

test_list = [decrypt(line) for line in test_input]
test_score = sum([compute_my_score(move_list) for move_list in test_list])

input_list = [decrypt(line) for line in puzzle_input]
input_score = sum([compute_my_score(move_list) for move_list in input_list])

# --- Part Two ---
move_dict2 = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
move_to_win = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
# Probably a smart way to reuse above dict, but no time
move_to_lose = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

def compute_my_score_2(round_info: list) -> int:
    """ Define my move then return my score for decrypted line"""
    [opp_move, result] = round_info

    if result == 'Draw':
        my_move = opp_move
    elif result == 'Win':
        my_move = move_to_win[opp_move]
    else:
        my_move = move_to_lose[opp_move]

    return move_pts_dict[my_move] + result_dict[result]



test_list = [decrypt(line, dict=move_dict2) for line in test_input]
test_score = sum([compute_my_score_2(move_list) for move_list in test_list])

input_list = [decrypt(line, dict=move_dict2) for line in puzzle_input]
input_score = sum([compute_my_score_2(move_list) for move_list in input_list])