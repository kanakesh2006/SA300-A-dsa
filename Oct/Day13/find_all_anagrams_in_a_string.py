class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
            
        p_count = {}
        s_count = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
            
        k = len(p)
        for i in range(k):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            
        res = []
        if s_count == p_count:
            res.append(0)
            
        for i in range(k, len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            
            old_char = s[i - k]
            if s_count[old_char] == 1:
                del s_count[old_char]
            else:
                s_count[old_char] -= 1
                
            if s_count == p_count:
                res.append(i - k + 1)
                
        return res
