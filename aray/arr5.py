#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sortnegpos(self, arr):
        # code here
        left = 0
        right = len(arr)-1
        i = 0
        while i <= right:
            # print(arr,i,left,right)
            if arr[i] < 0:
                arr[left],arr[i] = arr[i],arr[left]
                left+=1
                i+=1
            elif arr[i] == 0:
                i+=1
            else:
                arr[right],arr[i] = arr[i],arr[right]
                right-=1
            
        return arr

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split(","))
                   )  # Read the array as space-separated integers
        ob.sortnegpos(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()
