name = "global"

def print_name():
    global name
    name = "function block"
    print(name)

print_name()

print(name)
