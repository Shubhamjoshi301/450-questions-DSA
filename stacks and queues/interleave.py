# Python3 program to interleave the first
# half of the queue with the second half
from queue import Queue
import queue

# Function to interleave the queue
def interLeaveQueue(q:queue):
    n = int(q.qsize()/2)
    ans = []
    for i in range(n):
        ans.append(q.queue[i])
        ans.append(q.queue[n+i])
    for i in range(q.qsize()):
        q.queue[i] = ans[i]
	

# Driver Code
if __name__ == '__main__':
	q = Queue()
	q.put(11)
	q.put(12)
	q.put(13)
	q.put(14)
	q.put(15)
	q.put(16)
	q.put(17)
	q.put(18)
	q.put(19)
	q.put(20)
	interLeaveQueue(q)
	length = q.qsize()
	for i in range(length):
		print(q.queue[0], end = " ")
		q.get()

# This code is contributed by PranchalK
