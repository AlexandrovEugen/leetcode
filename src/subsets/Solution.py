from collections import deque


def swap_chars(i, j, word):
    sw = list(word)
    sw[i], sw[j] = sw[j], sw[i]
    return ''.join(sw)


def backtrack_0(word, c_i, result):
    if len(word) - 1 == c_i:
        result.append(word)
        return

    for i in range(c_i, len(word)):
        swap_str = swap_chars(c_i, i, word)
        backtrack_0(swap_str, c_i + 1, result)

def permute_word(word):
    result = []
    backtrack_0(word, 0, result)
    return result


def backtrack(n:int, l:int, r:int, output, result:list[str]):
    if l >= n and r >=n:
        result.append(''.join(output))

    if l < n:
        output.append('(')
        backtrack(n, l + 1, r, output, result)
        output.pop()

    if r < l:
        output.append(')')
        backtrack(n, l, r + 1, output, result)
        output.pop()


def generate_combinations(n):
    result = []
    output = []
    backtrack(n, 0, 0, output, result)
    return result


