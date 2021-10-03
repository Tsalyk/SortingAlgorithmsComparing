from random import randint
from time import time
from statistics import mean
from insertion import insertion_sort
from selection import selection_sort
from shell import shell_sort
from merge import merge_sort


def generate_arr(n: int) -> list:
    """Returns an array with random n elements"""
    return [randint(0, 1000000) for _ in range(n)]


def generate_sorted_arr(n: int) -> list:
    """Returns sorted array with random n elements"""
    return sorted([randint(0, 1000000) for _ in range(n)])


def generate_reversed_arr(n: int) -> list:
    """Returns reversed array with random n elements"""
    return sorted([randint(0, 1000000) for _ in range(n)], reverse=True)


def generate_arr_1_2_3(n: int) -> list:
    """Returns an array with size n which contains only 1, 2, 3"""
    return [randint(1, 3) for _ in range(n)]


def test_sort(k: int, size: int, algorithm: str, n: int) -> tuple:
    """Returns time and number of comparing repeats of
       sorting elements
       :k: choose which type of array should be generated
       :size: size of the array
       :algorithm: algorithm which will be used
       :n: number of experiments
    """
    array_types = [generate_arr, generate_sorted_arr, generate_reversed_arr, generate_arr_1_2_3]
    algorithms = {"merge": merge_sort,
                  "insertion": insertion_sort,
                  "selection": selection_sort,
                  "shell": shell_sort}
    comparing_nums = []
    time_arr = []

    for _ in range(n):
        array = array_types[k](size)
        start = time()
        comparing_nums.append(algorithms[algorithm](array))
        now = time() - start
        time_arr.append(now)

    return mean(time_arr), int(mean(comparing_nums))


def launch() -> str:
    """Returns data about testing sorting algorithms"""
    algorithms = ["merge", "insertion", "selection", "shell"]
    data = {key: dict() for key in algorithms}

    for algorithm in algorithms:
        for i in range(7, 16):
            time_res, comparing = test_sort(0, 2**i, algorithm, 5)
            data[algorithm][f"time_standart_array_2^{i}"] = time_res
            data[algorithm][f"comparing_number_standart_array_2^{i}"] = comparing

            time_res, comparing = test_sort(1, 2**i, algorithm, 5)
            data[algorithm][f"time_sorted_array_2^{i}"] = time_res
            data[algorithm][f"comparing_number_sorted_array_2^{i}"] = comparing

            time_res, comparing = test_sort(2, 2**i, algorithm, 5)
            data[algorithm][f"time_reversed_array_2^{i}"] = time_res
            data[algorithm][f"comparing_number_reversed_array_2^{i}"] = comparing

            time_res, comparing = test_sort(3, 2**i, algorithm, 3)
            data[algorithm][f"time_repeated_array_2^{i}"] = time_res
            data[algorithm][f"comparing_number_repeated_array_2^{i}"] = comparing

    return data


def write_data(file_name: str, data: dict):
    """Writes data in the file"""
    information = ""
    counter = 1

    with open(file_name, "w", encoding="utf-8") as file:
        for key in data:
            information += str(key).upper() + "\n"
            for subkey in data[key]:
                if counter % 8 == 0:
                    information += str(subkey) + ": " + str(data[key][subkey]) + "\n\n"
                else:
                    information += str(subkey) + ": " + str(data[key][subkey]) + "\n"
                counter += 1

        file.write(information)


def start():
    data = launch()
    write_data("data.txt", data)


if __name__ == "__main__":
    start()
