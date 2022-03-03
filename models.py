import yaml


class Model:
    def __init__(self):
        self.title = "Для данного представления не создана модель"
        self.body = "Progressively strategize user friendly process improvements via revolutionary interfaces. Conveniently disseminate premium functionalities vis-a-vis user friendly niches. Distinctively re-engineer real-time information rather than seamless alignments. Proactively provide access to interactive potentialities after."

    def getmodel(self, name):
        try:
            with open('models/' + name + '.yaml') as yl:
                data = yaml.safe_load(yl)
                self.title = data[0].get("title")
                self.body = data[0].get("body")
                return self
        except FileNotFoundError:
            return self



