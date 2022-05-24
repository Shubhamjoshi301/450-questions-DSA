import math
inp = list(map(int,input().split()))

for i in range(math.ceil(len(inp)/2)):
    inp[i], inp[len(inp) - (i+1)] = inp[len(inp) - (i+1)], inp[i]
print(inp)