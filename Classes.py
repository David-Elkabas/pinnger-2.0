class Machine:
    def __init__(self, hostname, ip, who_am_i, last_send_time, is_working):
        self.ip = ip
        self.hostname = hostname
        self.who_am_i = who_am_i
        self.last_send_time = last_send_time
        self.is_working = is_working


class Takash:
    def __init__(self, name):
        self.machine_list=[]
        self.name = name

    def add_machine(self,Machine):
        self.machine_list.append(Machine)






