from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment and load the template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")

# Define a class to represent a network interface
class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# Create an instance of the class
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)

# Render the template with the class object
print(template.render(interface=interface_obj))

