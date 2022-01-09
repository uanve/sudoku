def csv_to_list():
    f = open("initial_solution.txt", "r")
    l = []

    for e in f:
        # e = e[:-1]
        e = e.split('\t')
        l+=e

    f.close()
    idx = 0
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append(int(l[idx]))
            idx+=1

    return grid

from random import randint
def next_numb(numb_included):
    numb = randint(1,9)
    while numb in numb_included:
        numb = randint(1,9)

    return numb


def new_number(I,J,grid):
    
    numb_included  = [grid[i][J] for i in range(9) if grid[i][J]>0]
    numb_included+= [grid[I][j] for j in range(9) if grid[I][j]>0]
    for i in range(I//3*3,I//3*3+3):
        for j in range(J//3*3,J//3*3+3):
            if grid[i][j]!=0:
                numb_included.append(grid[i][j])

    # print(numb_included)

    if len(set(numb_included))>=9:
        return -1
    return next_numb(set(numb_included))


def is_correct(grid):
    for j in range(9):
        l = [grid[i][j] for i in range(9) if grid[i][j]!=0]
        if len(l) != len(set(l)):
            return False
        
    for i in range(9):
        l = [grid[i][j] for j in range(9) if grid[i][j]!=0]
        if len(l) != len(set(l)):
            return False
    return True

        
    