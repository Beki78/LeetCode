class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #loop throught all the elements and count the number of occurrence
        #count the number of counts and put it in to hashmap
        #hashmap = (numberof occurrence, the value)
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        most_occurrences = max(hash_table, key=hash_table.get)

        return most_occurrences