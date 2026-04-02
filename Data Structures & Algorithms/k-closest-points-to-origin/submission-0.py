class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
                distance = math.dist([x, y], [0, 0])
                minHeap.append((distance, [x,y]))

        heapq.heapify(minHeap)
        res = []
        for i in range(k):
                point = heapq.heappop(minHeap)[1]
                res.append(point)
        return res
        
                                                                                                                                