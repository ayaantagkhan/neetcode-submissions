class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cunt = {}
        freakq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            cunt[n] = 1 + cunt.get(n,0)
        for n, c in cunt.items():
            freakq[c].append(n)
        
        res = []
        for i in range(len(freakq)- 1, 0, -1):
            for n in freakq[i]:
                res.append(n)
                if len(res) == k:
                    return res
