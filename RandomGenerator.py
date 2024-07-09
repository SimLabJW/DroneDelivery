from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
import DeviceInfo
import random

class RandomGenerator(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, conn):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.conn = conn
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate",1)

        self.insert_input_port("start")
        self.insert_output_port("done")

 
    def ext_trans(self, port, msg):
        if port == "start":
            self.data_msg = msg.retrieve()[0]
            self._cur_state = "Generate"

    def output(self):
        if self._cur_state == "Generate":

            random_data = self.data_msg

            for rd in random_data:
                if rd['state'] == "None":
                    rd['state'] = "STAY"
                else:
                    self.transition_state(rd)

            # for rd in random_data:
            #     self.transition_state(rd)
            self.conn.http_send('http://192.168.50.75:13158/client/send', random_data)

            # print(f"random data2 {random_data}")
            # # 요기서 메시지 전달받은 다음 규식이형한테 전달
            msg = SysMessage(self.get_name(), "done")
            return msg


    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Wait"

    def transition_state(self, device):
        current_state = device['state']
        if current_state not in DeviceInfo.TRANSITIONS:
            print(f"Unknown state: {current_state}")
            return

        possible_states = list(DeviceInfo.TRANSITIONS[current_state].keys())
        weights = list(DeviceInfo.TRANSITIONS[current_state].values())
        selected_state = random.choices(possible_states, weights)[0]

        if current_state == "ACCIDENT":
            print(f"Device {device['id']} remains in {selected_state} state.")
            return  # ACCIDENT 상태에서 다른 상태로 전환 불가

        if current_state == "DELIVERY" and selected_state == "DELIVERY":
            print(f"Device {device['id']} remains in DELIVERY state.")
        else:
            print(f"Device {device['id']} transitioning \
                  from {current_state} to {selected_state}")
            device['state'] = selected_state

            if selected_state == "DELIVERY":
                numbers = random.sample(range(1, 67), 2)
                device['home'] = numbers[0]
                device['store'] = numbers[1]
                print(f"Device {device['id']} updated with \
                      home: {device['home']} and store: {device['store']}")
                
            elif selected_state == "ACCIDENT":
                self.handle_accident_state(device)
            elif selected_state == "CANCEL":
                device['state'] = 'STAY'
                device['home'] = 0
                device['store'] = 0
                print(f"Device {device['id']} state set to STAY with home: 0 and store: 0")

    def handle_accident_state(self, accident_device):
        stay_devices = [d for d in self.devices if d['state'] == 'STAY']
        if stay_devices:
            stay_device = random.choice(stay_devices)
            stay_device['home'] = accident_device['home']
            stay_device['store'] = accident_device['store']
            stay_device['state'] = 'DELIVERY'
            print(f"Device {stay_device['id']} updated with home: {stay_device['home']} \
                  and store: {stay_device['store']} due to accident of device {accident_device['id']}")