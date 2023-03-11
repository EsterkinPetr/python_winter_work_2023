class Gener:

    def __init__(self):
        self.x = -1
        self.s = []
        self.let = []
        for i in range(ord('A'), ord('Z') + 1):
            self.let.append(chr(i))
        for i in range(1, 27):
            self.s.append(i)
            self.s.append(self.let[i - 1])

    def __iter__(self):
        return self

    def __next__(self):
        y = self.s[self.x - len(self.s) + 1]
        if self.x <= 50:
            self.x += 1
        else:
            self.x = -1
        return y

a = Gener()
for i in range(106):
    print(next(a), end=',')





