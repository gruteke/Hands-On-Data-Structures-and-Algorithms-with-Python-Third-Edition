class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item
        
    def heap_sort(self):  
        sorted_list = []  
        for node in range(self.size):  
            n = self.pop()  
            sorted_list.append(n)  
        return sorted_list 
      
      
      
h = Heap()
for i in ( 4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)

print(h.heap)


h = Heap()  
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]  


for i in unsorted_list:  
    h.insert(i)  

print("Unsorted list: {}".format(unsorted_list))  


h.heap_sort()