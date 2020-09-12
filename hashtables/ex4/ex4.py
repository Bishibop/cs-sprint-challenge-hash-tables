'''
Test to see if the negative of each number is stored in the hash.
If so, that's a answer. If not, store the number as a key in the hasn.
'''


def has_negatives(a):

    ht = {}
    result = []
    for num in a:
        if num * -1 in ht:
            if num < 0:
                result.append(num * -1)
            else:
                result.append(num)
        else:
            ht[num] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
