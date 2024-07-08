from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
import random

class RandomGenerator(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)


        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate",1)

        self.insert_input_port("start")
        self.insert_output_port("done")

 
    def ext_trans(self, port, msg):
        if port == "start":
            self._cur_state = "Generate"

    def output(self):
        if self._cur_state == "Generate":
            print("In RandorGenrator")
            numbers = random.sample(range(1, 67), 2)

            num1 = numbers[0]
            num2 = numbers[1]
            print(f"선택된 숫자: {num1}, {num2}")

            # 요기서 메시지 전달받은 다음 규식이형한테 전달
            msg = SysMessage([num1, num2], "done")
            return msg


    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Wait"



    