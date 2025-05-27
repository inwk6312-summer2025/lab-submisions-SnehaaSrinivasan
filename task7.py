from jinja2 import Environment, FileSystemLoader
import yaml

# Set up Jinja2 to load templates from the current directory
ENV = Environment(loader=FileSystemLoader('.'))

# Load the template (same as Task 6)
template = ENV.get_template("template-task6.j2")

# Load the YAML file
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)

# Render and print configuration
print(template.render(interface_list=interfaces))

