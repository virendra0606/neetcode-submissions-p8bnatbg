class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data ={}
        for i in range(len(nums)):
            result=target-nums[i]
            if result in data:
                return list(data[result]+[i])
            data[nums[i]]=[i]
        