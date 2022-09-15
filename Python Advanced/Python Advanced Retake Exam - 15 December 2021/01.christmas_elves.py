from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

toys = 0
used_energy = 0
time = 0

while elfs_energy and materials:

    if elfs_energy[0] < 5:
        elfs_energy.popleft()
        continue
    if not elfs_energy:
        break

    elf = elfs_energy.popleft()
    box = materials.pop()

    time += 1

    toys_to_be_created = 1
    energy_to_be_spent = box
    energy_increase_factory = 1

    if time % 3 == 0:
        toys_to_be_created = 2
        energy_to_be_spent *= 2
    if time % 5 == 0:
        toys_to_be_created = 0
        energy_increase_factory = 0

    if energy_to_be_spent <= elf:
        toys += toys_to_be_created
        used_energy += energy_to_be_spent
        elfs_energy.append(elf - energy_to_be_spent + energy_increase_factory)
    else:
        materials.append(box)
        elfs_energy.append(elf * 2)


print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
