import heapq


def solution(n, vertex):
    to_visit = []
    dists = [float('inf')] * (n + 1)

    dists[1] = 0
    heapq.heappush(to_visit, (0, 1))
    while len(to_visit) > 0:
        dist, node = heapq.heappop(to_visit)
        adj_list = list(map(lambda x: x[1], filter(
            lambda x: x[0] == node, vertex)))
        adj_list += list(map(lambda x: x[0],
                         filter(lambda x: x[1] == node, vertex)))
        for adj_node in adj_list:
            if dists[adj_node] > dist + 1:
                dists[adj_node] = dist + 1
                heapq.heappush(to_visit, (dists[adj_node], adj_node))

    return dists.count(max(dists[1:]))


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
