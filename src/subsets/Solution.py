def permute_word(word):
    result = []

    def swap_chars(i, j, string):
        sw = list(string)
        sw[i], sw[j] = sw[j], sw[i]
        return ''.join(sw)

    def backtrack(string, c_i):
        if len(string) - 1 == c_i:
            result.append(string)
            return

        for i in range(c_i, len(string)):
            swap_str = swap_chars(c_i, i, string)
            backtrack(swap_str, c_i + 1)

    backtrack(word, 0)
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


def letter_combinations(digits):
    if len(digits) == 0:
        return []

    combinations = []
    output = []
    digits_mapping = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    def backtrack(index):
        if len(digits) == len(output):
            combinations.append(''.join(output))
            return
        possible_letters = digits_mapping[digits[index]]
        if possible_letters:
            for letter in possible_letters:
                output.append(letter)
                backtrack(index + 1)
                output.pop()

    backtrack(0)
    return combinations
