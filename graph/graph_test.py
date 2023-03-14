from collections import deque
graph = [
    [] ,
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9 


def dfs(graph , v , visited):
    print(v , end = ' ')
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph , i , visited)


# dfs(graph , 1 , visited)


def bfs(graph , v , visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v , end =' ')        
        for i in graph[v]:

            if visited[i] == False:
                visited[i] = True
                queue.append(i)

bfs(graph , 1 , visited)