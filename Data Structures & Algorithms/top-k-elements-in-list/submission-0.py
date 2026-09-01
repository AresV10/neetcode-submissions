class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1

        heap = []
        for number, frequency in frequency_dict.items():
            heapq.heappush(heap, (frequency, number))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [pair[1] for pair in heap]