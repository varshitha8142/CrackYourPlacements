class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a,b=0,len(mat)-1
        i=0;s=0
        while(i<len(mat)):
            if a==b:
                s-=mat[i][a]
            s+=mat[i][a]+mat[i][b]
            a+=1
            b-=1
            i+=1
        return s
            
            
            
        
        