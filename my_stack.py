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

# Новий стек порожній
assert stack.is_empty() is True
assert stack.peek() is None
assert stack.pop() is None

# Додавання елементів
stack.push("one")
stack.push("two")

assert stack.is_empty() is False
assert stack.peek() == "two"

# Видалення за принципом LIFO
assert stack.pop() == "two"
assert stack.pop() == "one"

# Після видалення всіх елементів стек знову порожній
assert stack.is_empty() is True

print("Усі тести успішно пройдені")