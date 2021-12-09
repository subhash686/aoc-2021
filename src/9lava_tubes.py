import os
from heapq import heappush, nlargest


def risk_factor():
    path = os.getcwd()
    file_path = os.path.join(path, 'lavatubes.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    risk = 0
    grids = []
    for line in Lines:
        grid = []
        input = line.strip()
        for digit in input:
            grid.append(int(digit))
        grids.append(grid)
    heap = []
    for row in range(0, len(grids)):
        for col in range(0, len(grids[row])):
            elem = grids[row][col]
            top = bottom = left = right = elem + 1
            if row > 0: 
                top = grids[row-1][col]
            if row < len(grids)-1:
                bottom = grids[row+1][col]
            if col > 0:
                left = grids[row][col-1]
            if col < len(grids[row])-1:
                right = grids[row][col+1]
            if elem < top and elem < bottom and elem < left and elem < right:
                risk += elem + 1
                size = [0]
                visited = [[0] * len(grids[row]) for x in range(0,len(grids))]
                bfs(grids, row, col, elem, size, visited)
                x = size[0]
                heappush(heap, x)

    print(risk)
    out = 1
    for x in nlargest(3, heap):
        out = out * x
    print(out)

def bfs(grid, row, col, elem, size, visited):
    if visited[row][col]:
        return
    visited[row][col] = 1
    if elem < grid[row][col] or elem == 9:
        return
    size[0] += 1
    if row > 0: 
        bfs(grid, row-1, col, grid[row-1][col], size, visited)
    if row < len(grid)-1:
        bfs(grid, row+1, col, grid[row+1][col], size, visited)
    if col > 0:
        bfs(grid, row, col-1, grid[row][col-1], size, visited)
    if col < len(grid[row])-1:
        bfs(grid, row, col+1, grid[row][col+1], size, visited)
    return
    
if __name__ == "__main__":
    risk_factor()
