# def peek(stack: list) -> str:
#   return stack[-1]

# def is_empty(stack: list) -> bool:
#   return len(stack) == 0

# stack = []

# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')
# stack.append('e')
# stack.append('f')
# print(stack)

# print(stack.pop())
# print(stack)
# print(peek(stack))
# print(stack)
# print(is_empty(stack))

class Stack:
    def __init__(self) -> None:
        self.stack = list()

    def push(self, item: str) -> None:
        self.stack.append(item)

    def pop(self) -> str:
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def peek(self) -> str:
        if not self.is_empty():
            return self.stack[-1]

stack = Stack()

stack.push('a')
stack.push('b')
stack.push('c')

print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())