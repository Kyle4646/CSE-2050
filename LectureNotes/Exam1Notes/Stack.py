'''
Task: Implement a Stack ADT
Methods:
- init
- push
- pop
- peek
- is_empty
- len
- str
'''

class Stack:
    """
    A class representing a Stack (LIFO - Last In, First Out) Abstract Data Type.
    """
    
    def __init__(self):
        """Initialize an empty stack using a list."""
        self.items = []
    
    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item of the stack. Raises an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item of the stack without removing it. Raises an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        """Return a string representation of the stack."""
        return "Stack: " + str(self.items)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)  # Output: Stack: [1, 2, 3]
    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.is_empty())  # Output: False
    print(stack.size())  # Output: 2