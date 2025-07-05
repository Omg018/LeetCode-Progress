class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # count = Counter(arr)
        # print(count)

        # max_lucky = -1
        # for i, val in count.items():
        #     print(i, val)
        #     if i == val:
        #         max_lucky = max(max_lucky, i)

        # return max_lucky

        
       
        count = Counter(arr)
        maxi = -1
        for i,val in count.items():
            print('om')
          
            if i == val:
                
                maxi = max(maxi,i)
                print(maxi)
        return maxi

         


 #  d = {}

        #  for i,num in enumerate(arr):
        #     print(i+1,num)
        
        # for i in range(len(arr)):
