def find_best_value(arr, target):
    arr.sort()
    remaining_target = target
    n = len(arr)

    for i, num in enumerate(arr):
        if remaining_target <= num * (n - i):
            replacement_value = remaining_target/ (n - i)
            if replacement_value - int(replacement_value) == 0.5:
                return int(replacement_value)
            return round(replacement_value)
        remaining_target -=num
    return arr[-1]
