'''
A stack permutation is a permutation of objects in the given input queue which is done by transferring elements from input queue to the output queue with the help of a stack and the built-in push and pop functions.
The well defined rules are: 
 

Only dequeue from the input queue.
Use inbuilt push, pop functions in the single stack.
Stack and input queue must be empty at the end.
Only enqueue to the output queue.
There are a huge number of permutations possible using a stack for a single input queue. 
Given two arrays, both of unique elements. One represents the input queue and the other represents the output queue. Our task is to check if the given output is possible through stack permutation.
Examples: 
Input : First array: 1, 2, 3  
        Second array: 2, 1, 3
Output : Yes
Procedure:
push 1 from input to stack
push 2 from input to stack
pop 2 from stack to output
pop 1 from stack to output
push 3 from input to stack
pop 3 from stack to output


Input : First array: 1, 2, 3  
        Second array: 3, 1, 2
Output : Not Possible 
'''

# Given two arrays, check if one array is
# stack permutation of other.
from collections import deque

# function to check if Input queue
# is permutable to output queue
def checkStackPermutation(ip, op, n):
    que = deque()
    for i in range(n):
        que.append(ip[i])
        
    out = deque()
    for i in range(n):
        out.append(op[i])
    
    stack = deque()
    while(que):
        ele = que.popleft()
        if (ele == out[0]):
            out.popleft()
            while(stack):
                if stack[-1] == out[0]:
                    stack.pop()
                    out.popleft()
                else:
                    break
        else:
            stack.append(ele)
            
    return((not que) and len(stack) == 0 )
    

# Driver Code
if __name__ == '__main__':

	# Input Queue
	Input = [1, 2, 3]

	# Output Queue
	output = [2, 1, 3]

	n = 3

	if (checkStackPermutation(Input,
							output, n)):
		print("Yes")
	else:
		print("Not Possible")

# This code is contributed by PranchalK
