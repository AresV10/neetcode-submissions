"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        slots = [(interval.start, interval.end) for interval in intervals]
        slots.sort()
        heap = []
        for start, end in slots:
            if heap and heap[0] <= start: #can slot in
                heapq.heapreplace(heap, end)
            else: # no valid slot so increase
                heapq.heappush(heap, end)

        return len(heap)