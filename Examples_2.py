# Stack implementation in python using collections.deque
from collections import deque

stack = deque()

# Append function to push elements into stack
stack.append("hindu")
stack.append("muslim")
stack.append("Christian")

print("Intial Stack")
print(stack)

# Pop function to delete elements from the stack using LIFO order
print("\n Elements popped from the stack :")
print(stack.pop())
print(stack.pop())

# Display stack after popped
print("\n Stack after elements are popped:")
print(stack)