def selection_sort(array):
    comparing_counter = 0

    for i in range(len(array)):
        comparing_counter += 1
        min_idx = i
        for j in range(i+1, len(array)):
            comparing_counter += 1
            if array[min_idx] > array[j]:
                min_idx = j
                comparing_counter += 1

        array[i], array[min_idx] = array[min_idx], array[i]

    return comparing_counter + 1
