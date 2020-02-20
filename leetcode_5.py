def isPalindrome(s: str) -> bool:
    leftStack = []
    rightStack = []
    for i in range(len(s)//2):
        leftStack.append(s[i])
        rightStack.append(s[-(i+1)])
    print(leftStack)
    print(rightStack)
    while len(leftStack) != 0 and len(rightStack) != 0:
        if leftStack.pop() != rightStack.pop():
            return False
    if len(leftStack) != 0 or len(rightStack) != 0:
        return False
    return True

print(isPalindrome("abba"))
print(isPalindrome("acba"))
print(isPalindrome("ababa"))
