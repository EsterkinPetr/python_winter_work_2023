class Person:
    def __init__(self):
        self.fam = input("ведите фамилию:")
        self.im = input("ведите имя:")
        self.ot = input("Введите отчество:")

    def __str__(self):
        self.fio = self.fam + self.im + self.ot
        self.spfio = list(self.fio)
        self.rspfio = reversed(self.spfio)
        return ''.join(self.rspfio)

p = Person()
print(p)

