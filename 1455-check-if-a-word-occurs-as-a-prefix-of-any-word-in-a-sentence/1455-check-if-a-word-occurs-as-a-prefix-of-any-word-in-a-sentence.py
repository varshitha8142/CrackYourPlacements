class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        c=0;x=0
        #if searchWord in sentence:
        sentence=sentence.split()
        for i in sentence:
            c+=1
            if searchWord == i[:len(searchWord)]:
                x+=1
                return(c)
        if x==0:
            return(-1)