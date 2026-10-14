class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if not words:
            return []
            
        common = {}
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1
            
        for word in words[1:]:
            curr = {}
            for ch in word:
                curr[ch] = curr.get(ch, 0) + 1
                
            for ch in list(common.keys()):
                if ch in curr:
                    common[ch] = min(common[ch], curr[ch])
                else:
                    del common[ch]
                    
        res = []
        for ch, count in common.items():
            res.extend([ch] * count)
            
        return res
