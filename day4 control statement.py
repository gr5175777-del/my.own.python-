# control statements:
'''
a = 10
if(a>5):
    print(" a is a natural number:")
print("program end")'''

'''
age = int(input("enter your age:"))
if age>18:
    print("eligible for vote")
else:
    print("not eligible to vote")
print("program end")'''


'''
x= int(input("enter marks:"))
if x<10:
    print("your fail")
else:
    print("pass")'''

#even >> 2,4,6,8,10 x%2 ==0
#odd >> 1,3,5,7,9
'''
x = int(input("enter your number:"))
if x%2==0:
    print("even number")
else:
    print("odd number")'''

'''
months = input("enter your month:")
if months==28:
    print("feb")
else:
    print("march")'''

'''a = 5
b = 6
d = 2
if (a>b and a>d):
    print("a is the big one")
elif(b>a and b>d):
    print("b is big one")
else:
    print("d is a big one")'''

#login page
username = input("enter username:")
password = input("enter password:")
user = "raj"
pas = "raj1435"
if (username==user and password==pas):
    print("login succesful")
elif (username!=user and password==pas):
    print("invalid username")
elif (username==user and password!=pas):
    print("invalid password")
else:
    print("invalid details")