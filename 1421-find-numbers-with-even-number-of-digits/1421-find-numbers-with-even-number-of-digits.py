class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #create an empty arr
        #determine the length of each values in the arr 
        #check if the count is % 2 == 0 if yes add them in to the array

        arr = []
        digit_counts = [len(str(abs(i))) for i in nums]
        for i in digit_counts:
            if i % 2 == 0:
                arr.append(i)
        return len(arr)
        

            
        

        