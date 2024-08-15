class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #initalize three varibles left , right, size
        #create an empty arr 
        #use two pointers sort
        #in the if statement square it and sort it in decreasing order and use abs
        #in the if statement check if the left value is greater than and append the larger number in to the empty arr
        #else append the right indexed value

        

        size = len(nums)
        left = 00
        right = size -1
        res = [] 

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left +=1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        res.reverse()
        return res
            
        