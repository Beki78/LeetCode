# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

lst = ["alice","bob","charlie"]

def a(list):
    x = []
    for i in list:
        if i:
            x.append(i[0])
    x = "".join(x)
    print(x)
a(lst)