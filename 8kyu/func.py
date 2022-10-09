'''

def greetings(name,age):
    print('Welcome '+name+ '. You are '+age+ ' years old')

greetings('John','21')


def greeting(*names):
    print('Welcome ', names[2])

greeting('John','Sam', 'Emma')   


def greetings(name,age):
    print('Welcome '+name+ '. You are '+age+ ' years old')
name = input('Enter your name: ')
age = input('Enter your age: ')

greetings(name,age)


def addnumbers(num1,num2):
    return num1 +num2

print(addnumbers(2,3))


def addnumbers(num1,num2):
    return num1 +num2

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

print(addnumbers(num1, num2))


a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
if a < b:
    print(a,' is lesser than ',b)
elif a is b:
    print('They are the same')
else:
    print(a,' is greater than ',b)


a = int(input('Enter a number: '))

if a%2 == 0:
    print(a,' is divisible by 2')

else:
    print(a, ' is not divisible by 2')


num = int(input('Enter a number: '))

if num%2 ==0:
    print('Even number')

else:
    print('Odd number')


Working with dictionaries

mydict = {
    'name':'Sam',
    'age': '21',
    'nationality':'Ghananian',
    'alive': True,
    'friends':['Emma','Caleb', 'Kwadwo']
}

print(type(mydict['friends']))



i = -3
while i <= 5:
    print(i)
    i+=1

working with FOR loops
for letter in  'Hello':
    print(letter)


my_list =['jo','so','go']
for x in my_list:
    print(x)
    if x == 'so':
        break


my_list =['jo','so','go']
for x in my_list:
    if x == 'so':
        break
    print(x)



for x in range(4):
    print(x)


for x in range(1,7):
    print(x)
else:
    print('FInished  looping')



my_list =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11],]

for x in my_list:
    for row in x:
        print(row)
print(my_list[0][1])



num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
op = input('Enter your operator: ')

if op == '+':
    print('The addition of both numbers are',num1+num2)

if op == '-':
    print('The subtraction of both numbers are',num1-num2)

if op == '*':
    print('The multiple of both numbers are',num1*num2)

if op == '/':
    print('The division of both numbers are',int(num1/num2))

else:
    print('The operator is invalid. \nUse +, -, /, *')

Working with TRY EXCEPT
try:
    x =int(input('Enter an integer: '))
    print(x)
except:
    print('Something went wrong, \nPlease try again....')

try:
    x =int(input('Enter an integer: '))
    print(x)
except ValueError:
    print('Value not an integer')
finally:
    print('Finished')
'''
import time
print('Create an Account now')

username = input('Enter a username: ')
password = input('Enter a password: ')

print(username, ' successfully created ')
print('Login now')

username1 = input('Enter your username: ')
password1 = input('Enter your password: ')

while True:
    if username == username1 and password == password1:
        print('You are successfully logged in as ',username)

    elif username !=username1 or password !=password1:
        print("Invalid credentials")
        time.sleep(2)