file_path = './numbers.txt'

file = open(file_path, 'r')
print(sum([int(x.strip()) for x in file]))
