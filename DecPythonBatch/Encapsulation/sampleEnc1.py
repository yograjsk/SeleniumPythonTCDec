class Employee:
    def __init__(self, name, sal):
        self._name = name
        self.sal = sal
        self.__age = 50

    def getAge(self):
        return self.__age

    def setAge(self, newAgeValue):
        if newAgeValue <= 60:
            self.__age = newAgeValue

    def empInfo(self):
        print(self._name)
        print(self.sal)
        print(self.__age)

emp = Employee("Bill", 10000)
emp.empInfo()
emp.setAge(60)
emp.empInfo()

# class HR(Employee):
#     pass

# hr = HR("John", 50000)
# print(hr.sal)
# print(hr._name)
# print(hr.__age)