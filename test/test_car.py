import unittest
from datetime import date
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from car import Car

class TestCar(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(mileage=35000)
        battery = SpindlerBattery(last_service_date=date(2020, 1, 1), current_date=date(2022, 1, 1))
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_willoughby_engine_needs_service(self):
        engine = WilloughbyEngine(mileage=65000)
        battery = SpindlerBattery(last_service_date=date(2020, 1, 1), current_date=date(2022, 1, 1))
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(warning_light_on=True)
        battery = SpindlerBattery(last_service_date=date(2020, 1, 1), current_date=date(2022, 1, 1))
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_spindler_battery_needs_service(self):
        engine = CapuletEngine(mileage=25000)
        battery = SpindlerBattery(last_service_date=date(2020, 1, 1), current_date=date(2023, 1, 1))
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_nubbin_battery_needs_service(self):
        engine = CapuletEngine(mileage=25000)
        battery = NubbinBattery(last_service_date=date(2020, 1, 1), current_date=date(2024, 1, 1))
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()
