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


def find_repeated_dna_sequences(s: str) -> list[str]:
    seen = set()
    repeated = set()

    for i in range(len(s) - 9):  # 10-letter sequences
        sequence = s[i:i + 10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)

    return list(repeated)


def least_interval(tasks, n):
    freq = [0] * 26

    for t in tasks:
        freq[ord(t) - ord('A')]+=1

    freq.sort(reverse=True)

    max_gaps = freq[0] - 1
    idle_slots = max_gaps * n

    for i in range(1, len(freq)):
        idle_slots -= min(freq[i], max_gaps)

    idle_slots = max(0, idle_slots)

    return idle_slots + len(tasks)

def merge_intervals(intervals):
    result = []
    result.append([intervals[0][0], intervals[0][1]])

    for i in range(1, len(intervals)):
        prev = result[len(result) - 1]
        cur = intervals[i]

        if prev[1] >= cur[0]:
            result[-1][1] = max(prev[1], cur[1])
        else:
            result.append(cur)

    return  result

def insert_interval(intervals, new_interval):
    ns, ne = new_interval

    i = 0
    result = []
    while i < len(intervals) and intervals[i][1] < ns:
        result.append(intervals[i])
        i = i + 1

    result.append(new_interval)

    while i < len(intervals):
        last_i = len(result) - 1
        os, oe = intervals[i]

        ns, ne = result[last_i]

        if ns <= os and ne >= oe:
            i = i + 1
            continue

        if oe <= ns or ne >= os:
            result[last_i] = [min(os, ns), max(oe, ne)]
        else:
            result.append(intervals[i])
        i = i + 1
    return result



