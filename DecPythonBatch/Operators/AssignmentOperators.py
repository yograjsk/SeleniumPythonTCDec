

def operations(operation, a):
    if (operation is "incr"):
        print (a)
        a += 2
        print (a)
    if operation is "decr":
        print (a)
        a -= 2
        print (a)
    if operation is "multIncr":
        print (a)
        a *= 2
        print (a)
    if operation is "divDecr":
        print (a)
        a /= 2
        print (a)
    if operation is "assignMod":
        print (a)
        a %= 2
        print (a)
    if operation is "assignExp":
        print (a)
        a **= 2
        print (a)

print(operations("incr", 5))
print(operations("decr", 5))
print(operations("multIncr", 5))
print(operations("divDecr", 5))
print(operations("assignMod", 5))
print(operations("assignExp", 5))