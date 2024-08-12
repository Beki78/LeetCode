class Solution:
    def repeatedCharacter(self, s: str) -> str:
        #create an empty set
        #loop through in the string 
        #check if the current letter is in the set if yes return the letter if not add to the set
        set_string = set()

        for i in s:
            if i in set_string:
                return i
            else:
                set_string.add(i)


        
        