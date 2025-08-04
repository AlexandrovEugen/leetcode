from collections import deque
from TreeNode import TreeNode


# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def zigzag_level_order(root):
    if root is None:
        return []

    results = []
    dq = deque([root])
    reverse = False

    while len(dq):
        size = len(dq)
        results.insert(len(results), [])

        for i in range(size):
            if not reverse:
                node = dq.popleft()
                results[len(results) - 1].append(node.data)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                node = dq.pop()
                results[len(results) - 1].append(node.data)

                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left)

        reverse = not reverse

    return results


def populate_next_pointers(root):

    q = deque()
    q.append(root)

    while q:
        size = len(q)

        prev = None
        for i in range(size):
            node = q.popleft()
            if prev:
                prev.next = node
            prev = node

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return root