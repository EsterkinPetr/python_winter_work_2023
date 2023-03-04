class Fibonacci:
    def __init__(self):
        self.fibo = []
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <= 1:
            self.chfibo = 1
        else:
            self.chfibo = self.fibo[self.i - 2] + self.fibo[self.i - 1]
        self.fibo.append(self.chfibo)
        self.i += 1
        return self.chfibo
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))