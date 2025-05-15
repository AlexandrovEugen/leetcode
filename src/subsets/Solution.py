def swap_chairs(word, i, j):
    swap_list = list(word)
    swap_list[i], swap_list[j] = swap_list[j], swap_list[i]
    return ''.join(swap_list)


def backtrack(word, cur, result):
    if len(word) - 1 == cur:
        result.append(word)

    for i in range(cur, len(word) - 1):
        swapped = swap_chairs(word, cur, i)
        result.append(swapped)
        backtrack(word, cur + 1, result)

def permute_word(word):
    result = []
    backtrack(word, 0, result)
    return result