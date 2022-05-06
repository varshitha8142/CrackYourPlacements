class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a,2)+int(b,2)
        d=bin(c)
        e=d.replace("0b",'')
        return ((e))
        