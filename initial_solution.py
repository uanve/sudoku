def csv_to_list():
    f = open("initial_solution.txt", "r")
    l = []

    for e in f:
        # e = e[:-1]
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