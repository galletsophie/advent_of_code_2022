from util import prep_input
import pandas as pd

def split_data(data_list: list):
    moves = [sentence.strip('\n') for sentence in data_list if sentence[:2] == 'mo']
    layout = [elt.strip('\n') for elt in data_list if elt[:2] != 'mo']
    return moves, layout


def clean_moves(move_list: list) -> pd.DataFrame:
    # Transform list of sentences into df with 3 cols [qty, origin, destination]
    move_series = pd.Series(move_list)
    move_df = move_series.str.split(" ", expand=True)
    move_df = move_df.iloc[:, [1, 3, 5]]  # keep only relevant number cols
    move_df.columns = ['quantity', 'origin', 'destination']
    move_df.quantity = move_df.quantity.astype('int')
    return move_df


def clean_layout(layout_list: list) -> pd.DataFrame:
    """ Transform messy list of str into layout dictionary
    # where the key is the loc name ('1', '2'..)
    # and the value is a list of crates represented by letters, lowest to highest"""

    layout_list = [elt for elt in layout_list if elt != '']
    stacks = [loc for loc in layout_list[-1].split(' ') if loc != '']
    layout_list = [elt.replace('    ', ' _ ') for elt in layout_list[:-1]]
    layout_s = pd.Series([elt.strip(' ').replace('  ', ' ') for elt in layout_list])

    layout_df = layout_s.str.split(' ', expand=True)
    layout_df.columns = stacks

    layout_dic = layout_df.to_dict('list')
    for stack, crate_list in layout_dic.items():
        crate_list.reverse()
        layout_dic[stack] = [elt for elt in crate_list if elt != '_' and elt is not None]

    return layout_dic


def prep_data(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()
    moves, layout = split_data(lines)
    move_df = clean_moves(moves)
    layout_dict = clean_layout(layout)
    return move_df, layout_dict


def perform_a_move(stack_dic: dict, move_row: object, cratemover9000=True):
    nb_crate, origin, destination = move_row
    moving_crates = stack_dic[origin][-nb_crate:]
    if cratemover9000:
        moving_crates.reverse()
    stack_dic[origin] = stack_dic[origin][:-nb_crate]
    stack_dic[destination] = stack_dic[destination] + moving_crates
    return None

def perform_all_moves(stack_dic, move_df, cratemover9000=True):
    for _, row in move_df.iterrows():
        perform_a_move(stack_dic, row, cratemover9000)

    message = ""
    for v in stack_dic.values():
        message += v[-1]
    message = message.replace('[', '').replace(']', '')
    return message


#move_df, layout_dic = prep_data('day5.txt')
#message = perform_all_moves(layout_dic, move_df)


# Part Two
move_df, layout_dic = prep_data('day5.txt')
message = perform_all_moves(layout_dic, move_df, cratemover9000=False)