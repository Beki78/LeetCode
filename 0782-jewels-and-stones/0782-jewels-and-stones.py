class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_list = []
        for i in jewels:
            for j in stones:
                if i == j:
                    hash_list.append((i,j)) 
        return len(hash_list)

        