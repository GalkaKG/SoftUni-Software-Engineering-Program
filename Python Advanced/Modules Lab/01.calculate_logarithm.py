from math import log

number = int(input())
base = input()

result = log(number) if base == 'natural' else log(number, int(base))
print(result)
