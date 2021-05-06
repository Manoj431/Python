#Write a program to throw exception with your own message

m = ("Jala Tech")

try:
    print(int(m))
except ValueError:
    print(f"Value Error: {m} is str type. ")