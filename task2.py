from jinja2 import Environment, FileSystemLoader

# Set up the environment
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task2.j2")

# Define the class
class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# Create the interface object (uplink set to False)
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10, uplink=True)

# Render and print the configuration
print(template.render(interface=interface_obj))

