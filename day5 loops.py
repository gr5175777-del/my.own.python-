#loops : for loop,while loop
'''
for i in range(1,10):
    print(i)'''

'''
for i in range(2,11,2): #even number
    print(i)'''
'''
for i in range(1,11,2):  #odd number

    print(i)'''

#check prime or not
'''
num = int(input("enter a number:"))
if num <=1:
    print("not a prime number")
else:
    for i in range(2,num):
        if num%i == 0:
            print("not a prime number")
            break
    else:
            print("the number is a prime number")'''

#to print list of prime numbers
'''
z = int(input("enter a number:"))
for z in range(2,z):
    for i in range(2,z):
        if z%i ==0:
            break
    else:
        print(z)'''

#print 2 table
'''
for i in range(1,11):
    print("2x",i,"=",2*i)'''

#print sum of n numbers
'''
n = int(input("enter a number:"))
sum = 0
for i in range(1,n+1):
    sum = sum +i
print("sum=", sum)'''

#print factorial of a number

n = int(input("enter a  number:"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("factorial=",fact)
