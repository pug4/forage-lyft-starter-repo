from model.car import Car
from batteries.battery import NubbinBattery
from batteries.battery import SplindlerBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


def createCalliopeCar(last_service_date, current_mileage: int, last_service_mileage: int):
    return Car(engine=CapuletEngine(current_mileage, last_service_mileage), battery=SplindlerBattery(last_service_date))

def create_glissade(last_service_date, current_mileage: int, last_service_mileage: int):
    return Car(engine=WilloughbyEngine(current_mileage, last_service_mileage), battery=SplindlerBattery(last_service_date))

def create_palindrome(last_service_date, warning_light_on: bool):
    return Car(engine=SternmanEngine(warning_light_on), battery=SplindlerBattery(last_service_date))

def create_rorschach(last_service_date, current_mileage: int, last_service_mileage: int):
    return Car(engine=WilloughbyEngine(current_mileage, last_service_mileage),battery=NubbinBattery(last_service_date))

def create_thovex(last_service_date, current_mileage: int, last_service_mileage: int):
    return Car(engine=CapuletEngine(current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date))