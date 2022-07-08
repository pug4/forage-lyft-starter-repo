from datetime import datetime

from battery import Battery


class SplindlerBattery(Battery):
    def __init__(self, last_service):
        self.last_service_date = last_service
        self.current_date = datetime.today().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < self.current_date