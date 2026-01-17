print("stmt-1")
try:
#     print(10/0) 
    print(int("Apple"))
except ZeroDivisionError:
    print("Are you perhaps 2 year old? 😮‍💨")
except ValueError:
    print("Are you sure you know what you are doing? 😡")
finally:
    print('Do Better! 😔')

class TooYoungException(Exception):
    def __init__(self, msg, *args):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self, msg, *args):
        self.msg = msg

a = int(input("Enter any number: "))
try:
    if a>18:
        print("Welcome to the dating app!")
    else: 
        raise TooYoungException("Too young, don't go to Roblox!")
except TooYoungException:
    print("PLEASE DON'T GO TO ROBLOX!!!✋🙏")