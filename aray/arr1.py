import math

def reverse_arr(inp):
    for i in range(math.ceil(len(inp)/2)):
        inp[i], inp[len(inp) - (i+1)] = inp[len(inp) - (i+1)], inp[i]
    return inp


inp = list(map(int,input().split()))
inp = reverse_arr(inp)

print(" ".join(list(map(str,inp))))