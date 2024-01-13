import random
import time

class RemoteControl():

    def __init__(self, tv_status="Off", tv_volume=0, channel_list=["Trt"], channel="Trt"):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def turn_on_tv(self):
        if self.tv_status == "On":
            print("The TV is already on...")
        else:
            print("Turning on the TV...")
            time.sleep(1)
            self.tv_status = "On"
            print("TV is now on.")

    def turn_off_tv(self):
        if self.tv_status == "Off":
            print("The TV is already off...")
        else:
            print("Turning off the TV...")
            self.tv_status = "Off"
            time.sleep(1)
            print("TV is now off.")

    def volume_settings(self):
        while True:
            response = input("Decrease volume: '<'\nIncrease volume: '>'\nExit: 'q'\n")

            if response == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("Volume:", self.tv_volume)
                else:
                    print("Volume:", self.tv_volume)
            elif response == ">":
                if self.tv_volume != 31:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)
                else:
                    print("Volume:", self.tv_volume)
            elif response == "q" or response == "Q":
                print("Volume updated: ", self.tv_volume)
                break
            else:
                print("Invalid operation!")

    def add_channel(self, channel_name):
        print("Adding channel...")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("{} added to the channel list".format(channel_name))

    def random_channel(self):
        random_index = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[random_index]
        print("Current channel: ", self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "TV status: {}\nTV volume: {}\nChannel List: {}\nCurrent channel: {}\n".format(
            self.tv_status, self.tv_volume, self.channel_list, self.channel
        )
