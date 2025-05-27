from jinja2 import Environment, FileSystemLoader

# Define the interface data as a dictionary
interface_data = {
    "name": "GigabitEthernet0/1",
    "description": "Server Port",
    "vlan": 10
}

# Load the Jinja2 environment and template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')

# Render the template with the interface data
output = template.render(interface=interface_data)

# Print the final configuration
print(output)

