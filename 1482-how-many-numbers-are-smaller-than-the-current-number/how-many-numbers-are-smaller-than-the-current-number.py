class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        new_num = sorted(nums)
        for i in nums:
            arr.append(new_num.index(i))
        return arr
        