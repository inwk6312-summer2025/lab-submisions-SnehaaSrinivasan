from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # R1
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # R2
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # R3 (added)
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]

for device in devices:
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_command("show version")
        net_connect.disconnect()

        # Extract uptime
        uptime_index = output.find('uptime is')
        if uptime_index != -1:
            uptime = output[uptime_index:uptime_index + 38]
        else:
            uptime = "Uptime not found"

        # Extract Configuration Register
        config_register = "Not found"
        for line in output.splitlines():
            if "Configuration register is" in line:
                config_register = line.strip()
                break

        # Print both results
        print(f"{device['ip']} => {uptime}")
        print(f"{device['ip']} => {config_register}\n")

    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

