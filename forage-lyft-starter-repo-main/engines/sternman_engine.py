from Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
        self.needService = self.engine_should_be_serviced()

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
