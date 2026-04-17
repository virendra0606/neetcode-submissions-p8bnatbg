class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data ={}
        for i in nums:
            if i in data:
                return True
            data[i]=i
        return False
        