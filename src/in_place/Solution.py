from email.feedparser import headerRE

from src.ListNode import ListNode


def swap_pair(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(-1)
    dummy.next = head

    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next

        second.next = first

        prev = first
        head = head.next
    return dummy.next


def reverse(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    prev = None
    cur = head
    next = cur.next

    while next:
        cur.next = prev

        prev = cur
        cur = next

        next = next.next
        cur.next = prev

    return cur


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    cur = prev.next

    for _ in range(right - left):
        next_node = cur.next
        cur.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    return dummy.next


def reorder_list(head):
    if not head:
        return head
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow

    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    first, second = head, prev

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head