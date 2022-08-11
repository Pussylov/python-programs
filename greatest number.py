num1 = int(input("enter number1 : "))  
num2 = int(input("enter number2 : "))  
num3 = int(input("enter number3 : "))  
num4 = int(input("enter number4 : ")) 
if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is greater") 
if(num2>num1 and num2>num3 and num2>num4):
    print("num 2 is greater")
if(num3>num1 and num3>num2 and num3>num4):
    print("num 3 is greater")
if(num4>num1 and num4>num3 and num4>num1):
    print("num 4 is greater")
if(num1==num2==num3==num4):
    print("entered numbers are equal")
else:
    print("it is not equal")
