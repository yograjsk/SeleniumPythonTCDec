

def checkListNumbers(list):
    for n in list:
        if n == 0:
            print("Number", n, "is Zero")
        elif n < 0:
            print("Number", n, "is negative")
        elif n > 0:
            print("Number", n, "is positive")
            i = 0
            while(i <= n):
                print(">>>>", i)
                i = i+1

list1 = [1,2,3,0,-3,-10,5,0]
checkListNumbers(list1)

'''
take a number list as a parameter and run through their indexes and check if the number is even or odd
'''