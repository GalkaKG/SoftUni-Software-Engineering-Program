items = input()
dwarfs = {}
colors = {}
while items != "Once upon a time":
    tokens = items.split(" <:> ")
    name = tokens[0]
    color = tokens[1]
    physics = int(tokens[2])
    id = name + ":" + color
    if id not in dwarfs:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        dwarfs[id] = [0, color]
    dwarfs[id][0] = max([dwarfs[id][0], physics])
    items = input()

sorted_dwrafs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
for key, value in sorted_dwrafs.items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")
