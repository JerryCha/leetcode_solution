class Solution:
    '''
        Recursion
    '''
    def isSubsequence1(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        for i in range(len(t)):
            if s[0] == t[i]:
                return self.isSubsequence(s[1:], t[i+1:])
        return False
    
    '''
        Iteration with 2x pointers
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        elif len(s) == 0 or len(t) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        sPointer = 0
        for c in t:
            if s[sPointer] == c:
                sPointer += 1
            if sPointer == len(s):
                return True
        return False