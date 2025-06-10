def find_corrupt_pair(nums: list[int]) -> list[int]:
    missing = None
    duplicated = None

    i = 0

    while i < len(nums):
        c_i = nums[i] - 1

        if nums[i] != nums[c_i]:
            nums[i], nums[c_i] = nums[c_i], nums[i]
        else:
            i +=1

    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicated = nums[j]
            missing = j + 1

    return [missing, duplicated]
