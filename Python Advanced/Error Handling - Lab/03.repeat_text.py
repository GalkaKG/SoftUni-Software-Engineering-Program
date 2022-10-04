text = input()

try:
    num = int(input())
    print(text * num)
except ValueError:
    print("Variable times must be an integer")
