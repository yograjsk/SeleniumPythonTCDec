
def CompOperations(a, b):
    if (a == b):
        print(a, "and", b, "are equal")
    if (a == b ):
        print(a, "and", b, "are equal")
    if (a < b):
        print(a, "is smaller than", b)
    if (a > b):
        print(a, "is greater than", b)

    while(a<=b):
        a+=1
        print(a)

    while(a>=b):
        a-=1
        print(a)


# CompOperations(10, 10)
# CompOperations(10, 20)
CompOperations(20, 10)
# CompOperations(10, 10)

# print(operations("add", 5, 2))
# print(operations("subtract", 5, 2))
# print(operations("mult", 5, 2))
# print(operations("div", 5, 2))
# print(operations("mod", 5, 2))
# print(operations("exp", 5, 3))