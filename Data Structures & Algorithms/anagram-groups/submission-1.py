class Solution:
    def is_short(self,s):
        strs = list(s)
        strs.sort()
        new = "".join(strs)
        return new
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for i in range(len(strs)):
            sort = self.is_short(strs[i])
            if sort in data:
                data[sort]+=[strs[i]]
            else:
                data[sort]=[strs[i]]
        return list(data.values())

        