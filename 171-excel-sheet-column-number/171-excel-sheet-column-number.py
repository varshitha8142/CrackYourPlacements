class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c=len(columnTitle)-1
        x=0
        for i in columnTitle:
            x+=(26**c)*(ord(i)-64)
            c-=1
        return x
        