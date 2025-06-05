def count_palindromic_substrings(s):
    count = 0

    dp = [[False for _ in range(len(s))] for i in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True
        count += 1

    for i in range(len(s) - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        count += dp[i][i + 1]

    for length in range(3, len(s) + 1):
        i = 0
        for j in range(length - 1, len(s)):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1

    return count


def coin_change_backtracking(coins: list[int], target: int) -> int:
    max_int = 2 ** 31 - 1
    if target == 0:
        return 0

    memo = {}

    def backtrack(cur_sum: int, index: int, count: int) -> int:
        if (cur_sum, index, count) in memo:
            return memo[(cur_sum, index, count)]

        if index >= len(coins):
            return max_int
        if cur_sum > target:
            return max_int
        if cur_sum == target:
            return count

        use_same = backtrack(cur_sum + coins[index], index, count + 1)
        skip = backtrack(cur_sum, index + 1, count)
        use_and_advance = backtrack(cur_sum + coins[index], index + 1, count + 1)

        result = min(use_same, use_and_advance, skip)
        memo[(cur_sum, index, count)] = result
        return result

    coin_count = backtrack(0, 0, 0)
    if coin_count == max_int:
        return -1
    return coin_count


def coin_change(coins, target):
    def calculate_minimum_coins(remaining, counter)-> int:
        if remaining < 0:
            return -1
        if remaining == 0:
            return 0
        if counter[remaining - 1] != float('inf'):
            return counter[remaining - 1]

        minimum = float('inf')

        for c in coins:
            result = calculate_minimum_coins(remaining - c, counter)
            if 0 <= result < minimum:
                minimum = result + 1
        counter[remaining - 1] = minimum if minimum != float('inf') else -1
        return counter[remaining - 1]

    return calculate_minimum_coins(target, [float('inf')] * target)
