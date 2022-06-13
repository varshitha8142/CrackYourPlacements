import re
class Solution:
    def ExtractNumber(self,S):
        #code here
        a=re.findall(r'\d+',S)
        #a1=[i for i in range(len(a)) if '9' not in str(a[i])]
        a1=[int(a[i]) for i in range(len(a)) if '9' not in str(a[i])]
        if(a1==[]):
            return -1
        return max(a1)
        

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends