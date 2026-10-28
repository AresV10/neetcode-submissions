class MedianFinder:

    def __init__(self):
        self.minheap = [] #larger half
        self.maxheap = [] #smaller half
    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        #balance heaps
        if len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        #print(self.maxheap, self.minheap)
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            return (self.minheap[0] - self.maxheap[0])/2
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            return -self.maxheap[0]

