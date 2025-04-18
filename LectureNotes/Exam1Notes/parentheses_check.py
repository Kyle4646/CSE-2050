'''
Task: Write a function parentheses_check using the Stack ADT you wrote in Stack.py
Specifics:
- There are only two types of parentheses here, () and []
- They will be used in a string where ANY other characters are allowed
- You need to tell me if the parentheses are valid
- That means that no parentheses are left open
- That also means that parentheses opened inside others must be closed inside them too
- Eg. [(]) would be FALSE because ( is inside of [] but ) is outside
- Return True is parentheses are valid, False if not
'''

from Stack import Stack

def parentheses_check(str_input):
    """Check if the string contains valid parentheses."""
    s = Stack()
    
    for c in str_input:
        if c in "([":  
            s.push(c)
        elif c in ")]":  
            if s.is_empty():  
                return False
            top = s.pop()
            if (top == '(' and c != ')') or (top == '[' and c != ']'):
                return False
    
    return s.is_empty()

# Example usage
if __name__ == "__main__":
    test_strings = ["()", "[()]", "[([])]", "([)]", "([)"]
    for test in test_strings:
        print(f"{test}: {parentheses_check(test)}")