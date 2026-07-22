class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
        dic = {}

        for i, ele in enumerate(nums):
            check = target - ele
            if check in dic:
                return [dic[check], i]
            
            dic[ele] = i







        # for i in range(len(nums)):
        #     sol = nums[i] - target
        #     for j in range(len(nums)):
        #         if sol == nums[j]:
                    
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+ nums[j] == target):
        #             arr = []
        #             arr.append(i)
        #             arr.append(j)
        #             return arr


        






        # dic = {}

        # for i, num in enumerate(nums):
        #     comp = target - num
        #     if comp in dic:
        #         return [dic[comp], i]

        #     dic[num] = i
