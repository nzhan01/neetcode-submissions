class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        r = 1
        l = 0

        seen = dict()
        currlongest = 1
        current = s[l]
        seen[s[l]] = 1
        length = 1

        while r < len(s):
            current += s[r]
            length += 1
            if seen.get(s[r]) == None or seen.get(s[r]) == 0:
                seen[s[r]] = 1

                currlongest  = max(length,currlongest )
                
            else:
                if seen[s[r]] == 1: #if duplicate character
                    while seen[s[r]] == 1:
                        seen[s[l]] = 0 #remove seen tag
                        current = current[1:] #decrement string
                        length -= 1
                        l += 1
                    seen[s[r]] = 1
            r+= 1

        return currlongest


