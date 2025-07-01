import heapq
from queue import PriorityQueue


def network_delay_time(times, n, k):
    adjacency = defaultdict(list)
    for v, u, w in times:
        adjacency[v].append((u, w))

    pq = PriorityQueue()
    pq.put((0, k))

    visited = set()
    delays = 0

    while not pq.empty():
        time, node = pq.get()

        if node in visited:
            continue

        visited.add(node)

        delays = max(delays, time)
        neighbors = adjacency[node]

        for neighbor in neighbors:
            n_u, n_w = neighbor
            if n_u not in visited:
                new_time = time + n_w
                pq.put((new_time, n_u))

    if len(visited) == n:
        return delays

    return -1


def valid_tree(n, edges):
    adjacency = defaultdict(list)

    for v, u in edges:
        adjacency[v].append(u)
        adjacency[u].append(v)

    stack = []

    visited = set()
    stack.append(0)

    while stack:
        node = stack.pop()

        if node in visited:
            return False

        visited.add(node)

        for nei in adjacency[node]:
            if nei not in visited:
                stack.append(nei)

    if len(visited) == n:
        return True
    return False


def number_of_paths_0(n, corridors):
    adjacency = defaultdict(list)
    for r1, r2 in corridors:
        adjacency[r1].append(r2)
        adjacency[r2].append(r1)

    cycles = 0
    tuples = set()
    for u in range(1, n + 1):
        for v in adjacency[u]:
            if v > u:
                for w in adjacency[v]:
                    if w > v and u in adjacency[w] and (u, v, w) not in tuples:
                        cycles += 1
                        tuples.add((u, v, w))
    return cycles


def number_of_paths_1(n, corridors):
    adjacency = defaultdict(set)
    for r1, r2 in corridors:
        adjacency[r1].add(r2)
        adjacency[r2].add(r1)

    cycles = 0
    tuples = set()
    for u in range(1, n + 1):
        for v in adjacency[u]:
            if v > u:
                for w in adjacency[v]:
                    if w > v and u in adjacency[w] and (u, v, w) not in tuples:
                        cycles += 1
                        tuples.add((u, v, w))
    return cycles


def number_of_paths(n, corridors):
    cycles = 0
    graph = defaultdict(set)
    for r1, r2 in corridors:
        graph[r1].add(r2)
        graph[r2].add(r1)
        cycles += len(graph[r1].intersection(graph[r2]))

    return cycles


from collections import defaultdict


def find_judge(n, trust):
    # Replace this placeholder return statement with your code
    adj = defaultdict(list)
    trusts = [0] * (n + 1)
    for a, b in trust:
        adj[a].append(b)
        trusts[b] += 1

    for i, j in enumerate(trusts):
        if j == n -1 and len(adj[i]) == 0:
            return i

    return -1


def max_probability(n, edges, succProb, start, end):
    graph = defaultdict(list)

    for i, (u, v) in enumerate(edges):
        graph[u].append((v, succProb[i]))
        graph[v].append((u, succProb[i]))

    heap = [(-1.0, start)]
    probs = [0.0] * n
    probs[start] = 1.0

    while heap:
        prob, node = heapq.heappop(heap)

        prob = -prob

        if node == end:
            return prob

        for nei, edgProb in graph[node]:
            new_prob = prob * edgProb
            if new_prob > probs[nei]:
                probs[nei] = new_prob
                heapq.heappush(heap, (-new_prob, nei))
    return 0.0
