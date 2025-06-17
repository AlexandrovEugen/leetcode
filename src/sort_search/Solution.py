def find_best_value(arr, target):
    arr.sort()
    remaining_target = target
    n = len(arr)

    for i, num in enumerate(arr):
        if remaining_target <= num * (n - i):
            replacement_value = remaining_target / (n - i)
            if replacement_value - int(replacement_value) == 0.5:
                return int(replacement_value)
            return round(replacement_value)
        remaining_target -= num
    return arr[-1]


def contains_nearby_duplicates(nums: list[int], k: int) -> bool:
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            return True

        seen.add(nums[i])

        if len(seen) > k:
            seen.remove(nums[i - k])

    return False


def max_count(banned: list[int], n: int, max_sum: int) -> int:
    banned.sort()
    banned_idx = 0
    count = 0

    for i in range(1, n + 1):
        if banned_idx < len(banned) and banned[banned_idx] == i:
            while banned_idx < len(banned) and banned[banned_idx] == i:
                banned_idx += 1
        else:
            max_sum -= i
            if max_sum < 0:
                return count
            count += 1
    return count
