from jinja2 import Environment, FileSystemLoader

# Set up the Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task3.j2")

# Define a class (though here we're using only one object with repeated values)
class NetworkInterface(object):
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Create one interface object (used for all 10 interfaces in the loop)
interface_obj = NetworkInterface("Server Port", 10)

# Render the template
print(template.render(interface=interface_obj))

