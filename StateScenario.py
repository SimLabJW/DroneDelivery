import random

class DeviceInfo:
    STATE = {
        "STAY": 40, 
        "DELIVERY": 50, 
        "ACCIDENT": 5, 
        "CANCEL": 5
    }

class StateScenario:
    def __init__(self):
        self.current_state = None  # 현재 상태를 저장하기 위한 변수
        self.functions = {
            "STAY": self.Stay_State,
            "DELIVERY": self.Delivery_State,
            "ACCIDENT": self.Accident_State,
            "CANCEL": self.Cancel_State
        }
        self.transition_count = 0

    def Stay_State(self):
        print("Stay State Executed")
        self.transition_state(["STAY", "DELIVERY", "ACCIDENT"])

    def Delivery_State(self):
        print("Delivery State Executed")
        self.transition_state(["DELIVERY", "CANCEL", "ACCIDENT"])

    def Accident_State(self, acc_device=None, stay_device=None):
        print(f"Accident State Executed for {acc_device}")
        # 고장난 기기에 대한 정보를 stay 상태인 드론에게 전달
        stay_device = "example_stay_device"
        print(f"Transferring data to {stay_device}")
        # 상태 전이 없이 ACCIDENT 상태 유지
        self.transition_count += 1

    def Cancel_State(self, cancel_device=None):
        print("Cancel State Executed")
        self.transition_state(["STAY"])

    def Remote_State(self):
        print("Remote State Executed")
        # 모든 기능 정지 로직 구현 필요
        self.current_state = None

    def transition_state(self, possible_states):
        if self.transition_count >= 20:
            print("Maximum transition count reached.")
            self.current_state = None
            return

        states = possible_states
        weights = [DeviceInfo.STATE[state] for state in states]
        selected_state = random.choices(states, weights)[0]
        self.current_state = selected_state
        
        # 해당 함수에 필요한 인자가 있을 경우, 적절히 전달해야 합니다.
        if selected_state == "ACCIDENT":
            self.functions[selected_state](acc_device="example_acc_device")
        elif selected_state == "CANCEL":
            self.functions[selected_state](cancel_device="example_cancel_device")
        else:
            self.functions[selected_state]()

    def execute_random_state(self):
        if self.current_state is None:
            states = list(DeviceInfo.STATE.keys())
            weights = list(DeviceInfo.STATE.values())
            selected_state = random.choices(states, weights)[0]
            self.current_state = selected_state

        while self.current_state and self.transition_count < 20:
            func = self.functions[self.current_state]
            func()

# 사용 예시
scenario = StateScenario()
scenario.execute_random_state()
