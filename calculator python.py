def add(x,y):
    return x + y;
def subtract(x,y):
    return x - y;
def multiply(x,y):
    return x * y;
def divide(x,y):
    return x / y;
def power(x,y):
    return x ** y;
def remainder(x,y):
    return x % y;

while True:
    print("Select operation.")
    print("Add      : + ")
    print("Subtract : - ")
    print("Multiply : * ")
    print("Divide   : / ")
    print("Power    : ^ ")
    print("Remainder: % ")
    print("Reset    : $ ")
    print("Terminate: # ")
    
    operation = input("Enter Operation : ")
    if operation in ('+' '-' '*' '/' '^' '%' '#' '$'):
        if operation == '$':
            continue
        if operation == '#':
            break
        
        num1 = int(input("Enter First Number = "))
        num2 = int(input("Enter 2nd Number = "))
    
        if operation == '+':
            print(num1, "+", num2, "=", add(num1,num2))
        elif operation == '-':
            print(num1, "-", num2, "=", subtract(num1,num2))
        elif operation == '*':
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif operation == '/':
            print(num1, "/", num2, "=", divide(num1,num2))
        elif operation == '^':
            print(num1, "^", num2, "=", power(num1,num2))    
        elif operation == '%':
            print(num1, "%", num2, "=", remainder(num1,num2))
    else:
     print("invalid input")
 
   

        
