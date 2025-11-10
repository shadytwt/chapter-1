print("Hello, user!")
name = input("What is your name?\n")
age = int(input("What is your age?\n"))


print("It is good to meet you,", name.title())
print("The length of your name is:")
print(len(name.replace(" ", "")))  
print(f"You will be {age + 1} in a year.")
