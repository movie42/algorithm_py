import heapq


def solution(n, vertex):
    queue = []
    distances = [float("inf")] * (n + 1)
    distances[1] = 0

    heapq.heappush(queue, (distances[1], 1))

    while queue:
        distance_c, node_c = heapq.heappop(queue)
        # 여기서부터...
        adj_list = list(map(lambda x: x[1], filter(lambda x: x[0] == node_c, vertex)))

        print("node_c", node_c, "adj_list", adj_list)


# 노드의 개수
n = 6
# vertex [a, b] a 노드와 b 노드 사이에 간선이 있다는 의미
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
