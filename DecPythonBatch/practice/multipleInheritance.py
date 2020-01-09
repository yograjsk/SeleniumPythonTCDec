class Calculation1:
    def summation(self,a,b):
        print("summation result is:",str(a+b))
        return a+b

class Calculation2:
    def multiplication(self,a,b):
        print("multiplication result is:",str(a+b))
        return a*b

class Derived(Calculation2, Calculation1):
    def division(self, b, a):
        print("another division",str(b/a))
        return a / b

cal = Derived()
print(cal.summation(5,10))
print(cal.multiplication(5,10))
print(cal.division(100,5))
