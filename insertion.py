def insertion_sort(array):
    comparing_counter = 0

    for i in range(1, len(array)):
        comparing_counter += 1
        key = array[i]

        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            comparing_counter += 1
        array[j + 1] = key

    return comparing_counter + 1
