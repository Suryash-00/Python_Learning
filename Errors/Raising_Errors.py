class Car:
    def __init__(self, make, model):
        self.make=make
        self.model=model

    def __repr__(self):
        return f"Car {self.make} {self.model}"

class Garage:
    def __init__(self):
        self.cars=[]
    
    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        # raise NotImplementedError("We can't add cars to the Garage yet")
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but only object of 'Car' can be added")
        self.cars.append(car)

ford=Garage()
#ford.add_car('Fiesta')
car= Car('Ford', 'Fiesta')
ford.add_car(car)
print(len(ford))

'''
def count_from_zero_to_n(n):
    if n>=0:
        for x in range(0, n+1):
            print(x)
    else:
        raise ValueError("Invalid argument entered")
'''