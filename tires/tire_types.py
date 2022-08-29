from abc import ABC

from car import Car


class Tires():
    class CarriganTires(Car, ABC):
        def __init__(self, tire_wear):
            super().__init__(tire_wear)

        def tire_should_be_serviced(self):
            return(all(x >= 0.9 for x in tire_wear))
    
    class OctoprimeTires(Car, ABC):
        def __init__(self, tire_wear):
            super().__init__(tire_wear)

        def tire_should_be_serviced(self):
            return sum(tire_wear) if sum(tire_wear) > 3 else 0