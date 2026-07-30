class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        


        temp = nums[0]
        for x in range(1,len(nums)):
            prefix[x] = temp
            temp *= nums[x]

        temp = nums[len(nums)-1]
        for x in range(len(nums)-2,-1,-1):
            suffix[x] = temp
            temp *= nums[x]  
            

        print(prefix)
        print(suffix)

        for x in range(len(prefix)):
            prefix[x] = prefix[x] *suffix[x]

        return prefix
