class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.number:
            raise StopIteration
        symbol = self.sequence[self.pointer % len(self.sequence)]
        self.pointer += 1
        return symbol
    
