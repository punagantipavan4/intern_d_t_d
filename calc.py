# here i am creating calculator script with python 
# functions using for operations
def add(a,b):
#"addition:returns of two numbers"
  return a+b
def sub(a,b):
#"subratcation: return of two numbers"
  return a-b
def mul(a,b):
# "muliplication: return of two numbers"
  return a*b
def divide(a,b):
  #"divide:return quiotent of two numbers"
  if b==0:
   raise ZeroDivisionError("Division by zero is not allowed")
  return a/b

# main program operations
while True:
  print("\n1.add(+)")
  print("2.sub(-)")
  print("3.mul(*)")
  print("4.divide(/)")
  print("5.Exit")

  choice=input("enter your number from (1-5):")
  
  if choice == "5":
    print("Exiting calculator")
    break
  
  #expextion handling  works on the operation 
  try:
    num1=float(input("enter your first number: "))
    num2=float(input("enter your second number: "))
    
    # perform the selection operator
    if choice =="1":
      result=add(num1,num2)
      operator="+"
    elif choice=="2":
      result=sub(num1,num2)
      operator="-"
    elif choice=="3":
      result=mul(num1,num2)
      operator="*"
    elif choice=="4":
      result=divide(num1,num2)
      operator="/"
    else:
      print("Invalid choice,please enter 1to 5.")
      continue
    
    print(f"\nResult: {num1} {operator} {num2} = {result}")
  except ZeroDivisionError as e:
    print(e)
# here used i covered functions, operators, loops, user input, conditionals, exception handling, and edge cases.

