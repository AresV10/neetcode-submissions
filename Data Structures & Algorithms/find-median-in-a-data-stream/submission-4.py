class MedianFinder:

    def __init__(self):
        self.minheap = [] #larger half
        self.maxheap = [] #smaller half
        self.minheap_count = 0
        self.maxheap_count = 0
    def addNum(self, num: int) -> None:
        if self.maxheap == [] or self.minheap == []:
            heapq.heappush(self.maxheap, -num)
            self.maxheap_count+=1
        elif num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
            self.maxheap_count+=1
        else:
            heapq.heappush(self.minheap, num)
            self.minheap_count+=1
        #balance heaps
        if self.minheap_count - self.maxheap_count > 1:
            temp = heapq.heappop(self.minheap)
            self.minheap_count-=1
            heapq.heappush(self.maxheap, -temp)
            self.maxheap_count+=1
        elif self.maxheap_count - self.minheap_count > 1:
            temp = heapq.heappop(self.maxheap)
            self.maxheap_count-=1
            heapq.heappush(self.minheap, -temp)
            self.minheap_count+=1

    def findMedian(self) -> float:
        #print(self.maxheap, self.minheap)
        if (self.minheap_count + self.maxheap_count) % 2 == 0:
            return (self.minheap[0] - self.maxheap[0])/2
        else:
            if self.minheap_count > self.maxheap_count:
                return self.minheap[0]
            else:
                return -self.maxheap[0]

