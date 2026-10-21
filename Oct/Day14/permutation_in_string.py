class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
            
        target = {}
        window = {}
        for ch in s1:
            target[ch] = target.get(ch, 0) + 1
            
        for i in range(n1):
            ch = s2[i]
            window[ch] = window.get(ch, 0) + 1
            
        if window == target:
            return True
            
        for i in range(n1, n2):
            ch_in = s2[i]
            window[ch_in] = window.get(ch_in, 0) + 1
            
            ch_out = s2[i - n1]
            if window[ch_out] == 1:
                del window[ch_out]
            else:
                window[ch_out] -= 1
                
            if window == target:
                return True
                
        return False
