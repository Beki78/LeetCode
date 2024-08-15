class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove the non-alphanumeric characters 
        #change all uppercase to lowercase 
        #using two pointers revers the string
        #if it is reversible return True else False

        cleaned_string = ''.join([char for char in s if char.isalnum()]).lower()
        chars = list(cleaned_string)
        size = len(chars) - 1
        left = 0
        right = size    
        

        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True