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
