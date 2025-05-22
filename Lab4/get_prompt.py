from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22
    }
]

for device in devices:
    print(f"\nConnecting to {device['ip']}...")
    try:
        net_connect = Netmiko(**device)
        print(f"Default prompt: {net_connect.find_prompt()}")
        net_connect.send_command_timing("disable")
        print(f"After 'disable': {net_connect.find_prompt()}")
        net_connect.enable()
        print(f"After 'enable': {net_connect.find_prompt()}")
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

