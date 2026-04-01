class Solution:
    def isSort(self,c):
        s = list(c)
        s.sort()
        new ="".join(s)
        return new
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in range(len(strs)):
            sort = self.isSort(strs[s])
            if sort in dict:
                dict[sort]+=[strs[s]]
            else:
                dict[sort]=[strs[s]]
        
        return list(dict.values())
        