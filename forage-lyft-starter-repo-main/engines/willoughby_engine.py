

from Engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.needService = self.engine_should_be_serviced()

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
