class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ordered = []
        stack = []

        # combine position and speed
        for i in range(len(position)):
            time = (target- position[i])/ speed[i]
            ordered.append([position[i],speed[i],time]) 
        
        #sort by descending position (highest first)
        ordered.sort(reverse=True) 

        stack.append(ordered[0][2]) # set first time to stack

        #iterate through rest of cars
        for x in range(1,len(ordered)):
            print(ordered[x])

            #if car has a slower speed -> form new fleet = new speed push to stack
            if ordered[x][2] > stack[-1]:
                stack.append(ordered[x][2])
            
        # number of speeds = number of fleets
        return len(stack)