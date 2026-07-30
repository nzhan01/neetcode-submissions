class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ordered = []
        fleets = len(ordered)
        stack = []
        for i in range(len(position)):
            #print(i)
            time = (target- position[i])/ speed[i]
            ordered.append([position[i],speed[i],time]) 
        
        ordered.sort(reverse=True) 
        stack.append(ordered[0][2]) # set first time to stack

        for x in range(1,len(ordered)):
            print(ordered[x])
            if ordered[x][2] > stack[-1]:
                stack.append(ordered[x][2])
            


        return len(stack)