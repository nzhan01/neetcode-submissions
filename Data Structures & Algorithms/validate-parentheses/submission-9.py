class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2 or (len(s)%2 != 0 ):
            return False
        
        for i in range(len(s)):
            if s[i] in "{[(":
                stack.append(s[i])
            else:
                if s[i] in "}])" and stack:
                    top = stack.pop()
                    if top == "[" and s[i] != "]":
                        return False
                    if top == "{" and s[i] != "}":
                        return False
                    if top == "("and s[i] != ")":
                        return False
                else:
                    return False
        if not stack:
            return True 
        else:
            return False