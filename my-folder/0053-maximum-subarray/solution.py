class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        iterator = iter(nums)
        next(iterator)
     

        for num in iterator:
            curSum = num if num > curSum + num else curSum + num

            if maxSum < curSum:
                maxSum = curSum

            
        
        return maxSum
           
            
     
