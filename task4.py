from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task4.j2")

# Interface data class
class NetworkInterface(object):
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Create the data object to be passed to the template
interface_obj = NetworkInterface("Server Port", 10)

# Render and print the output
print(template.render(interface=interface_obj))

