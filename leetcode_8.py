class Solution:
    def myAtoi(self, str: str) -> int:
        '''
            Due to the design of integer system of Python, there is impossible that
            an integet could exceed a given precision, which is signed 32-bit 
            in this question. 
            As a consequence, Python solution does not need to consider 
            overflow problem. But keep in mind, range check is compulsory in Java,
            C, or other strongly typed language.
        '''
        # Establish the valid range
        LOWER_BOUND = -1<<31    # -2^31
        UPPER_BOUND = (1<<31) - 1 # 2^31 - 1
        # Use a stack to keep the token read from given string
        stack = []
        # Iterate through the string
        for c in str:
            '''
            Divide the case based on the length of stack. 
            len(stack) > 0 is equivalent to already found a valid token.
            '''
            # Stack is empty: we need to check the started character is valid.
            if len(stack) == 0:
                # Valid case 1: starting with number or +, -
                if c in "-+0123456789":
                    stack.append(c)
                # Valid case 2: starting with empty space ' '. 
                # If it is the case, keep iteration
                elif c == ' ':
                    continue
                # Otherwise, return 0.
                else:
                    return 0
            # Stack is not empty: we already found the valid starting character.
            else:
                # If we read continuous digit, we keep pushing to the stack.
                if c in '0123456789':
                    stack.append(c)
                # Once we read a non-numeric character, we stop the iteration.
                else:
                    break
        # Parsing
        num = 0 # Variable for summing during parsing
        factor = 1  # Multiplication factor for summing
        # Popping elements from stack
        while len(stack) > 0:
            token = stack.pop()
            # If the token is negative sign '-', reverse the result
            if token == '-':
                num = -num
            # If the token is positive sign '+', do nothing.
            elif token == '+':
                continue
            # Otherwise, the token must be a digit
            else:
                # Convert the token to integer
                num += int(token)*factor
                # Enlarge factor by 10 times 
                factor *= 10
        # Check range
        # Note that the practical way in strongly typed language is to compare the previous state and the current state. If the new state is smaller than the previous state, it must be overflowed. 
        if num >= LOWER_BOUND and num <= UPPER_BOUND:
            return num
        elif num < LOWER_BOUND:
            return LOWER_BOUND
        else:
            return UPPER_BOUND