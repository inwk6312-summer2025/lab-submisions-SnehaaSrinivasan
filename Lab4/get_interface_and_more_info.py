from netmiko import ConnectHandler

# Define each router
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",  # R1
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}
r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",  # R2
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}
r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",  # R3
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Commands to run on each device
show_commands = [
    "show interface description",
    "show ip interface brief",
    "show version",
    "show cdp neighbors",
    "show running-config | include hostname",
    "show interfaces"
]

# Loop through each router and execute commands
for device in (r1, r2, r3):
    try:
        print(f"\nConnecting to {device['ip']}...\n")
        net_connect = ConnectHandler(**device)

        for command in show_commands:
            print(f"\n--- {command.upper()} on {device['ip']} ---")
            output = net_connect.send_command(command)
            print(output)
            print("-" * 100)

        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

