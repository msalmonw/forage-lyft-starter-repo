import unittest
from datetime import datetime

from engine.model.car_models import Car_Models


class TestCar(unittest.TestCase):

    def __init__(self, Car_Input):
        self.Car_Model = Car_Input

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = self.Car_Model(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = self.Car_Model(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = self.Car_Model(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = self.Car_Model(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):

        car = self.Car_Model(tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):

        car = self.Car_Model(tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main(Car_Models.Calliope)
