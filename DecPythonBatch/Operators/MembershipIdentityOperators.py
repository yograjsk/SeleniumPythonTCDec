
def Members(text):
    if text in ("a", "b", "aa", "bb"):
        print (text, "is present")
    if text not in ("a", "b", "aa", "bb"):
        print (text, "is NOT present")

    if text is "aa":
        print (text, "is aa")
    if text is not "aa":
        print (text, "is NOT aa")

Members("aa")
Members("xx")

'''
Assignment:
Create a function which takes the list of numbers as a parameter and check every number, if its even or odd
print "number is even" if its even
print "number is odd" if its odd
for example from the list below:
list1 = [1,2,3,4,5]
'''