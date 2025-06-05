

def jump_game(nums):
    dest = len(nums) - 1

    for i in range(len(nums) - 2, - 1, -1):
        if dest <= i + nums[i]:
            dest = i
    if dest == 0:
        return True

    return False


def jump_game_two(nums:list[int]) -> int:

    jumps = 0
    farthest_jump = 0
    current_jump_boundary = 0
    for i in range(len(nums) - 1):
        farthest_jump = max(farthest_jump, i + nums[i])

        if i == current_jump_boundary:
            jumps +=1
            current_jump_boundary = farthest_jump


    return jumps