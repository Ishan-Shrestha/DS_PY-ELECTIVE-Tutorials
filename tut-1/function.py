# # function

# def iseven(num):
#     """
#     Function for detecting even numbers
#     """
#     if num%2 ==0:
#         return True
#     else:
#         return False

# x = int(input("Enter your number: "))
# check = iseven(x)
# print(check)

# def gimmesum(num1, num2):
#     return num1+num2

# sum1,sum2 = gimmesum(10,10), gimmesum(20+20)

# # types of arguments

# # positional
# def show(a, b):
#     print("The value of a is", a)
#     print("The value of b is", b)

# gimme = gimmesum(11, 12)

# #  keyword
# def show(a, b):
#     print("The value of a is", a)
#     print("The value of b is", b)

# gimme = show(b=11, a=12)
# gimme2 = show(10, a=20)
# # gimme3 = show(a=10, 10) -- error 

# #  note: positional argument can't come after keyword argument

# # default

# def starve(a = 10, b =11):
#     print("The value of a is", a)
#     print("The value of b is", b)

# showme = starve(15)

#  variable length argument 

# def wow(*args): #tuple
#     for num in args:
#         print(num)

# print(wow(10))
# print(wow(10,20,30,40,50,60))

# def wow2(**kwargs): #dictionary
#     for k, v in kwargs.items():
#         print(f"The value is key is {k} and the value of value is {v}.")

# print(wow2(a= 10,b= 20,c =30,d= 40,e= 50,f= 60))

# # Types of functions

# # anonymous functions:

# # normal functions:

# # lambda function:
# square = lambda a: a*a
# print(square(2))

# filter(function, sequence), map(function, sequence) and reduce(function, sequence)
li = [0,5,10,15,20,25,30]

# l1 = list(filter(lambda num:num%2==0, li))
# # even list
# print(l1)
# l2 = list(filter(lambda num:num%2!=0, li))
# # even list
# print(l2)

sli = tuple(map(lambda x:x*x, li))
print(sli)

from functools import reduce
total_product = reduce(lambda x, y: x * y, li)
print(total_product)