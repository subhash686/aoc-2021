import os


def octopus(steps):
    path = os.getcwd()
    file_path = os.path.join(path, 'octopus.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    grid = []
    flashes = 0
    for line in Lines:
        input = line.strip()
        row = []
        for level in input:
            row.append(int(level))
        grid.append(row)
    flashes = [0]
    loop = 0
    
    while True:
        loop += 1
        all_flash = True
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] != 0:
                    all_flash = False
        
        if all_flash:
            print(loop-1)
            break

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                grid[row][col] +=1


        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] > 9:
                    dfs(grid, row, col, flashes)
        
        if steps and loop == 100:
            print(flashes[0])
            break


def dfs(grid, row, col, flashes):
    if grid[row][col] != 0:
        grid[row][col] += 1
    if grid[row][col] <= 9:
        return
    else:
        grid[row][col] = 0
        flashes[0] += 1
    
    if row > 0: 
        dfs(grid, row-1, col, flashes)
    if row < len(grid)-1:
        dfs(grid, row+1, col, flashes)
    if col > 0:
        dfs(grid, row, col-1, flashes)
    if col < len(grid[row])-1:
        dfs(grid, row, col+1, flashes)
    if row > 0 and col > 0: 
        dfs(grid, row-1, col-1, flashes)
    if row < len(grid)-1 and col > 0:
        dfs(grid, row+1, col-1, flashes)
    if row > 0 and col < len(grid[row])-1:
        dfs(grid, row-1, col+1, flashes)
    if row < len(grid)-1 and col < len(grid[row])-1:
        dfs(grid, row+1, col+1, flashes)
    

if __name__ == "__main__":
    octopus(True)
    octopus(False)
