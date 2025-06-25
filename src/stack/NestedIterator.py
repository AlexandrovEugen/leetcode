from collections import deque


class NestedIterator:

    def __init__(self, nested_list):
        self.arr = []
        self.count = 0
        self._flatten(nested_list)

    def _flatten(self, nested_list):
        stack = []
        queue = deque()
        for item in nested_list:
            self._handle_inner_list(queue, stack)
            if type(item) is list:
                stack.append(item)
            else:
                self.arr.append(item)
        self._handle_inner_list(queue, stack)

    def _handle_inner_list(self, queue, stack):
        while queue or stack:
            while stack:
                ite = stack.pop()
                i = 0
                while i < len(ite):
                    if type(ite[i]) is list:
                        stack.append(ite[i])
                        i += 1
                        if queue:
                            while i < len(ite):
                                queue.appendleft(ite[i])
                                i += 1
                        else:
                            while i < len(ite):
                                queue.append(ite[i])
                                i += 1
                    else:
                        self.arr.append(ite[i])
                    i += 1
            while queue:
                ite = queue.popleft()
                if type(ite) is list:
                    stack.append(ite)
                    break
                else:
                    self.arr.append(ite)

    def has_next(self):
        return self.count < len(self.arr)

    def next(self):
        item = self.arr[self.count]
        self.count += 1
        return item
