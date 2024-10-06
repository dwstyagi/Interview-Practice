class MinHeap:
    
    def __init__(self ,capacity) :
        self.capacity = capacity
        self.heap = [0 for i in range(capacity)]
        self.size = 0
        
    def minHeapify(self ,i) :
        
        smallest = i    # Root
        l = 2 * i + 1   # Left Child
        r = 2 * i + 2   # Right Child
        
        if l < self.size and self.heap[l] < self.heap[smallest] :
            smallest = l
        
        if r < self.size and self.heap[r] < self.heap[smallest] :
            smallest = r
        
        if smallest != i :
            self.heap[smallest] ,self.heap[i] = self.heap[i] ,self.heap[smallest]
            self.minHeapify(smallest)  
    
    def insertKey(self ,data) :
        
        self.heap[self.size] = data
        child = self.size
        parent = (child-1)//2
        self.size += 1
        
        while child > 0 and self.heap[child] < self.heap[parent]:
            self.heap[child] ,self.heap[parent] = self.heap[parent] ,self.heap[child]
            child = parent # child go to 1 level up
            parent = (parent-1)//2 # parent go to 1 level up
    
    def deleteKey(self, i) :

        if self.size <= i:
            return -1

        self.heap[i] = self.heap[self.size-1]
        self.heap[self.size-1] = 0
        self.size -= 1
        self.minHeapify(i)
    
    def peek(self):
        
        if self.size < 0:
            return -1
        
        return self.heap[0]
        
    def extractMin(self):
        
        if self.size < 0:
            return -1

        min_ = self.heap[0]
        self.deleteKey(0)        
        return min_  
    
    def printData(self):
        if self.size == -1:
            return -1

        for i in range(self.size):
            print(self.heap[i],end=" ")

def findMedian(arr, k):
    heap = MinHeap(k)
    n = len(arr)

    heap = MinHeap(k)


    for i in range(n):
        if i < k - 1 :
            print(-1,end=" ")
            heap.insertKey(arr[i])
            
        
        elif i == k - 1:
            heap.insertKey(arr[i])
            print(heap.peek(),end=" ")
        
        else:
            if arr[i] > heap.peek():
                heap.deleteKey(0)
                heap.insertKey(arr[i])
                print(heap.peek(),end=" ")
                
            elif arr[i] <= heap.peek():
                print(heap.peek(),end=" ")

stream = [10, 20, 11, 70, 50, 40, 100, 5]
k = 3

findMedian(stream, k)
