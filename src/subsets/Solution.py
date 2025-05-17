def permute_word(word):
    result = []

    def swap_chars(i, j, string):
        sw = list(string)
        sw[i], sw[j] = sw[j], sw[i]
        return ''.join(sw)

    def backtrack_0(string, c_i):
        if len(string) - 1 == c_i:
            result.append(string)
            return

        for i in range(c_i, len(string)):
            swap_str = swap_chars(c_i, i, string)
            backtrack_0(swap_str, c_i + 1)

    backtrack_0(word, 0)
    return result


def generate_combinations(n):
    result = []
    output = []

    def backtrack(l: int, r: int):
        if l >= n and r >= n:
            result.append(''.join(output))

        if l < n:
            output.append('(')
            backtrack(l + 1, r)
            output.pop()

        if r < l:
            output.append(')')
            backtrack(l, r + 1)
            output.pop()

    backtrack(0, 0)
    return result
