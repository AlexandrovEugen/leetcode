def sort_colors(colors):

    red = 0
    white = 0
    blue = len(colors) - 1

    while white <= blue:
        if colors[white] == 0:
            tmp = colors[red]
            colors[red] = colors[white]
            colors[white] = tmp
            red = red + 1
            white = white + 1
        elif colors[white] == 1:
            white = white + 1
        else:
            tmp = colors[blue]
            colors[blue] = colors[white]
            colors[white] = tmp
            blue = blue - 1

    return colors


def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast


def circular_array_loop(nums):
    for i in range(0, len(nums)):
        slow = i
        fast = i
        forward = nums[i] > 0

        def nextStep(pointer, arr):
            result = (pointer + arr[pointer]) % len(arr)
            if result < 0:
                return len(arr) + result
            else: return result

        def hasNoCycle(pointer, arr, prevDir):
            curDir = arr[pointer] > 0

            if curDir != prevDir or arr[pointer] % len(nums) == 0:
                return True
            else: return False


        while True:
            slow = nextStep(slow, nums)

            if hasNoCycle(slow, nums, forward):
                break

            fast = nextStep(fast, nums)

            if hasNoCycle(fast, nums, forward):
                break

            fast = nextStep(fast, nums)

            if hasNoCycle(fast, nums, forward):
                break

            if slow == fast: return True

    return False


def count_cycle_length(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            slow = slow.next
            while slow != fast:
                length = length + 1
                slow = slow.next
            return length
    return 0