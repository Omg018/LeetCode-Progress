class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, ele in enumerate(nums):
            check = target - ele
            if check in seen:
                return [seen[check], i]
            seen[ele] = i        
        
