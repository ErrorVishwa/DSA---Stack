# Creating a Empty stack
stack = [] # Creating a Stack into List

# Adding Element into stack
stack.append("Actors")    # Use Append for push .If you declare push into stack it gets an attribute error.In python You Must append for adding element into stack
stack.append("Hackers")
stack.append("Doctors")
stack.append("Officer")

print("Intial Stack")
print(stack)

# Popping element from the stack
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

#print(stack.pop()) # You cant use pop () to an empty stack
print("\n Stack after the elements are popped")
print(stack)