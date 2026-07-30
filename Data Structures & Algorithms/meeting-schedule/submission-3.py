"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def quicksort(intervals):

            if len(intervals)<=1:
                return intervals

            pivot = intervals[len(intervals)//2].start

            left = [x for x in intervals if x.start< pivot]
            middle= [x for x in intervals if x.start == pivot]
            right = [x for x in intervals if x.start > pivot]
            #print(pivot)
            #print(left)

            return quicksort(left) + middle + quicksort(right)

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <=1:
            return True

        sortedIntervals = quicksort(intervals)
        #print(sortedIntervals)
        

        x = 0
        y= 1
        #print(x.start, y.start)
        length = len(sortedIntervals)
        for i in range(length-1):
            if sortedIntervals[i].end > sortedIntervals[i+1].start:
                return False
            #if sortedIntervals[i].start == sortedIntervals[y].start:
              #  return False
            x+= 1
            y+= 1

        return True        

