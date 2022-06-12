people = int(input())
all_people = people
wagons = input().split()
max_places = 4
sum_places = sum([int(num) for num in wagons])
empty_places = len(wagons) * max_places - sum_places

for i in range(len(wagons)):
    if int(wagons[i]) < 4 and people >= 4:
        people -= max_places - int(wagons[i])
        wagons[i] = str(max_places)
    elif int(wagons[i]) < 4 and people < 4:
        wagons[i] = str(int(wagons[i]) + people)
        people = 0
        break


if people == 0 and empty_places > all_people:
    print("The lift has empty spots!")
    print(" ".join(wagons))
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(wagons))
elif empty_places == all_people and people == 0:
    print(" ".join(wagons))
