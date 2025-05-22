from netmiko import Netmiko

# List of devices in the topology
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]

# Loop through each router
for device in devices:
    print(f"\n====== Device: {device['ip']} ======\n")
    net_connect = Netmiko(**device)

    # ✅ Question 1: Show IP Interface Brief with TextFSM
    output1 = net_connect.send_command("show ip interface brief", use_textfsm=True)
    print(f"--- Interfaces on {device['ip']} ---")
    for interface in output1:
        print(f"Interface: {interface.get('interface', 'N/A')}, IP: {interface.get('ip_address', 'N/A')}")

    # ✅ Question 2: View available TextFSM templates (manually done in Linux VM or GitHub folder)
    # You can explore: /home/student/ntc-templates/templates/cisco_ios_show_ip_interface_brief.textfsm

    # ✅ Question 3: Parse "show ip route" and extract protocol, network, distance, metric
    output2 = net_connect.send_command("show ip route", use_textfsm=True)
    print(f"\n--- IP Routing Table for {device['ip']} ---")
    for route in output2:
        print(f"Protocol: {route.get('protocol', 'N/A')}, "
              f"Network: {route.get('network', 'N/A')}, "
              f"AD/Metric: {route.get('distance_metric', 'N/A')}")

    net_connect.disconnect()

