class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #convert to negative to use min heap
        stones = [-x for x in stones]

        #turn into min heap
        heapq.heapify(stones)

        #loop to iterate through until none left or only 1
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

        #y cannot be greater than x
        #if y is different than x, then we need to smash together
        # x = -6, y = -5,   push x - y = -1
            if x != y:
                heapq.heappush(stones, x -y)
        # append 0 in case of x == y, leaving empty heap
        stones.append(0)
        #return back into positive value
        return abs(stones[0])





