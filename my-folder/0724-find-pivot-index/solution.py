class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lprefix = [0]
        for num in nums:
            lprefix.append(lprefix[-1] + num)
        rprefix = [0]
        for num in nums[::-1]:
            rprefix.append(rprefix[-1] + num)
        
        for i in range(len(nums)):
            if lprefix[i] == rprefix[len(nums) - i - 1]:
                return i
        return -1


        # for i in range(len(nums)):
        #     if lprefix[i+1] == rprefix[i+1 ]:

        
        
        # for i in range(len(nums)):
        #     left = 
        #     if nums[0]:
        #         return -1
        #     elif nums[-1]:
        #         return -1
            
