

class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        self.needService = engine.needService
    
    def needSerive(engine, battery):
        return engine.needService and battery.needService
    