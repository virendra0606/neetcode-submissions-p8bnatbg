class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for num in range(len(nums)):
            result = target-nums[num]
            if result in data:
                return list(data[result]+[num])
            data[nums[num]] = [num]
        