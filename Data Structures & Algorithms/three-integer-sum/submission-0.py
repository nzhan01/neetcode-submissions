class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        solution = set()
        length = range(len(nums))
        nums.sort()
        for x in length:
            for y in range(x+1,len(nums)):
                
                for z in range(y+1,len(nums)):
                    sum = nums[x] + nums[y] + nums[z]
                    if sum == 0: 
                        if tuple([nums[x],nums[y],nums[z]]) not in solution:
                                solution.add(tuple([nums[x],nums[y],nums[z]]))






        return [list(x) for x in solution]