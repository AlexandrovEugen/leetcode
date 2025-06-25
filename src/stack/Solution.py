from stack.logs import *


def min_remove_parentheses(s):
    res = [''] * len(s)
    stack = []

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
            res[i] = c
        elif c == ')':
            if stack:
                stack.pop()
                res[i] = c
        else:
            res[i] = c

    while stack:
        i = stack.pop()
        res.pop(i)

    return ''.join(res)


def exclusive_time(n, logs):
    res = [0] * n
    stack = []
    for l in logs:
        log = Log(l)
        if log.is_start:
            stack.append(log)
        else:
            top = stack.pop()
            res[top.id] += (log.time - top.time + 1)
            if stack:
                res[stack[-1].id] -= (log.time - top.time + 1)

    return res
