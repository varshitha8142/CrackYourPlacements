class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=[str(i) for i in digits]
        b="".join(a)
        b=int(b)+1
        b=[int(i) for i in str(b)]
        return b
        