class Solution:
    def is_sort(self,s):
        strs = list(s)
        strs.sort()
        new_strs = "".join(strs)
        return new_strs
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for item in strs:
            sort = self.is_sort(item)
            if sort in data:
                data[sort]+=[item]
            else:
                data[sort]=[item]
        return list(data.values())