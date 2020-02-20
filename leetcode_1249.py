class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        leftStack = []
        for i in range(len(s)):
            if s[i] == '(':
                leftStack.append((i, s[i]))
            elif s[i] == ')':
                if len(leftStack) == 0:
                    s[i] = ''
                else:
                    leftStack.pop()
        for i,_ in leftStack:
            s[i] = ''
        
        return ''.join(s)