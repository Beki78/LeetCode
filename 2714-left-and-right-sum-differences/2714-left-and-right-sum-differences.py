class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        #create 3 different arr for the left right and the result
        #iterate through the list and find the the right and left sums in differerent loop
        #find the sum in the third loop by using abs
        n = len(nums)
        left = [0] * n
        right = [0] * n
        res = [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
        for i in range(n-2, -1, -1):
            right[i] = right[i + 1] + nums[i + 1]
        for i in range(n):
            res[i] = abs(left[i] - right[i])
        return res
        