# 단일 출발 최단 경로 문제
# 다익스트라 알고리즘
# BFS와 유사함
# 우선순위 큐를 사용한다.
import heapq

# 1. 그래프가 주어진다.
graph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(graph, start):
    # 2. 그래프 노드들의 거리를 전부 inf로 초기화한다.
    distances = {node: float("inf") for node in graph}
    # 3. 시작점은 0이다.
    distances[start] = 0
    # 큐에 넣는다.
    queue = []

    # heapq 라이브러리를 사용하여 우선순위 큐를 만든다.
    heapq.heappush(queue, [distances[start], start])
    print("queue", queue)

    # while은 queue에 item이 있는 동안만 작동된다.
    while queue:
        # queue에 들어간 아이템을 튜플로 뽑아낸다. c = current
        distance_c, node_c = heapq.heappop(queue)
        # graph안에서 현재 node에 연결된 node와 가중치를 뽑아낸다.

        # 만약에 원래 구한 시작점에서 현재 노드까지의 거리값이 작으면 업데이트 하지 않는다.
        if distances[node_c] < distance_c:
            continue

        for adjacent, weight in graph[node_c].items():
            # 시작 노드에서 현재 노드까지 거리
            distance = distance_c + weight
            # 만약에 계산한 거리가 이전 거리보다 작으면 계산한 거리로 업데이트를 한다.
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                print("queue", queue)

    return distances


print(dijkstra(graph, "A"))
