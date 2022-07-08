from datetime import datetime
from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service):
        super().__init__()
        self.last_service_date = last_service
        self.current_date = datetime.today().date()
        self.needs_service = self.needs_service()
        
    def needs_service(self):
        return self.last_service_date.year - self.current_date.year