def checkZero(number):
    try:
        if number == 0:
            print("Number is Zero")
        elif number > 0:
            print("Number is Positive")
        elif number < 0:
        # else:
            print("Number is Negative")
    except TypeError:
        print("Invalid type provided")
    finally:
        try:
            print("The number", int(number), "checking is done")
        except:
            print("Exception in Finally block")
checkZero("a")