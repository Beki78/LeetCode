class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic = {}
        count = 0
        for i in range(len(nums)):
            dic[nums[i]] = i 
        for num in nums:
            if (num + diff) in dic and (num + 2 * diff) in dic:
                count += 1
        return count
        