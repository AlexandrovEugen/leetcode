import heapq


def k_smallest_pairs(list1, list2, k):
    count = 0
    heap = []

    for i in range(min(k, len(list1))):
        heapq.heappush(heap, (list1[i] + list2[0], i, 0))

    pairs = []

    while heap and count <= k:
        _, i, j = heapq.heappop(heap)

        pairs.append([list1[i], list2[j]])

        next_j = j + 1

        if len(list2) > next_j:
            heapq.heappush(heap, (list1[i] + list2[next_j], i, next_j))

        count += 1

    return pairs


def kth_smallest_element(matrix: list[list[int]], k: int) -> int:
    res = None
    heap = []  #(val, list_i, el_i)

    for i, row in enumerate(matrix):
        heapq.heappush(heap, (row[0], i, 0))

    count = 0
    while heap and count < k:
        res, list_i, el_i = heapq.heappop(heap)
        count +=1
        if count == k:
            break

        next_i = el_i + 1
        if len(matrix[list_i]) > next_i:
            heapq.heappush(heap, (matrix[list_i][next_i], list_i, next_i))

    return res
