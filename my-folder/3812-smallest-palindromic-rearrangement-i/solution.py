class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ch_fre = {}
        left = ""
        mid = ""
        
        for ch in s:
            ch_fre[ch] = ch_fre.get(ch, 0) + 1
        
        for ch in sorted(ch_fre):
            
            half = ch_fre[ch] // 2
            left += ch * half
            if ch_fre[ch] % 2 == 1:
                mid = ch

        return left + mid + left[::-1]
            


            
