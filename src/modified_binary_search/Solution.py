

def single_non_duplicate(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l != r:
        m = l + (r - l) // 2

        if m % 2 == 1:
            m -= 1

        if nums[m] == nums[m + 1]:
            l = m + 2
        else:
            r = m

    return nums[l]


def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:

        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            left = mid + 1


        else:
            right = mid - 1
    return left


def find_closest_elements(nums, k, target):
    if len(nums) == k:
        return nums

    if target <= nums[0]:
        return nums[0:k]

    if target >= nums[-1]:
        return nums[len(nums) - k: len(nums)]

    first_closest = binary_search(nums, target)

    window_left = first_closest - 1
    window_right = window_left + 1

    while (window_right - window_left - 1) < k:
        if window_left == -1:
            window_right += 1
            continue

        if window_right == len(nums) or abs(nums[window_left] - target) <= abs(nums[window_right] - target):
            window_left -= 1

        else:
            window_right += 1

    return nums[window_left + 1: window_right]




