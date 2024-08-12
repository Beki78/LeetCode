class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        #create two different array one for single one for double 
        #loop and append those numbers based on their deigits
        #check if their sum is not equal if not return true else false 

        single_d = []
        double_d = []
        for i in nums:
            if i < 10:
                single_d.append(i)
            else:
                double_d.append(i)
        if sum(single_d) != sum(double_d):
            return True
        else:
            return False
        