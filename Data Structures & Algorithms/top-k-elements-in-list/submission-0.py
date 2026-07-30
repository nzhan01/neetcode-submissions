class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[]for i in range(len(nums)+1)]
        frequency = {}
        for x in range(len(nums)):
            if nums[x] in frequency:
                frequency[nums[x]] += 1
            else:
                frequency[nums[x]] = 1
        
        #print(frequency.items)
        
        for number,freq in frequency.items():
            bucket[freq].append(number)

        #print(bucket)
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for val in bucket[i]:
                result.append(val)
                if len(result) == k:
                    return result

