from controllers import RequestController, PageControllerAbout


class Wsgi:
    def __call__(self, environ, start_response):
        # Page Controller
        if environ["PATH_INFO"] == "/about":
            page_about = PageControllerAbout(start_response)
            response = page_about.about()
        # Front Controller
        else:
            front_controller = RequestController()
            response = front_controller.dispatch(environ, start_response)

        return [bytes(str(response), encoding='utf-8')]
