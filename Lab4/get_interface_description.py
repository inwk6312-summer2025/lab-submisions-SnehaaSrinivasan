from netmiko import ConnectHandler

# Define each router in the topology
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

# Loop through all devices
for device in (r1, r2, r3):
    try:
        print(f"\nConnecting to {device['ip']}...\n")
        net_connect = ConnectHandler(**device)

        # Command 1: Interface Descriptions
        print(f"--- Interface Descriptions on {device['ip']} ---")
        output = net_connect.send_command("show interface description")
        print(output)

        # Command 2: Optional - Any other command you want
        print(f"\n--- IP Interface Brief on {device['ip']} ---")
        brief_output = net_connect.send_command("show ip interface brief")
        print(brief_output)

        net_connect.disconnect()
        print("-" * 100)

    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

