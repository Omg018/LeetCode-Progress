class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)
        return best
        # best = 0 
        # for start in range(len(s)):
        #     seen = set()
        #     if not seen:
        #         seen.add(s[start])
        #     elif seen == s[start]:
        #         break
        #     elif seen != s[start]:
        #         seen.add(s[start])
        #     print(seen)
            
        
                     
            # for end in range(start, len(s)):
            #     if not seen:
            #         s[start]
            #     if 
                     

             
                    
            
                    
