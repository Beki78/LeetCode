class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #create an empty arr with the value of 0
        #loop through each element and find the cumulative 
        #return the arr
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i]
        return sums