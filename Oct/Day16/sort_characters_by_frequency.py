class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        sorted_chars = sorted(freq.keys(), key=lambda ch: freq[ch], reverse=True)
        
        res = []
        for ch in sorted_chars:
            res.append(ch * freq[ch])
            
        return "".join(res)
