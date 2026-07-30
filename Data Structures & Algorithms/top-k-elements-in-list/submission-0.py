from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN = Counter(nums)
        sortedCount = dict(sorted(countN.items(), key = lambda item: item[1], reverse = True))
        print(sortedCount)
        return list(sortedCount.keys())[:k]