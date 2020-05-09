from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print('its running')
class Programmer:
    def work(self,com):
        print('solving bug')
        com.process()
#comp=Computer()
lp=Laptop()
#lp.process()

pg=Programmer()
pg.work(lp)