from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
import DeviceInfo
import random

class RecvDevice(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, conn):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.conn = conn
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate",1)

        self.insert_input_port("start")

        self.insert_output_port("random")

 
    def ext_trans(self, port, msg):
        if port == "start":
            self._cur_state = "Generate"


    def output(self):
        if self._cur_state == "Generate":
            print("In SelectDevice")
            # self.raw_data = self.conn.recv(4096).decode("utf-8")

            # 요기서 데이터를 수신 받고 출력하도록하는 코드를 작성하는 구조
            # 서버로부터 데이터를 수신
            self.raw_data = self.conn.http_receive('http://192.168.50.75:13158/unity/receive')
            print(f"Received data: {self.raw_data}")

            # data recv code
            if self.raw_data :
                # self.Modify_devcie_info(self.raw_data)
                self._curstate = "Generate" 


        if self._cur_state == "Generate":
            msg = SysMessage([self.raw_data], "random")
            return msg


    def int_trans(self):
        if self._cur_state == "Wait":
            self._cur_state = "Wait"
        elif self._cur_state == "Generate":
            self._cur_state = "Wait"


    def Modify_devcie_info(self, data):
        """
        device info classify
        """
        print("Modifying device info with data: ", data)
