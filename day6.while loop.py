# while loop(no pre defined limits
#print numbers from 1to5
'''
c = 1
while c<=5:
    print(c)
    c+=1'''

#secret number >> raj=7
#veer =?
#1-10
'''
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("enter any number from 1 to 10:"))
    if guess == secret_number:
        print("congratulations! you guessed it right")
        break

    elif guess < secret_number:
        print("your guess is too low")

    elif guess >secret_number:
        print("your guess is too high")

    else:
        print("invalid input")'''

#print sum of n numbers
'''
x = int(input("enter any number:"))

i = 1
sum =0
while i <=x:
    sum = sum +i
    i +=1
print("sum of n numbers is:",sum)'''

#factorial numbers @imp
'''
n = int(input("enter any number:"))
sum=1
i = 1
while i<=n:
    sum = sum *i
    i+=1
print("factorial",sum)'''

#calculator

x = int(input("enter first number:"))
y = int(input("enter second number:"))
ch = input("enter any operator(+,-,*,/,%):")

if ch == "+":
    print(x+y)
elif ch == "-":
    print(x-y)
elif ch == "*":
    print(x*y)
elif ch == "/":
    print(x/y)
elif ch == "%":
    print(x%y)
else:
    print("select a valid operator")
