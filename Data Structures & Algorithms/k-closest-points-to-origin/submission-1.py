class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
                dist = math.dist([x, y], [0, 0])
                minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        for i in range(k):
                dist, x, y = heapq.heappop(minHeap)
                res.append([x, y])
        return res
        
                                                                                                                                