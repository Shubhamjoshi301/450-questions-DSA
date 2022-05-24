def setBits(N):
    c = 0
    while N > 0:
        N = N&N-1
        c +=1
    return c