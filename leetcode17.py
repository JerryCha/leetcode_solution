class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        buttons = { \
                    '1': [], \
                    '2': ['a','b','c'], \
                    '3': ['d', 'e', 'f'], \
                    '4': ['g','h','i'], \
                    '5': ['j', 'k', 'l'], \
                    '6': ['m', 'n', 'o'], \
                    '7': ['p', 'q', 'r', 's'], \
                    '8': ['t', 'u', 'v'], \
                    '9': ['w', 'x', 'y', 'z']
                  }
        
        if len(digits) == 1:
            return buttons[digits]
        
        postfixs = self.letterCombinations(digits[1:])
        prefixs = buttons[digits[0]]
        res = []
        for prefix in prefixs:
            for postfix in postfixs:
                res.append(prefix+postfix)
        return res