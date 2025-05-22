from netmiko import Netmiko

# List of devices in the topology
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Commands to configure a Loopback interface
loopback_config = [
    "interface Loopback0",
    "ip address 10.0.0.1 255.255.255.0",
    "description Configured by Netmiko"
]

# Loop through each device and apply the configuration
for device in devices:
    print(f"\n>>> Connecting to {device['ip']}")
    net_connect = Netmiko(**device)

    output = net_connect.send_config_set(loopback_config)
    print(output)
    verify_output = net_connect.send_command("show ip interface brief")
    print(verify_output)

    net_connect.disconnect()

