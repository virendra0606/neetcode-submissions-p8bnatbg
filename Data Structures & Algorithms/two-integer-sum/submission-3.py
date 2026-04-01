class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        
        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in data:
                return list(data[difference]+[i])
            
            data[nums[i]]=[i]
    