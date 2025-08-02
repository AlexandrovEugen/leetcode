from typing import List

from src.TreeNode import TreeNode


def right_side_view(root):
    if root:
        stack = [(1, root)]
    else:
        return []
    arr = []
    total_depth = 0
    while stack:
        depth, node = stack.pop()

        if depth > total_depth:
            arr.append(node.data)
            total_depth += 1

        if node.left:
            stack.append((depth + 1, node.left))
        if node.right:
            stack.append((depth + 1, node.right))

    return arr


# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def flatten_tree(root):
    if not root:
        return root
    stack = [root]
    n = TreeNode(-1)
    head = n

    while stack:
        node = stack.pop()
        n.right = node
        n.left = None
        n = n.right

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return head.right


def build_tree(p_order: List[int], i_order: List[int]) -> TreeNode:
    p_index = [0]
    mapping = {}

    for i in range(len(p_order)):
        mapping[i_order[i]] = i

    def build_tree_helper(left: int, right: int) -> TreeNode | None:
        if left > right:
            return None

        curr = p_order[p_index[0]]
        p_index[0] += 1
        root = TreeNode(curr)

        if left == right:
            return root

        in_index = mapping[curr]

        root.left = build_tree_helper(left, in_index - 1)
        root.right = build_tree_helper(in_index + 1, right)
        return root

    return build_tree_helper(0, len(p_order) - 1)
