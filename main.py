from remote_control import RemoteControl

remote_control = RemoteControl()

print("""
TV Application

1. Turn On TV

2. Turn Off TV

3. Volume Settings

4. Add Channel

5. Get Number of Channels

6. Switch to a Random Channel

7. TV Information

Press 'q' to exit.
""")

while True:
    operation = input("Select an operation: ")

    if operation == "q" or operation == "Q":
        print("Exiting...")
        break
    elif operation == "1":
        remote_control.turn_on_tv()
    elif operation == "2":
        remote_control.turn_off_tv()
    elif operation == "3":
        if remote_control.tv_status == "On":
            remote_control.volume_settings()
        else:
            print("TV is off, please turn on the TV first!")
    elif operation == "4":
        if remote_control.tv_status == "On":
            channel_names = input("Enter channel names separated by ',' : ")
            channel_list = channel_names.split(",")
            for to_add in channel_list:
                remote_control.add_channel(to_add)
        else:
            print("TV is off, please turn on the TV first!")
    elif operation == "5":
        if remote_control.tv_status == "On":
            print("Number of channels: ", len(remote_control))
        else:
            print("TV is off, please turn on the TV first!")
    elif operation == "6":
        if remote_control.tv_status == "On":
            remote_control.random_channel()
        else:
            print("TV is off, please turn on the TV first!")
    elif operation == "7":
        print(remote_control)
    else:
        print("Invalid Operation!")
