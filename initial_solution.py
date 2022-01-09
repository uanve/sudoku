def csv_to_list():
    f = open("initial_solution.txt", "r")
    l = []

    for e in f:
        # e = e[:-1]
        # print(e)
        e = e.split('\t')
        l+=e
    f.close()
    idx = 0
    grid = {}
    for i in range(9):
        for j in range(9):
            grid[(i,j)] = int(l[idx])
            idx+=1

    return grid

from random import randint
def next_numb(numb_included):
    numb = randint(1,9)
    while numb in numb_included:
        numb = randint(1,9)

    return numb

def line(n,grid):
    j = n
    is_new = [grid[(i,j)] == 0 for i in range(9)]
    numb_included  = [grid[(i,j)] for i in range(9) if grid[(i,j)]>0]

    for i in range(9):
        if is_new[i]:
            grid[(i,j)] = next_numb(numb_included)
            numb_included.append(grid[(i,j)])
    return ([grid[(i,j)] for i in range(9)], is_new)




def is_correct(grid):
    n_current_solution = 0
    for j in range(9):
        l = [grid[(i,j)] for i in range(9) if grid[(i,j)]!=0]
        if len(l) != len(set(l)):
            return False,0
        n_current_solution+=len(set(l))
        
    for i in range(9):
        l = [grid[(i,j)] for j in range(9) if grid[(i,j)]!=0]
        if len(l) != len(set(l)):
            return False,0
        n_current_solution+=len(set(l))
    return (True,n_current_solution)

        
    