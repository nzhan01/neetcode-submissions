class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [temp, index]
        output = [0] * len(temperatures)
        for x in range(len(temperatures)):

            while stack and temperatures[x] > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                output[stackIndex] = (x-stackIndex)
            
            stack.append([temperatures[x],x])
        return output

