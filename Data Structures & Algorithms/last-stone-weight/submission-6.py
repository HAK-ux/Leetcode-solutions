class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            heapq.heappush(stones, (y - x) * -1)
        

        return heapq.heappop(stones) * -1 if stones else 0
