from abc import abstractmethod, ABC


class Bank(ABC):
    @abstractmethod
    def getROI(self):
        pass

    @abstractmethod
    def getName(self):
        pass
        # print("bank name is Parent Bank")
        # return "Parent Bank"
        # print("dfdsaf")


class SBI(Bank):
    def getROI(self):
        print("Rate of Interest is 8")
        return 8

    def getName(self):
        print("bank name is SBI Bank")
        return "SBI Bank"


class ICICI(Bank):
    def getROI(self):
        print("Rate of Interest is 9")
        return 9

    def getName(self):
        # pass
        print("bank name is ICICI Bank")
        return "ICICI Bank"

# b1 = Bank()
b2 = SBI()
b3 = ICICI()

# print("Base Rate of Interest:", b1.getName())
# print("Base Rate of Interest:", b1.getROI())
print("SBI Rate of Interest:", b2.getROI())
print("ICICI Rate of Interest:", b3.getROI())

print(b2.getName())
print(b3.getName())
