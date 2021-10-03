def merge_sort(array, comparing_counter=0):
    if len(array) > 1:
        comparing_counter += 1
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L, comparing_counter)
        merge_sort(R, comparing_counter)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
            comparing_counter += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            comparing_counter += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
            comparing_counter += 1

    return comparing_counter + 1
