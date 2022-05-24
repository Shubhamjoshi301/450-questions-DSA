class Solution: 
    def minJumps(self,arr, n):
        # The number of jumps needed to reach the starting index is 0
        if (n <= 1):
            return 0

        # Return -1 if not possible to jump
        if (arr[0] == 0):
            return -1

        # initialization
        # stores all time the maximal reachable index in the array
        maxReach = arr[0]
        # stores the amount of steps we can still take
        step = arr[0]
        # stores the amount of jumps necessary to reach that maximal reachable position
        jump = 1

        # Start traversing array

        for i in range(1, n):
            # Check if we have reached the end of the array
            if (i == n-1):
                return jump

            # updating maxReach
            maxReach = max(maxReach, i + arr[i])

            # we use a step to get to the current index
            step -= 1

            # If no further steps left
            if (step == 0):
                # we must have used a jump
                jump += 1

                # Check if the current index / position or lesser index
                # is the maximum reach point from the previous indexes
                if(i >= maxReach):
                    return -1

                # re-initialize the steps to the amount
                # of steps to reach maxReach from position i.
                step = maxReach - i
        return -1


# User function Template for python3


        # code here


        # {
        #  Driver Code Starts
        # Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)
# } Driver Code Ends
