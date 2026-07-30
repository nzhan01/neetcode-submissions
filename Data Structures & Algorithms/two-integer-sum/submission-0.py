class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difs = {}


        for x in range(len(nums)):
            difference = target - nums[x]
            if difference in difs:
                return [difs[difference],x]
            else:
                difs[nums[x]]= x
        #print(difs)
        