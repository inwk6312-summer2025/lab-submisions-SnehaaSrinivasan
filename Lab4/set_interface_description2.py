from netmiko import Netmiko
import logging

# Optional: enable logging if you want to debug
# logging.basicConfig(filename='netmiko_log.txt', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")

# List of routers
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # R1
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # R2
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # R3
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Loop through each router
for device in devices:
    print(f"\n--- Connecting to {device['ip']} ---")
    net_connect = Netmiko(**device)

    # Apply changes from file
    output = net_connect.send_config_from_file('changes.txt')
    print("Configuration Output:")
    print(output)

    # Verify the change
    verify = net_connect.send_command("show interface description")
    print("Interface Description After Change:")
    print(verify)

    # Disconnect
    net_connect.disconnect()
    print(f"--- Disconnected from {device['ip']} ---\n")

