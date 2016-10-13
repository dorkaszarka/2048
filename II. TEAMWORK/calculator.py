operators = ["+","-","/","*"]
def add(a, b):
    return a + b
def subt(a, b):
    return a - b
def dev(a, b):
    if a == 0 or b == 0:
       print("Do not count with zero")
    else:
        return a / b
def mult(a, b):
    return a * b

alive = True
while alive:
    firstnumber = input("Enter a number (or a letter to exit:)")
    if firstnumber.isdigit():
        operation = input("Enter an operation:")
        if operation in operators:
            secondnumber = input("Enter another number:")
            if secondnumber.isdigit():
                firstnumber = int(firstnumber)
                secondnumber = int(secondnumber)
                if operation == '+':
                    print(add(firstnumber, secondnumber))
                elif operation == '-':
                    print(subt(firstnumber, secondnumber))
                elif operation == '*':
                    print(mult(firstnumber, secondnumber))
                elif operation == '/':
                    print(dev(firstnumber, secondnumber))
            else:
                alive = False
    else:
        alive = False
 
   


