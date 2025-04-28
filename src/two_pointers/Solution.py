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
            else:
                return result

        def hasNoCycle(pointer, arr, prevDir):
            curDir = arr[pointer] > 0

            if curDir != prevDir or arr[pointer] % len(nums) == 0:
                return True
            else:
                return False

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


def remove_duplicates(nums):
    i = 0
    j = 0
    k = 1

    while j < len(nums):
        if nums[i] == nums[j]:
            j = j + 1
        else:
            i = i + 1
            nums[i] = nums[j]
            k = k + 1
    return k


def length_of_longest_substring(self, s: str) -> int:
    if len(s) == 1:
        return 1
    d = {}
    l, r = 0, 0
    n = len(s)
    max_len = 0
    while r < n:
        if s[r] in d:
            l = max(l, d[s[r]] + 1)
        length = r - l + 1
        max_len = max(max_len, length)
        d[s[r]] = r
        r += 1
    return max_len


def character_replacement(self, s: str, k: int) -> int:
    freq = {}
    i = 0
    max_length = 0
    max_freq = 0
    for j in range(len(s)):
        freq[s[j]] += 1 + freq.get(s[j], 0)

        max_freq = max(max_freq, freq.get(s[j]))

        if j - i + 1 - max_freq > k:
            freq[s[i]] -= 1
            i += 1

        max_length = max(max_length, j - i + 1)
    return max_length
