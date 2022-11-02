class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.i = len(obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            current = self.obj[self.i]
            self.i -= 1
            return current
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
