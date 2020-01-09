def except_1():
    try:
        list=[1,2,3,4]
        print(list[4])
        print(a)
        a = 10
        print(a/0)
    except NameError:
        print("Name Error exception occured")
    except IndexError:
        print("Invalid Index provided")
    # except ZeroDivisionError:
    #     print("Exception has occured due to zero division")
    except Exception:
        print ("Common Exception")
    else:
        print("No Exception at all")
    finally:
        # print("This is the Finally block. Gets executed irrespective of any error or errorless code")
        print("Able to call this function successfully")
        #
        # a = 10
        # print(a/0)

except_1()
