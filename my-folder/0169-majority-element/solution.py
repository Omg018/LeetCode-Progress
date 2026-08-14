class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        seensort = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            # seensort = sorted(seen.keys(), reverse = True)
        for num, freq in seen.items():
            if freq > len(nums) // 2:
                return num







        # seen = {}
        # for i in nums:
        #     seen[i] = seen.get(i, 0) + 1
        
        # for key, value in seen.items():
        #     if value > len(nums) // 2:
               
        #         return key
        

        
