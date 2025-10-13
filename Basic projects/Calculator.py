num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
arithmatic= input("Enter arithmetic operation(+,-,*,/): ")
if arithmatic == "+":
    print('The sum of two number is',num1 + num2)
elif arithmatic == '-':
    print('The min of two number is',num1-num2)
elif arithmatic == '*':
    print('The mul of two number is',num1*num2)
elif arithmatic == '/':
    if num2 != 0:
        print('The div of two number is',num1/num2)
    else:
        print('The division cannot be zero')
