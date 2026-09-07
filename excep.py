try:
    num=int(input("enter the number:"))
    print(10/num)
except ZeroDivisionError:
    print("you are trying to divide by zero!")
except ValueError:
    print("invalid value enter")
except Exception as e:
    print(f"an excepted error occur:{e}")
