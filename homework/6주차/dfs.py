# 그래프를 DFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
# 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.
# 출력: V부터 방문된 점을 순서대로 출력한다.


# 내 답안
N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]


def solution(N, M, V, edges):
    def dfs(start):
        # 나는 그냥 배운대로 그래프를 만들었다.
        graph = {}
        for i in edges:
            if i[0] not in graph:
                graph[i[0]] = [i[1]]
            else:
                graph[i[0]].append(i[1])
            if i[1] not in graph:
                graph[i[1]] = [i[0]]
            else:
                graph[i[1]].append(i[0])

        visited, will_visit = [], []

        will_visit.append(start)

        while will_visit:
            # dfs는 둘다 큐를 이용하니까....
            node = will_visit.pop(0)
            if node not in visited:
                visited.append(node)
                will_visit.extend(graph[node])
        return visited

    return dfs(V)

# 예시답안


def solution2(N, M, V, edges):
    visited = []
    # 1,2,3,4일때, 인접한 노드를 전부 구할 수 있다. 따지고 보면 graph를 만들었던 방법과 똑같다.
    adj_nodes = [[]]*(N+1)

    # graph가 list로 주어질때...어떻게 해결해야하나에 대한 간단한 해답
    for i in range(1, N+1):
        adj_node = list(
            map(lambda x: x[1], filter(lambda x: x[0] == i, edges))) + list(map(lambda x: x[0], filter(lambda x: x[1] == i, edges)))
        adj_node.sort()
        adj_nodes[i] = adj_node

    def dfs(node):
        visited.append(node)
        print(node, end=' ')
        for i in adj_nodes[node]:
            if i not in visited:
                dfs(i)
    dfs(V)


N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

print(solution(N, M, V, edges))
print(solution2(N, M, V, edges))
