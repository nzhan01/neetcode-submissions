class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # keep track of duplicates
        l = 0 # left pointer
        longest = 0 


        for r in range(len(s)): #iterate through string with right pointer
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l +1)

        return longest

