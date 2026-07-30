class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        solution = set()

        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            target = -1 * (nums[i])
            while l < r:
                if nums[l] + nums[r] == target:
                    if tuple([nums[l], nums[r],nums[i]]) not in solution:
                        solution.add(tuple([nums[l], nums[r],nums[i]]))
                    l+= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r-= 1



        return [list(x) for x in solution]