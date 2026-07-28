class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second_lar = 0

        for num in nums:
            if num > largest:
                second_lar = largest
                largest = num
            elif num > second_lar:
                second_lar = num
        ans = (second_lar - 1) * (largest - 1)
        return ans


        # sort_num = sorted(nums, reverse= True)
        # first_ele = sort_num[0:1]
        # second_ele = sort_num[1:2]
   

        # ans = (first_ele[0] - 1) * (second_ele[0] - 1)
        # return ans

        
