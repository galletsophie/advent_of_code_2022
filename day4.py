from util import prep_input
import pandas as pd


def perform_additional_prep(data_list: list) -> pd.DataFrame:
    """Split data into 4 columns, and cast all as int"""
    data = pd.DataFrame(data_list)[0].str.split(',', expand=True)
    data_1 = data[0].str.split('-', expand=True)
    data_2 = data[1].str.split('-', expand=True)
    data = pd.concat([data_1, data_2], axis=1, ignore_index=True)
    return data.astype('int')


def add_is_subset_column(data) -> None:
    first_subset_of_second = (data[0] >= data[2]) & (data[1] <= data[3])
    second_subset_of_first = (data[0] <= data[2]) & (data[1] >= data[3])
    data['is_subset'] = first_subset_of_second | second_subset_of_first
    return None


test = prep_input('day4_t.txt')
test = perform_additional_prep(test)
add_is_subset_column(test)

input = prep_input('day4.txt')
input = perform_additional_prep(input)
add_is_subset_column(input)

print(input['is_subset'].sum())

# --- Part Two ---

def add_overlap_column(data) -> None:
    # Overlap if either of section_1's bounds is between section_2's bounds ...
    first_in_second = (data[0] >= data[2]) & (data[0] <= data[3]) | (data[1] >= data[2]) & (data[1] <= data[3])
    second_in_first = (data[2] >= data[0]) & (data[2] <= data[1]) | (data[3] >= data[0]) & (data[3] <= data[1])
    # ... or either of section_2's bounds is between section_1's bounds
    data['has_overlap'] = first_in_second | second_in_first
    print(data['has_overlap'].sum())
    return None


add_overlap_column(test)
add_overlap_column(input)