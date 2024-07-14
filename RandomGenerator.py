from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
import DeviceInfo
import random

class RandomGenerator(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, conn):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.conn = conn
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate", 1)

        self.insert_input_port("start")
        self.insert_output_port("done")

    def ext_trans(self, port, msg):
        if port == "start":
            self.data_msg = msg.retrieve()[0]
            print(f"recv : {self.data_msg } ")
            self._cur_state = "Generate"

    def output(self):
        if self._cur_state == "Generate":
       
            random_data = self.data_msg

            for rd in random_data:
                if rd['state'] == "None":
                    rd['state'] = "STAY"
                else:
                    self.transition_state(rd)

            print(f"send : {random_data} ")
            self.conn.http_send('http://192.168.50.75:17148/client/send', random_data)
            msg = SysMessage(self.get_name(), "done")
            return msg

    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Wait"

    def transition_state(self, device):

        current_state = device['state']
        if current_state not in DeviceInfo.TRANSITIONS:
            return

        possible_states = list(DeviceInfo.TRANSITIONS[current_state].keys())
        weights = list(DeviceInfo.TRANSITIONS[current_state].values())
        selected_state = random.choices(possible_states, weights)[0]

        if current_state == "ACCIDENT":
            device['state'] = "ACCIDENT"
            return  # ACCIDENT 상태에서 다른 상태로 전환 불가

        if current_state == "DELIVERY":
            if selected_state == "ACCIDENT":
                self.handle_accident_state(device)
            elif selected_state == "CANCEL":
                device['state'] = 'STAY'
                device['home'] = 0
                device['store'] = 0
            else:
                device['state'] = "DELIVERY"  # 유지
                return  # 상태 유지, 변경하지 않음
            
        elif current_state == "STAY":
            if selected_state == "DELIVERY":
                if device['home'] == 0 and device['store'] == 0:
                    numbers = random.sample(range(1, 67), 2)
                    device['home'] = numbers[0]
                    device['store'] = numbers[1]

                    device['state'] = "DELIVERY"


    def handle_accident_state(self, accident_device):
        stay_devices = [d for d in self.data_msg if d['state'] == 'STAY']
        if stay_devices:
            stay_device = random.choice(stay_devices)
            stay_device['home'] = accident_device['home']
            stay_device['store'] = accident_device['store']
            stay_device['state'] = 'DELIVERY'
