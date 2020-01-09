

def printString(text):
    print("Executing printString")
    for a in text:
        print(a)

def printString_logicFlow(text):
    print("Executing printString_logicFlow")
    length = len(text)
    i = 0
    while(i < length):
        print(text[i])
        i = i+1

    # for a in text:
    #     print(a)

def printList(list):
    for n in list:
        print(n)

def printRange(startNumber, rangeNumber, jumbBy):
    for n in range(startNumber, rangeNumber, jumbBy):
        print(n)

printString("TECHCANVASS")

# list1 = [1,2,3,4,5,6]
# printList(list1)

# printRange(1, 11, 2)

printString_logicFlow("TECHCANVASS")