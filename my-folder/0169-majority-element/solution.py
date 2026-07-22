class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        
        for key, value in seen.items():
            if value > len(nums) // 2:
               
                return key
        

        
