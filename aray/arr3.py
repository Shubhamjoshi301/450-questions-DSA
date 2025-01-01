import math

def kthSmallest(inp,k):
    inp.sort()
    
    return inp[k-1]


if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(kthSmallest(arr, k))
        print("~")