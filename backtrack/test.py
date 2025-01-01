class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        inv = 0
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
        print("left " , len(arr[l:l+m+1]))
        L = arr[l:l+m+1]
        print("right ", len(arr[l+m+1:r+1]))
        R = arr[l+m+1:r+1]
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
        # print(L,R)
        # Copy data to temp arrays L[] and R[]
        # for i in range(0, n1):
        #     L[i] = arr[l + i]
    
        # for j in range(0, n2):
        #     R[j] = arr[m + 1 + j]
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                inv += n1-i
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
        
        return inv        
              
    def mergeSort(self, arr,l,r):
        leftinv = rightinv = mergeinv = 0
        if l < r:
     
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2
            # print(m)
            # Sort first and second halves
            leftinv = self.mergeSort(arr, l, m)
            rightinv = self.mergeSort(arr, m+1, r)
            mergeinv = self.merge(arr, l, m, r)
        return(leftinv+rightinv+mergeinv)
        
        
    
    
    
    def inversionCount(self, arr, n):
        # Your Code Here
        return self.mergeSort(arr,0,n-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends