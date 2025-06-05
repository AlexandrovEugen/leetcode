from xml.etree.ElementInclude import include


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def word_search(grid: list[list[str]], word: str) -> bool:
    def dfs(row, col, index) -> bool:
        # if solution is complete
        if len(word) == index:
            return True

        # or if the solution is dead end
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) \
                or grid[row][col] != word[index]:
            return False

        temp = grid[row][col]

        grid[row][col] = "*"

        # for every possible option run the backtrack function once again
        for rowOffset, collOffset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if dfs(row + rowOffset, col + collOffset, index + 1):
                return True

        # backtrack
        grid[row][col] = temp
        return False

    # start at every possible position
    n = len(grid)
    m = len(grid[0])
    for row in range(n):
        for col in range(m):
            if dfs(row=row, col=col, index=0):
                return True
    return False


def rob(root: TreeNode):
    def heist(node: TreeNode) -> list[int]:
        if node is None:
            return [0, 0]

        left_subtree = heist(node.left)
        right_subtree = heist(node.right)

        include_root = node.data + left_subtree[1] + right_subtree[1]
        exclude_root = max(left_subtree) + max(right_subtree)

        return [include_root, exclude_root]

    return max(heist(root))


def valid(segment):
    segment_length = len(segment)  # storing the length of each segment
    if segment_length > 3:  # each segment's length should be less than 3
        return False

    # Check if the current segment is valid
    # for either one of following conditions:
    # 1. Check if the current segment is less or equal to 255.
    # 2. Check if the length of the segment is 1. The first character of segment
    #    can be `0` only if the length of the segment is 1.
    return 0 <= int(segment) <= 255


# this function will append the current list of segments to the list of results.
def update_segment(s, curr_dot, segments, result):
    segment = s[curr_dot + 1:len(s)]

    if valid(segment):  # if the segment is acceptable
        segments.append(segment)  # add it to the list of segments
        result.append('.'.join(segments))
        segments.pop()  # remove the top segment


def backtrack(s, prev_dot, dots, segments, result):
    # prev_dot : the position of the previously placed dot
    # dots : number of dots to place

    size = len(s)

    # The current dot curr_dot could be placed in
    # a range from prev_dot + 1 to prev_dot + 4.
    # The dot couldn't be placed after the last character in the string.
    for curr_dot in range(prev_dot + 1, min(size - 1, prev_dot + 4)):
        segment = s[prev_dot + 1:curr_dot + 1]
        if valid(segment):
            segments.append(segment)

            # if all 3 dots are placed add the solution to result
            if dots - 1 == 0:
                update_segment(s, curr_dot, segments, result)
            else:
                # continue to place dots
                backtrack(s, curr_dot, dots - 1, segments, result)

            segments.pop()  # remove the last placed dot


def restore_ip_addresses(s):

    # creating empty lists for storing valid IP addresses,
    # and each segment of IP
    result, segments = [], []
    backtrack(s, -1, 3, segments, result)
    return result