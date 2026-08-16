"""
matrix
target

it is in increasing order first row end and second row start is also in increasing order

if target matched true else false

binary

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (right + left) // 2
            
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False







        # totalarr = []
        # for subarr in matrix:
        #     left = 0
        #     for items in subarr:
        #         totalarr.append(items)
        # print(totalarr)

        # left = 0
        # right = len(totalarr) - 1

        # while left <= right:
        #     mid = (right + left) // 2
        #     if totalarr[mid] == target:
        #         return True
        #     elif totalarr[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False    
        # # left = 0
        # # right = matrix[[]]
        
