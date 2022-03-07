import yaml


class Route:
    def __init__(self):
        self.routes = {}
        self.titles = {}
        with open('data.yaml', encoding="utf-8") as yl:
            data = yaml.safe_load(yl)
            for route in data:
                self.routes[route['slug']] = route['model']
                self.titles[route['slug']] = route['title']
