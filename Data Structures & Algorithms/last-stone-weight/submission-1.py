import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #sortedStones = [x for x in stones]
        heapq.heapify_max(stones)
        #x = heapq.heappop_max(sortedStones)
        #print(x)
        while len(stones) >=1:
            x = heapq.heappop_max(stones)
            print("x = " , x)
            if len(stones) == 0:
                return x
            y = heapq.heappop_max(stones)
            print("y = " , y)
            if x == y:
                continue
            if x < y:
                y = y - x
                heapq.heappush_max(stones, y)
                print("pushed ", y)
                print("new heap =", stones)
            if x > y:
                x = x - y
                heapq.heappush_max(stones, x)
                print("pushed ", x)
                print("new heap =", stones)
            
        return 0