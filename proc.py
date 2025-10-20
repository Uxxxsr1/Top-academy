stack = []
def push(val):
    stack.append(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(5)
push(7)
push(20)
print(pop())
print(pop())
print(pop())