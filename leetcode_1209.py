class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        charStack = []
        countStack = []
        nothingToDelete = True
        for c in s:
            if len(charStack):
                if charStack[-1] == c:
                    countStack[-1] += 1
                else:
                    charStack.append(c)
                    countStack.append(1)
            else:
                charStack.append(c)
                countStack.append(1)
            if countStack[-1] == k:
                charStack.pop()
                countStack.pop()
                nothingToDelete = False
        res = []
        for i in range(len(charStack)):
            c = charStack[i]
            times = countStack[i]
            for _ in range(times):
                res.append(c)
        if nothingToDelete:
            return ''.join(res)
        return self.removeDuplicates(''.join(res), k)