class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted((nums))
        d = {}
        
        for i,val in enumerate(temp):
            if val not in d:
                d[val] = i
               
        print(d)

        ret = []

        for i in nums:
            ret.append(d[i])
        return ret
        
        
        
        # arr = []
        # for i in range(len(nums)):
        #     k = 0
        #     nums[i]
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             k = k + 1
        #     arr.append(k)
        # return arr    
        
               
                    
               
