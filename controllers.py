from routes import Route
from views import View
from models import Model

status = '200 OK'
headers = [('Content-Type', 'text/html')]


# Front Controller
class RequestController:
    def __init__(self):
        self.status = status
        self.headers = headers
        self.routes = Route()
        self.views = View()
        self.model = Model()

    def dispatch(self, env, start_response):
        current_path = env["PATH_INFO"]
        if current_path in self.routes.routes:
            # page in routes
            for path, handler in self.routes.routes.items():
                if path == current_path:
                    start_response(self.status, self.headers)
                    page = self.model.getmodel(handler)
                    return self.views.render('page.html', nav=self.routes.titles, title=page.title, body=page.body)
        else:
            # page 404
            page = self.model.getmodel('404')
            start_response(self.status, self.headers)
            return self.views.render('page.html', nav=self.routes.titles, title=page.title, body=page.body)


# Page Controller
class PageControllerAbout:
    def __init__(self, start_response):
        self.status = status
        self.headers = headers
        self.views = View()
        self.routes = Route()
        start_response(self.status, self.headers)
        return None

    def about(self):
        model = Model()
        about = model.getmodel('about')
        return self.views.render('about.html', nav=self.routes.titles, title=about.title, body=about.body)
