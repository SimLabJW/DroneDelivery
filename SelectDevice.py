from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
import DeviceInfo
import random

class RecvDevice(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, conn):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name, conn)

        self.conn = conn.conn
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate",1)

        self.insert_input_port("start")

        self.insert_output_port("random")

 
    def ext_trans(self, port, msg):
        if port == "start":
            self._cur_state = "Wait"


    def output(self):
        if self._cur_state == "Wait":
            print("In SelectDevice")
            self.raw_data = self.conn.recv(4096).decode("utf-8")

            # data recv code
            if self.raw_data :
                self.Modify_devcie_info(self.raw_data)
                self._curstate = "Generate" 


        if self._cur_state == "Generate":
            msg = SysMessage([self.raw_data], "random")
            return msg


    def int_trans(self):
        if self._cur_state == "Wait":
            self._cur_state = "Wait"
        elif self._cur_state == "Generate":
            self._cur_state = "Wait"


    def Modify_devcie_info(self, Data):
        """
        device info classify
        """

