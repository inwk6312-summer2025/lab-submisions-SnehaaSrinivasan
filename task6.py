from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment to load templates from the current directory
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task6.j2")

# List of dictionaries representing interfaces
interfaces = [
    {
        "name": "GigabitEthernet0/1",
        "desc": "uplink port",
        "uplink": True
    },
    {
        "name": "GigabitEthernet0/2",
        "desc": "Server port number one",
        "vlan": 10
    },
    {
        "name": "GigabitEthernet0/3",
        "desc": "Server port number two",
        "vlan": 10
    }
]

# Render the template with the interface list
print(template.render(interface_list=interfaces))

