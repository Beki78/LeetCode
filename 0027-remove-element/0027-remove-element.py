class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = 0
        for i in nums:
            if i != val:
                nums[size] = i
                size += 1
        return size

        
        