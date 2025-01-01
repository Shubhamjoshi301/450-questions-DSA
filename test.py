
def smash(bigHits, newtons):
    s = []
    for i in range(len(newtons)):
        s.append([newtons[i],i])
      
    s.sort(key = lambda x : x[0],reverse = True)
    # print(s)
    ans = min(bigHits,len(newtons))
    ind = ans
    big = []
    for i in range(ans):
        big.append(s[i][1]+1)
        
    small = []
    for i in range(ind,len(newtons)):
        small.append(s[i][1]+1)
        ans += s[i][0]
    big.sort()
    small.sort()
    if not big:
        return([[ans],[-1],small])
    if not small:
        return([[ans],big,[-1]])
    return([[ans],big,small])
        
big = int(input())
bricks = list(map(int, input().split()))
print(smash(big,bricks))