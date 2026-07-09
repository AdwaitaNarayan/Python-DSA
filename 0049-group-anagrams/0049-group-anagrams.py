class Solution:
    def sorting(self, s):
        t = list(s)
        t.sort()
        return "".join(t)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for s in strs:
            key = self.sorting(s)
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key] = [s]
        
        return list(dict1.values())

        