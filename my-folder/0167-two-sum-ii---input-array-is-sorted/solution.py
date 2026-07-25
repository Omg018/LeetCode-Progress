class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            print(current)

            if current == target:
                return [left + 1, right + 1]
            elif current > target:
                right -= 1
            else:
                left += 1 
        return[]
            
        

        # for i, num in enumerate(numbers):
        #     comp = target - num
        #     if comp in numbers:

