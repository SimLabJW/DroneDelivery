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
        self.insert_state("DATAIN",1)

        self.insert_input_port("start")

        self.insert_output_port("random")

 
    def ext_trans(self, port, msg):
        if port == "start":
            self._cur_state = "Generate"


    def output(self):
        if self._cur_state == "Generate":
            self.raw_data = self.conn.http_receive('http://192.168.50.75:13158/unity/receive')
    
            # data recv code
            if self.raw_data :
                print(f"Received data: {self.raw_data}")
                self._curstate = "DATAIN" 


        if self._cur_state == "DATAIN":

            send_data = self.Modify_devcie_info(self.raw_data)
            msg = SysMessage(self.get_name(), "random")
            msg.insert(send_data)
            return msg


    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "DATAIN"
        elif self._cur_state == "DATAIN":
            self._cur_state = "Wait"
        elif self._cur_state == "Wait":
            self._cur_state = "Wait"


    def Modify_devcie_info(self, data):
        """
        device info classify
        """
        unity_recv = []

        if isinstance(data, dict):
            # data가 딕셔너리인 경우
            unity_recv.append({
                "id": data['id'],
                "home": data['home'],
                "store": data['store'],
                "state": data['state']
            })
        elif isinstance(data, list):
            # data가 리스트인 경우
            for data_index in data:
                unity_recv.append({
                    "id": data_index['id'],
                    "home": data_index['home'],
                    "store": data_index['store'],
                    "state": data_index['state']
                })
        else:
            print("Unsupported data format")

        return unity_recv