'''
Iterate through the list, storing weights in a hash with their indici as
values. For each weight test if the remainder is in the hash. If so, that's
your result.
'''


def get_indices_of_item_weights(weights, length, limit):
    remainders = {}
    indici_pair = None

    for i, weight in enumerate(weights):
        if limit - weight in remainders:
            indici_pair = (i, remainders[limit - weight])
            break
        else:
            remainders[weight] = i

    return indici_pair
