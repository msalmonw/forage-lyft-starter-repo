from datetime import datetime

from engine.engines import Engines

from tires.tire_types import Tires

class Car_Models():
    class Calliope(Engines.CapuletEngine, Tires.CarriganTires):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False
    
    class Glissade(Engines.WilloughbyEngine, Tires.OctoprimeTires):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False
    
    class Palindrome(Engines.SternmanEngine, Tires.CarriganTires):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False

    class Rorschach(Engines.WilloughbyEngine, Tires.CarriganTires):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False

    class Thovex(Engines.CapuletEngine, Tires.OctoprimeTires):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False


