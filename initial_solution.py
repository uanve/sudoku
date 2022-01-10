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
def possible_numbers(I,J,grid):
    numb_included  = [grid[i][J] for i in range(9) if grid[i][J]>0]
    numb_included += [grid[I][j] for j in range(9) if grid[I][j]>0]
    for i in range(I//3*3,I//3*3+3):
        for j in range(J//3*3,J//3*3+3):
            if grid[i][j]!=0:
                numb_included.append(grid[i][j])

    return list(set(numb_included))

def square_idx(idx):
    square_idx = []
    I = idx%3
    J = idx//3
    for j in range(J*3,J*3+3):
        for i in range(I*3,I*3+3):
        
            square_idx.append((i,j))
    

    return square_idx

def lines_idx(i,j):
    lines_idx = []
    for idx in range(9):
        square_idx.append((idx,i))
        square_idx.append((j,idx))
    return lines_idx


def possible_numbers_square(square,grid):
    candidates = []
    for numb in range(1,10):
        candidates_ = []
        for idx,(i,j) in enumerate(square_idx(square)):
            if (grid[i][j]==0) and (numb not in possible_numbers(i,j,grid)):
                candidates_.append((i,j))
                # print(candidates)
        if len(candidates_)==1:
            candidates.append([candidates_[0][0],candidates_[0][1],numb])
            # print("put {} in {},{}".format(numb,candidates[0][0],candidates[0][1]))
    return candidates
            



    return candidates

                
                


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

        
    