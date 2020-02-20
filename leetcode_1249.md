# 1249. Minimum Remove to Make Valid Parentheses

## Problem

Given a string s of `'('` , `')'` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return **any** valid string.

Formally, a parentheses string is valid if and only if:

* It is empty string, contains only lowercase characters, or

* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or

* It can be written as `(A)`, where `A` is a valid string.

**Example 1:**

```py
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**

```py
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**

```py
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

**Example 4:**

```py
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
```

## Solution

We use a stack to keep track of left parentheses. All right parentheses are well paired with the left one when the stack is empty finally. This solution is inspired by the solution of checking the balance of parentheses.

To accommodate the problem, we modify the content we push into stack. Besides left parentheses, we add the index where this one exists in the given string so that we can delete the unnecessary parentheses from string. We need to delete either left or right parentheses or both of them. Furthermore, it is tricky that any pair of parenthese should enclose a substring. In other words, any pair in order `)(` is also invalid.

Our strategy is to delete any right parentheses when the stack is empty. After iterated the given string, we back to stack and pop all of them and get the index of that left parentheses to delete unpaired left parentheses.

```py
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
```
