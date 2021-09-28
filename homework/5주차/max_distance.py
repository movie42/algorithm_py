# 최단 경로 찾기

import heapq


def solution(n, vertex):
    queue = []
    distances = [float("inf")] * (n + 1)
    distances[1] = 0

    heapq.heappush(queue, (distances[1], 1))

    while queue:
        # 현재 거리, 현재 노드
        distance_c, node_c = heapq.heappop(queue)
        print("distance_c", distance_c, 'node_c', node_c)

        # 인접 노드 찾기
        # map은 map(적용시킬 조건, 타겟) filter(적용시킬 조건, 타겟)
        # map(적용시킬 조건, 타겟(filter(적용시킬 조건, 타겟)))
        adj_list = list(map(lambda x: x[1], filter(
            lambda x: x[0] == node_c, vertex)))
        adj_list += list(map(lambda x: x[0],
                             filter(lambda x: x[1] == node_c, vertex)))

        for adj_node in adj_list:
            # print("adj_node", adj_node)
            if distances[adj_node] > distance_c + 1:
                distances[adj_node] = distance_c + 1
                heapq.heappush(queue, (distances[adj_node], adj_node))
                # print("queue", queue)
    return distances.count(max(distances[1:]))


# 노드의 개수
n = 6
# vertex [a, b] a 노드와 b 노드 사이에 간선이 있다는 의미
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
