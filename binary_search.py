import os
import json

cwd_path = os.getcwd()
file_path = 'files'


def read_data(file_name, key='ordered_numbers'):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), 'r') as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list on numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return

def recursive_binary_search(num_list, value, left_end, right_end):
    middle_idx = (left_end + right_end) // 2

    if num_list[middle_idx] < value:
        recursive_binary_search(num_list, value, middle_idx + 1, right_end)
    elif num_list[middle_idx] > value:
        recursive_binary_search(num_list, value, left_end, middle_idx)
    elif num_list[middle_idx] == value:
        return middle_idx
    else:
        return -1





def main(file_name, number):
    sequence = read_data(file_name=file_name, key='ordered_numbers')

    # iterative binary search
    #binary_search(sequence, number=number)


    value_idx = recursive_binary_search(sequence, number, 0, len(sequence)-1)
    print(value_idx)

if __name__ == '__main__':
    my_file = 'sequential.json'
    my_number = 90
    main(my_file, my_number)
