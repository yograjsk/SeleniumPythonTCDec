class Employee:
    def __init__(self, name, sal):
        self._name = name
        self.sal = sal
        self.__age = 50

    def empInfo(self):
        print(self._name)
        print(self.sal)
        print(self.__age)

emp = Employee("Bill", 10000)
emp.empInfo()
print(emp._name)
print(emp.sal)
print(emp.__age)

class HR(Employee):
    pass

hr = HR("John", 50000)
print(hr.sal)
print(hr._name)
print(hr.__age)
