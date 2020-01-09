class calc1:
    def sum(self, a, b):
        print(a+b)

class calc2:
    def mult(self,a,b):
        print(a*b)

class multipleCalc(calc1, calc2):
    def divide(self, a, b):
        print(a/b)

mcal = multipleCalc()
mcal.sum(2,3)
mcal.mult(2,3)
mcal.divide(2,3)