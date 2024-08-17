class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        p = []
        n = []

        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                n.append(i)
            else:       
                p.append(i)

        if not p:
            return max(n)
        if not n:
            return min(p)
        
        if abs(max(n)) < abs(min(p)):
            return max(n)
        else:
            return min(p)