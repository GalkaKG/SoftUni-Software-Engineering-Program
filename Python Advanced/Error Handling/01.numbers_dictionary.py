numbers_dict = {}

while True:
    num_as_string = input()
    if num_as_string == "Search":
        break
    try:
        num = int(input())
        numbers_dict[num_as_string] = num
    except ValueError:
        print("The variable number must be an integer")

while True:
    searched = input()
    if searched == "Remove":
        break
    try:
        print(numbers_dict[searched])
    except KeyError:
        print("Number does not exist in dictionary")

while True:
    searched = input()
    if searched == "End":
        break
    try:
        del numbers_dict[searched]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dict)
