"""
Each opening symbol must match its corresponding closing symbol. For example, a
left bracket, “[,” must match a corresponding right bracket, “],” as in the expression
[(5+x)-(y+z)]. The following examples further illustrate this concept:
• Correct: ( )(( )){([( )])}
• Correct: ((( )(( )){([( )])}))
• Incorrect: )(( )){([( )])}
• Incorrect: ({[])}
"""


def is_matched(expression):
    """Return True if all delimiters are properly matched. False otherwise"""
    left = "({["
    right = ")}]"
    S = Stack()
    for char in expression:
        if char in left:
            S.push(char)
        elif char in right:
            if S.isEmpty():
                return False
            if right.index(char) != left.index(S.pop()):
                return False
    return S.isEmpty()


class Stack:
    def __init__(self):
        """Creates an empty stack"""
        self.data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self.data)

    def isEmpty(self):
        """Return True if the stack is empty"""
        return len(self.data) == 0

    def push(self, item):
        """Add element item to the top of the stack."""
        self.data.append(item)

    def top(self):
        """Return (but not remove) the element at the top of the stack"""
        return self.data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (LIFO)"""
        return self.data.pop()


print(is_matched("[(5+x)-(y-z)]"))  # False

