class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of both input strings
        len_text1, len_text2 = len(text1), len(text2)
      
        # Initialize a 2D array (list of lists) with zeros for dynamic programming
        # The array has (len_text1 + 1) rows and (len_text2 + 1) columns
        dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]
      
        # Loop through each character index of text1 and text2
        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                # If the characters match, take the diagonal value and add 1
                if text1[i - 1] == text2[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    # If the characters do not match, take the maximum of the value from the left and above
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
      
        # The bottom-right value in the matrix contains the length of the longest common subsequence
        return dp_matrix[len_text1][len_text2]
        # dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        # len1, len2 = len(text1),len(text2) 

        # for i in range(len1 - 1 , -1,-1):
        #     for j in range(len2 - 1 , -1,-1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
                   
        #         else:
        #             dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                
           
        # return dp[0][0]
        
