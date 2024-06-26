a = int (input ("enter the number :"))
b= int (input ("enter the another number :"))


def add(a,b):
    print (a+b)
def subtract(a,b):
    print (a-b)
def divide(a,b):
    print (a/b)
def multiply(a,b):
    print (a*b)

add(a,b)
subtract(a,b)
divide(a,b)
multiply(a,b)



#  creation of replictions
n = int(input ("enter the number of operations:"))
count =0
while count < n:
    
    a=(input("enter the number"))
    b=eval(a)
    print (b)
    count += 1