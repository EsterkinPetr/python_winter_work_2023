def dis(self):
    print(self.x)


Par = type('Par', (), {'dis': dis, 'x':'Значение'})
p = Par()
p.dis()
