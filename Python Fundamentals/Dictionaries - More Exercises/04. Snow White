dwarfs = {}
hat_colours = {}

while True:
	input_line = input()
	if input_line == 'Once upon a time':
		break
		
	name, colour, physics = input_line.split(' <:> ')
	key = (name, colour)
	value = int(physics)
	
	if key in dwarfs:
		dwarfs[key] = max(value, dwarfs.get(key))
	else:
		dwarfs[key] = value
		
		if not colour in hat_colours:
			hat_colours[colour] = 0
		hat_colours[colour] += 1
		
sorted_dwarfes = sorted(dwarfs.items(), key= lambda item: (item[1], hat_colours[item[0][1]]), reverse= True)
for dwarf in sorted_dwarfes:
	print(f'({dwarf[0][1]}) {dwarf[0][0]} <-> {dwarf[1]}')
