from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
import random

class SelectDevice(BehaviorModelExecutor):
    # def __init__(self, instance_time, destruct_time, name, engine_name, conn):
    #     BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name, conn)
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        # self.conn = conn
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate",1)
        self.insert_state("ReGenerate",1)

        self.insert_input_port("start")

 
    def ext_trans(self, port, msg):
        if port == "start":
            self.random_data = msg.retrieve()[0]
            self._cur_state = "Generate"

    def output(self):
        if self._cur_state == "Generate":
            print("In SelectDevice")
            
            print(f"S 선택된 숫자: {self.random_data[0]}, {self.random_data[1]}")
            # self.conn.send(self.count, self.conn.time(), self.jsone_nane)


    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Wait"



    