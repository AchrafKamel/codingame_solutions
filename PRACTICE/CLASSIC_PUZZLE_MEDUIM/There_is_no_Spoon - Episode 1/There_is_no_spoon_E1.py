grid = []

# read the inputs
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)


def nextRightCell(x, y):
    if (x >= width): return '-1 -1'
    for i in range(x + 1, width):
        if grid[y][i] == '0': return f'{i} {y}'
    return '-1 -1'

def nextBottomCell(x, y):
    if (y >= height): return '-1 -1'
    for i in range(y + 1, height):
        if grid[i][x] == '0': return f'{x} {i}'
    return '-1 -1'
    
for y in range(height):
    for x in range(width):
        if (grid[y][x] == '0'):       
            print(f'{x} {y} {nextRightCell(x, y)} {nextBottomCell(x, y)}')
