class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #first we will create an empty stack
        #loop theough the array
        #give theh condition -
                #if the input is intiger add to the stack 
                #if the input is c pop the last element
                #if the input is d multiply it by two
                #if the input is + sum the last two stacks and add new num in to the stack
        #return the sum of the stacks 

        stack = []
        for i in operations:
            if i == "C":
                if stack:
                    stack.pop()
            elif i == "D":
                if stack:
                    stack.append(2 * stack[-1])
            elif i == "+":
                if len(stack) >= 2:
                    stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)

        