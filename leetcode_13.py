class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        symbolDict = {0:0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
        #return self.solution2(s, 0, symbolDict)
        return self.solution3(s, symbolDict)
        
    # We take the advantage of Roman numbers' rule: 
    # Roman numerals are usually written largest to smallest from left to right
    # Therefore, we can compare each numeral with its further one in each iteration.
    def solution1(self, s:str, tbl: dict) -> int:
        result = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and tbl[s[i]] < tbl[s[i+1]]:
                result += tbl[s[i+1]]-tbl[s[i]]
                i += 2
            else:
                result += tbl[s[i]]
                i += 1
        return result
    
    # We rewrite solution1 in recursive way.
    def solution2(self, s: str, idx: int, tbl: dict) -> int:
        if idx < len(s):
            if idx+1 < len(s) and tbl[s[idx]] < tbl[s[idx+1]]:
                return tbl[s[idx+1]]-tbl[s[idx]] + self.solution2(s, idx+2, tbl)
            else:
                return tbl[s[idx]] + self.solution2(s, idx+1, tbl)
        else:
            return 0
        
    #  We use a stack.
    def solution3(self, s: str, tbl: dict) -> int:
        s_list = [0, 0] + list(s)
        result = 0
        reg1 = 0
        reg2 = 0
        while len(s_list) != 0:
            reg1 = reg2
            reg2 = tbl[s_list.pop()]
            if reg1 > reg2:
                result += reg1-reg2
                reg2 = tbl[s_list.pop()]
            else:
                result += reg1
        return result