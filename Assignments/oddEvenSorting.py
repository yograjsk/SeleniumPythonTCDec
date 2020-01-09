

def checkevenodd(list):
    evenList = []
    oddList = []
    for n in list:
        if n % 2 == 0:
            print("This is even number", n)
            evenList.append(n)
        else:
            print("This is odd number", n)
            oddList.append(n)
    print("Even Numbers", evenList)
    print("Odd Numbers", oddList)
list = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
checkevenodd(list)
