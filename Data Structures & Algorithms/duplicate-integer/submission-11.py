class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = set()

        for x in nums:
            if x in current:
                return True
            else:
                current.add(x)
        
        return False