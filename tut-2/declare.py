def wish(name):
    if name == 'Ram':
        print(f"Welcome Back, {name}!")
    else:
        print(f"{name} isn't registered in the directory!")
    
def welcome():
    if __name__ == "__main__":
        print('This is direct execution!')
    else:
        print('This is indirect execution!')

welcome()