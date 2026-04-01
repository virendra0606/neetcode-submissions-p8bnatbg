class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(numbers)):
            rem = target -numbers[i]
            if rem in dict:
                return [dict[rem],i+1]
            
            dict[numbers[i]] = i+1
        return []
        