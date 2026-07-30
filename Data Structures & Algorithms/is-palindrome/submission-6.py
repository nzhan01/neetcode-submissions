class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        x = 0
        y = len(s) - 1

        while (x < y):
            print([ord(s[x].lower()),ord(s[y].lower()) ])
            while x<y and not (
                 (97 <= ord(s[x].lower()) <= 122 ) or (48 <= ord(s[x]) <= 57)):


                x+=1
            while x<y and not (
                 (97 <= ord(s[y].lower()) <= 122 ) or (48 <= ord(s[y]) <= 57)):
                y-=1
            print(s[x],s[y])
            if s[x].lower() != s[y].lower():
                return False
            x += 1
            y -= 1
            print(x,y)
        return True