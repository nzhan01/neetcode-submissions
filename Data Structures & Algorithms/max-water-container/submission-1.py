class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer sliding window, update pointer with lower val

        #Area = (min(heights[x], heights[y])) * (x-y)
        CurrentMax = 0
        #initialize 2 pointers
        x= 0
        y= len(heights)-1

        while x < y:
            volume = min(heights[x], heights[y]) * abs(x-y)
            if volume > CurrentMax:
                CurrentMax = volume

            if heights[x] < heights[y]:
                x += 1
            else: 
                y-= 1


            


        return CurrentMax