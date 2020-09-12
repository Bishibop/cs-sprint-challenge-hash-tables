'''
For each array, iterate over each number.
Key each number into a hash. If it isn't there set the value as 1.
If it is there, increment the value.
Iterate over all key value pairs. If the value is equal to the number of
arrays you iterated over, that key (the number) is an answer.
'''


def intersection(arrays):

    ht = {}
    num_arrays = 0
    for i, arr in enumerate(arrays):
        num_arrays += 1
        for num in arr:
            if num in ht:
                ht[num] += 1
            else:
                ht[num] = 1

    result = []
    for num, occurences in ht.items():
        if occurences == num_arrays:
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
