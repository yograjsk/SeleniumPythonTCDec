# defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

emp = Employee("Ironman", 999000)
print(emp.sal)

# defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name   # protected attribute
        self._sal = sal     # protected attribute

emp = Employee("Captain", 10000)
print(emp._sal)


# defining a child class
class HR(Employee):

    # member function task
    def task(self):
        print ("We manage Employees")

hrEmp = HR("Captain", 10000)
print(hrEmp._sal)
#10000
hrEmp.task()
#We manage Employees

# defining class Employee
class Employee:
    def __init__(self, name, sal):
        self.__name = name    # private attribute
        self.__sal = sal      # private attribute

emp = Employee("Bill", 10000)
print(emp.__sal)

