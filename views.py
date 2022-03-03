from jinja2 import Environment, FileSystemLoader
import os


class View:
    def __init__(self):
        return None

    def render(self, template_name, **kwargs):
        env = Environment(loader=FileSystemLoader(os.getcwd() + "/templates"))
        template = env.get_template(template_name)
        return template.render(**kwargs)
