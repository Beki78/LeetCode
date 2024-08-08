class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    hash_map[(i,j)] = nums[i] , nums[j]
        ans =  hash_map.values()
        return len(ans)
        