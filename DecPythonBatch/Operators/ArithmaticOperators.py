

def operations(operation, a, b):
    if (operation is "add"):
        return a + b
    if operation is "subtract":
        return a-b
    if operation is "mult":
        return a*b
    if operation is "div":
        return a/b
    if operation is "mod":
        return a%b
    if operation is "exp":
        return a**b

# print(operations("add", 5, 2))
# print(operations("subtract", 5, 2))
# print(operations("mult", 5, 2))
# print(operations("div", 5, 2))
# print(operations("mod", 5, 2))
# print(operations("exp", 5, 3))

def checkEvenOrOdd(num):
    if num%2 is 0:
        print("number is even", num)
    if num%2 is 1:
        print("number is odd", num)

checkEvenOrOdd(20)
