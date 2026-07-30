class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string1 = {}
        string2 = {}

        if len(s) != len(t):
            return False
        for x in s:
            if x in string1:
                string1[x] += 1
            else:
                string1[x] = 1
        
        for y in t:
            if y not in string1:
                return False
            elif y in string2:
                string2[y] +=1
            else:
                string2[y]= 1
        
        return string1 == string2
            
        
