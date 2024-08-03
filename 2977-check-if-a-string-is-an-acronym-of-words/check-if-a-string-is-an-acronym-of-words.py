class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = []
        for i in words:
            if i:
                x.append(i[0])
        x = "".join(x)
        if (x==s):
            return(True)
        

        