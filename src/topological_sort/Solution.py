from collections import defaultdict, deque


def topological_sort(graph):
    in_degree = [0] * len(graph)

    for node in graph:
        for nei in graph[node]:
            in_degree[nei] += 1

    queue = []

    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    topological_order = []

    while queue:
        current = queue.pop()
        topological_order.append(current)

        for nei in graph[current]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    if len(topological_order) != len(graph):
        raise Exception

    return topological_order


def find_recipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for i, r in enumerate(recipes):
        for ing in ingredients[i]:
            graph[ing].append(r)
            in_degree[r] += 1

    queue = deque(supplies)

    res = []

    while queue:
        current = queue.pop()

        if current in recipes:
            res.append(current)

        for nei in graph[current]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return res


def find_order(n, prerequisites):
    graph = defaultdict(list)
    in_greed = [0] * n

    for a, b in prerequisites:
        graph[b].append(a)
        in_greed[a] += 1

    q = deque()
    for i in range(n):
        if in_greed[i] == 0:
            q.append(i)

    topological_order = []

    while q:
        current = q.pop()
        topological_order.append(current)

        for nei in graph[current]:
            in_greed[nei] -= 1
            if in_greed[nei] == 0:
                q.append(nei)

    return topological_order


def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)

    in_greed = [0] * num_courses

    for a, b in prerequisites:
        graph[b].append(a)
        in_greed[a] += 1

    queue = deque()

    for c in range(num_courses):
        if in_greed[c] == 0:
            queue.append(c)

    topological_order = []

    while queue:
        cur = queue.pop()
        topological_order.append(cur)

        for nei in graph[cur]:
            in_greed[nei]-=1
            if in_greed[nei] == 0:
                queue.append(nei)


    return len(topological_order) == num_courses
