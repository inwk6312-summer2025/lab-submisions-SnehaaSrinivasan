from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123"}
]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface brief")
    print(f"--- Interfaces on {device['ip']} ---")
    print(output)
    net_connect.disconnect()

