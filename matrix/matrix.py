def findCommon(mat,n,m):
    common = set(mat[0])
    for row in mat:
        temp = set(row)
        l = list(common)
        for i in range(len(common)):
            if l[i] not in temp:
                common.remove(l[i])
    
    return list(common)
mat = [[1,2,3,4],[2,3,4,5],[2,3,6,7],[2,3,6,8]]
print(findCommon(mat,4,4))