from util import prep_input


# ref. Got some help for part I from https://www.youtube.com/watch?v=FXQWIWHaFBE


test = prep_input('day7_t.txt')
input = prep_input('day7.txt')

def compute_dir_sizes(input: list) -> dict:
    path = '/home'
    dir_sizes = {'/home': 0}

    while len(input) > 0:
        line = input.pop(0)

        if line == '$ ls':
            while len(input) > 0 and '$' not in input[0]:
                info_line = input.pop(0)
                size_or_dir = info_line.split(' ')[0]
                if size_or_dir != 'dir':
                    size = int(size_or_dir)

                    # Impute size to all parent directories
                    dir_path = path
                    for i in range(path.count('/')):
                        dir_sizes[dir_path] += size
                        dir_path = dir_path[:dir_path.rfind('/')]

        elif line == '$ cd /':
            path = '/home'

        elif line == '$ cd ..':
            path = path[: path.rfind('/')]

        else:
            dir_name = line.split(' ')[-1]
            path += '/' + dir_name
            dir_sizes[path] = 0

    return dir_sizes


def find_answer(size_dict: dict, threshold=100000) -> int:
    answer = 0
    for k, v in size_dict.items():
        if v <= threshold:
            answer += v
    return answer


size_dict = compute_dir_sizes(input)
answer = find_answer(size_dict)

#--- Part Two ---

total_disk = 70000000
unused_target = 30000000

unused_current = total_disk - size_dict['/home']
delete_size = unused_target - unused_current

def find_del_directory(size_dict: dict, delete_size: int) -> int:
    min_size = total_disk
    for k, v in size_dict.items():
        if v > delete_size and v < min_size:
            min_size = v
    return min_size


answer_2 = find_del_directory(size_dict, delete_size)
