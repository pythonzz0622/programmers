adj_mat= [
[1 , 2],
[1 , 3],
[2 , 4],
[2 , 5],
[4 , 6],
[5 , 6],
[6 , 7],
[3 , 7]]

V , E = 7 ,8

adj_matrix = [[0] * (V +1) for _ in range(V+1)]

for adj_mat_i in adj_mat:
        i, j = adj_mat_i
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1

for adj_matrix_i in adj_matrix:
        print(adj_matrix_i)


stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
    
    for destination in range(V+1):
          if adj_matrix[current][destination] and destination not in visited:
                stack.append(destination)

print('이동경로:' , *visited)

