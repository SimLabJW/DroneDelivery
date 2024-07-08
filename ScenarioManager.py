from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite

from .CommunicationSet.TCP import Communication
from SelectDevice import RecvDevice
from RandomGenerator import RandomGenerator

class ScenarioManager():
    def __init__(self) -> None:
        self.communication = Communication()
        self.Register_Engine()

    def Register_Engine(self):
        self.send = SystemSimulator()
        self.send.register_engine("Scenario", "VIRTUAL_TIME", 1)
        self.send_model = self.send.get_engine("Scenario")

        self.Insert_Port()

    def Insert_Port(self):
        self.send_model.insert_input_port("start")

        self.RecvDevice_m = RecvDevice(0, Infinite, "RecvDevice_m", "Scenario", self.communication) # recv data(device data)
        self.RandomGenerator_m = RandomGenerator(0, Infinite, "RandomGenerator_m", "Scenario", self.communication) # send data(update device data => random data)

        self.Register_Entity()

    def Register_Entity(self):
        self.send_model.register_entity(self.RecvDevice_m)
        self.send_model.register_entity(self.RandomGenerator_m)

        self.Copuling_Relation()

    def Copuling_Relation(self):
        self.send_model.coupling_relation(None, "start", self.RecvDevice_m, "start")
        self.send_model.coupling_relation(self.RecvDevice_m, "random", self.RandomGenerator_m, "start")
        self.send_model.coupling_relation(self.RandomGenerator_m, "done", self.RecvDevice_m, "start")

        self.start()


    def start(self):

        self.send_model.insert_external_event("start", "start")
        self.send_model.simulate()



ScenarioManager()