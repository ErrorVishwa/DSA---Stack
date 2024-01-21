# Stack implementation using queue module 
from queue import LifoQueue

# Intializing the stack
stack = LifoQueue(maxsize=3)

# Show the number elements into stack
print(stack.qsize())

# Put function to push elements from the stack
stack.put('Python')
stack.put("Java")
stack.put("C++")

print("Full:",stack.full())
print("Size:",stack.qsize())

# Get() function to pop elements from the stack
print("\n Elements are get from the Stack:")
print(stack.get())
print(stack.get())

print("\n Empty:", stack.empty())