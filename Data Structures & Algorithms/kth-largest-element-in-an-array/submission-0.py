from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #nums = [-x for x in nums]

        temp = []
        heapify(temp)
        for x in range(k):
            heappush(temp, nums[x])
            print("pushed", nums[x])
        
        for num in nums[k:]:
            print("checking num", num)
            if num > temp[0]:
                
                heappop(temp)
                heappush(temp,num)

        
        #temp = [-x for x in temp]
        return temp[0]
            

