from calculate import calculate

first, operator, second = input().split()

print(calculate(float(first), float(second), operator))
