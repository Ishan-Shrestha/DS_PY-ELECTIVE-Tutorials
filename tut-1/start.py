# # RESERVED KEYWORDS
# from keyword import kwlist
# print(kwlist)

# # BOOL PROPERTY
# print(True+True)

# # DOCSTRING
# a = """a"""
# print(a)

# # FUNCTION
# def hello():
#     """
#     This function prints hello world
#     """
#     print("Hello World!")

# # help(hello)

# # eval function
# val = eval(input("Enter your value:"))
# print(val)


# #  flow control

# # conditional
# def genderCode():
#     male, female = 1,0
#     gender = int(input("ENTER YOUR GENDER CODE: "))
#     gender = "male" if gender == male else "female"  #if else
#     print(gender)
# genderCode()

# transfer statement
li = [1,11,111,1111,11111]

for x in li:
    if x == 1111:
        break
    print(x)

for x in li:
    if x == 1111:
        continue
    print(x)
else:
    print("This is else block of for loop.")
