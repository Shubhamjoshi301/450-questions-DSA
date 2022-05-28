'''
A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
 

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.

Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
2 <= N <= 3000
0 <= M[][] <= 1

'''

# complexity n^2
#User function Template for python3

# class Solution:
    
#     #Function to find if there is a celebrity in the party or not.
#     def celebrity(self, M, n):
#         # code here 
#         indeg = []
#         outdeg = []
#         for i in range(n):
#             temp1 = 0
#             temp2 = 0
#             for j in range(n):
#                 temp1 += M[j][i]
#                 temp2 += M[i][j]
#             indeg.append(temp1)
#             outdeg.append(temp2)
            
#         for i in range(len(indeg)):
#             if indeg[i] == n-1 and outdeg[i] == 0:
#                 return i
#         return -1


# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t) :
#         n = int(input())
#         a = list(map(int,input().strip().split()))
#         k = 0
#         m = []
#         for i in range(n):
#             row = []
#             for j in range(n):
#                 row.append(a[k])
#                 k+=1
#             m.append(row)
#         ob = Solution()
#         print(ob.celebrity(m,n))
# # } Driver Code Ends

'''
Two pointer complexcity : o(n)
'''

#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        i = 0
        j = n-1
        while i < j:
            if M[i][j] == 1:
                i += 1
            else:
                j-=1
        
        for k in range(n):
            if M[i][k] == 1 and i !=k:
                return -1
        for k in range(n):
            if M[k][i] == 0 and i!=k:
                return -1
        
        return i


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends