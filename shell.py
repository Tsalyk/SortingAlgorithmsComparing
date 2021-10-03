def shell_sort(array):
    n = len(array)
    gap = n//2
    comparing_counter = 0

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            comparing_counter += 1

            while  j >= gap and array[j-gap] >temp:
                array[j] = array[j-gap]
                j -= gap
                comparing_counter += 1

            array[j] = temp
        gap //= 2
        comparing_counter += 1

    return comparing_counter + 1
