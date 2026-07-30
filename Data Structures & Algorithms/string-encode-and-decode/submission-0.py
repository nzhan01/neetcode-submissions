class Solution:


        # turn a list of strings into a single string
    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            length = len(string)
            output += str(length) + "#" + string
        print("output is" + output)
        return output
        

        #turn a single string into a list of strings
    def decode(self, s: str) -> List[str]:
        output = []
        wordLength = ""
        pointer = 0
        while pointer < len(s):
            #print(s[pointer])
            if s[pointer] != "#":
                wordLength += s[pointer]
                pointer += 1
                continue 
            # found #
            wordLength = int(wordLength)
            #print(wordLength)
            word = s[pointer+1: pointer + 1 + wordLength]
        
           
            pointer += wordLength +1
            output.append(word)
            wordLength = ""

        return output





            

