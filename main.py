class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def Gt (self , New):
        if 0 < New <= self.floors:
            for f in range(1, New+1):
                print(f)
        else:
                print("Floor is not defined")
    def __len__ (self):
        return self.floors
    def __str__(self):
        return (f"Название: {self.name}, количество этажей: {self.floors}")


h1 = House('Doctrine', 10)
h2 = House('Laclord', 11)
h1.Gt(5)
h2.Gt(12)
print('------')
#str
print(h1)
print(h2)
print('------')
#len
print(int(len(h1)))
print(int(len(h2)))