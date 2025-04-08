'''
11725번
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''
from collections import deque

N = int(input())

graph = []
for _ in range(N+1): # 0번 아예 안쓰고 1번부터 할거니깐
    graph.append([])
for _ in range(N-1): # 엣지의 갯수는 N-1개니깐 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N +1)
visited = [False] * (N+1)


def bfs(start): # 루트부터 시작
    queue = deque()
    queue.append(start)

    visited[start] = True

    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                parent[next_node] = current
                queue.append(next_node)

bfs(1)

for i in range(2, N+1):
    print(parent[i])