class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(self.name, self.number_of_floors)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("такого этажа не сушествует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House("ЖК Эльбрус", 30 )

h2 = House("April", 9)

h1.go_to(5)
h2.go_to(10)