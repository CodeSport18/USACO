# https://usaco.org/index.php?page=viewproblem2&cpid=689

def win_condition(grid,grid_length):

    for a in range(grid_length-1,-1,-1):
        for b in range(grid_length-1,-1,-1):
            if grid[a][b] == '1':
                return [b,a]
            
    return True

file = open('cowtip.in','r')

for a in file:
    number_of_lines = int(a.strip())
    break

grid = []

for a in file:
    grid.append( list(a.strip()) )

file.close()

# print(grid)

moves = 0

the_win_condition = win_condition(grid,number_of_lines)

# print(the_win_condition)

while the_win_condition != True:

    moves += 1
    bottom_right = the_win_condition.copy()

    for a in range(bottom_right[1],-1,-1):
        for b in range(bottom_right[0],-1,-1):
            if grid[a][b] == '1':
                grid[a][b] = '0'
            else:
                grid[a][b] = '1'

    the_win_condition = win_condition(grid,number_of_lines)

    # for a in grid:
    #     for b in a:
    #         print(b,end=' ')
    #     print()
    # print()

file = open('cowtip.out','w')
file.write(str(moves))
file.close()