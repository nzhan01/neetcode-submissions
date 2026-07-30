class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        Intset = set(nums)
        longest = 0

        for x in nums:
            length = 1
            if (x - 1) not in Intset:
                
                while (x+1) in Intset:
                    x+= 1
                    length += 1
            longest = max(length, longest)


        return longest
