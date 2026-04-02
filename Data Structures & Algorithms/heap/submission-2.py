class MinHeap:
    
    def __init__(self):
        self.minHeap = [0]

    def push(self, val: int) -> None:
        self.minHeap.append(val)
        i = len(self.minHeap) - 1

        # Percolate up
        while self.minHeap[i // 2] > self.minHeap[i] and i > 1:
            self.minHeap[i], self.minHeap[i // 2] = self.minHeap[i // 2], self.minHeap[i]
            i = i // 2

    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        if len(self.minHeap) == 2:
            return self.minHeap.pop()
            
        res = self.minHeap[1]
        self.minHeap[1] = self.minHeap.pop()
        i = 1

        # Percolate down
        while 2 * i < len(self.minHeap):
            left = 2 * i
            right = 2 * i + 1
            curr = i

            # Swap right child
            if (right < len(self.minHeap) and 
                self.minHeap[right] < self.minHeap[left] and self.minHeap[right] < self.minHeap[curr]):
                self.minHeap[curr], self.minHeap[right] = self.minHeap[right], self.minHeap[curr]
                i = right
            
            # Swap left child
            elif self.minHeap[left] < self.minHeap[curr]:
                self.minHeap[curr], self.minHeap[left] = self.minHeap[left], self.minHeap[curr]
                i = left
            
            else:
                break
        return res


    def top(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        
        return self.minHeap[1]
        

    def heapify(self, nums: List[int]) -> None:
        self.minHeap = [0] + nums
        
        curr = (len(self.minHeap) - 1) // 2

        while curr > 0:
            i = curr
            # Percolate down
            while 2 * i < len(self.minHeap):
                left = 2 * i
                right = 2 * i + 1

                # Swap right child
                if (right < len(self.minHeap) and 
                    self.minHeap[right] < self.minHeap[left] and self.minHeap[right] < self.minHeap[i]):
                    self.minHeap[i], self.minHeap[right] = self.minHeap[right], self.minHeap[i]
                    i = right
                
                # Swap left child
                elif self.minHeap[left] < self.minHeap[i]:
                    self.minHeap[i], self.minHeap[left] = self.minHeap[left], self.minHeap[i]
                    i = left
                
                else:
                    break
            curr -= 1
        
        