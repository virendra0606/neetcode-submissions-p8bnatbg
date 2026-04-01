class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for i in range(len(nums)):
            if nums[i] in data:
                return True
            else:
                data[nums[i]] = i
        return False

        
        