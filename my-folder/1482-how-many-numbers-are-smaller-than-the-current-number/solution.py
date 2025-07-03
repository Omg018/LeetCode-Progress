class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        arr = []
        for i in range(len(nums)):
            k = 0
            nums[i]
            for j in range(len(nums)):
                
               
                if nums[i] > nums[j]:
                    
                    k = k + 1
                    
            arr.append(k)
             
        return arr    
        
               
                    
               
