class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for item in nums:
            if item in data:
                return True
            else:
                data[item]=item
        return False
        