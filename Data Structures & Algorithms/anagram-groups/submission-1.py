class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for s in strs:
            sortedString = sorted(s)

            result[tuple(sortedString)].append(s)

        return list(result.values())