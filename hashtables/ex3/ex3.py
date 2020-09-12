def intersection(arrays):
    print('arrays: ', arrays)

    ht = {}
    num_arrays = 0
    for i, arr in enumerate(arrays):
        num_arrays += 1
        for num in arr:
            if num in ht:
                ht[num].append(i)
            else:
                ht[num] = [i]

    result = []
    for key, value in ht.items():
        print(key, value)
        if len(value) == num_arrays:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
