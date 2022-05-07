class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return ''.join(i[0] for i in itertools.takewhile(lambda x: len(set(x)) == 1, zip(*strs)))
        