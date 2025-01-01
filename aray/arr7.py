#User function Template for python3

class Solution:
    def rotate(self, arr):
        i = 0
        j = len(arr)-1
        
        while i<j:
            arr[i], arr[j] = arr[j],arr[i]
            i+=1
            
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1

# } Driver Code Ends