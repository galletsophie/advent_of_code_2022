from util import prep_input
import pandas as pd
import numpy as np

test = """
30373
25512
65332
33549
35390
"""
test_df = pd.Series(test.split()).str.split('', expand=True)
test_df = np.array(test_df.iloc[:, 1:-1].astype('int'))

input = prep_input('day8.txt')
input_df = pd.Series(input).str.split('', expand=True)
input_df = np.array(input_df.iloc[:, 1:-1].astype('int'))


# Visible if it's the max in any direction
def check_visible(np_arr: np.array, i: int, j: int):
    target = np_arr[i, j]
    n = np_arr.shape[0]  # square mat
    # check target compared to numbers left, right, above, below, respectively
    if target > np_arr[i, :j].max() \
            or target > np_arr[i, min(n, j + 1):].max() \
            or target > np_arr[:i, j].max() \
            or target > np_arr[min(i + 1, n):, j].max():
        return True
    else:
        return False


def go_through_mat(np_arr: np.array):
    n = np_arr.shape[0]
    visible_count = 4 * (n - 1)  # edge
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            visible_count += check_visible(np_arr, i, j)
    return visible_count


test_res = go_through_mat(test_df)
res = go_through_mat(input_df)


# --- Part Two ---
def find_dir_score(target: int, direction: list) -> int:
    # return number of trees seen given the tree heights in direction
    # from the current tree height (target)
    score = 0
    for tree_height in direction:
        score += 1
        if tree_height >= target:
            break
    return score


def get_scenic_score(np_arr: np.array, i: int, j: int) -> int:
    # Return the scenic score for given tree
    # (score_left * score_right * score_up * score_down)
    target = np_arr[i, j]
    n = np_arr.shape[0]
    score = 1
    directions = [np_arr[i, :j][::-1],  # left, reversing order to look from given tree towards edge
                  np_arr[i, min(n, j + 1):],
                  np_arr[:i, j][::-1],  # top, reversing order to look from given tree
                  np_arr[min(i + 1, n):, j]]
    for direction in directions:
        dir_score = find_dir_score(target, direction)
        score *= dir_score
    return score


def go_through_mat2(np_arr: np.array) -> int:
    max_scenic_score = 0
    n = np_arr.shape[0]
    for i in range(1, n-1):  # skip edges...
        for j in range(1, n-1):  # ... their score is 0
            score = get_scenic_score(np_arr, i, j)
            if score > max_scenic_score:
                max_scenic_score = score
    return max_scenic_score


test_res = go_through_mat2(test_df)
res = go_through_mat2(input_df)
