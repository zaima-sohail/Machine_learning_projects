print(".........................Calculator..................")
number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
operator=input("select the operator: +,-,*,%,/")
if operator=="+":
       def add(number1,number2):
        return number1+number2
       result=add(number1,number2)
       print("the result of two numbers are:",result)

elif operator=="-":

    def subtract(number1,number2):
      return number1-number2
    result=subtract(number1,number2)
    print("the result of two numbers are:",result)
elif operator=="*":
    def multiply(number1,number2):
      return number1*number2
    result=multiply(number1,number2)
    print("the result of two numbers are:",result)
elif operator=="%":
    def modulus(number1,number2):
     return number1%number2
    result=modulus(number1,number2)
    print("the result of two numbers are:",result)
elif operator=="/":
    def division(number1,number2):
     return number1/number2
    result=division(number1,number2)
    print("the result of two numbers are:",result)
else:
   print("incorrect statement ! Try again")