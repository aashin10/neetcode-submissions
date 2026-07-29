from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = dict()
        for i, word in enumerate(strs):
            countWordFrozen = frozenset(Counter(word).items())
            if countWordFrozen not in anagramMap:
                anagramMap[countWordFrozen] = [word]
            else:
                anagramMap[countWordFrozen].append(word)
        return list(anagramMap.values())