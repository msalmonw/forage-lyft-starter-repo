from datetime import datetime

from engine.engines import Engines

class Car_Models():
    class Calliope(Engines.CapuletEngine):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False
    
    class Glissade(Engines.WilloughbyEngine):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False
    
    class Palindrome(Engines.SternmanEngine):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False

    class Rorschach(Engines.WilloughbyEngine):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False

    class Thovex(Engines.CapuletEngine):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False


