class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        init = 0
        for i in operations:
            if i == "++X" or i =="X++":
                init +=1
            elif i == "--X" or i =="X--":
                init -= 1
        return init
        