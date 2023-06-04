from django.utils.deprecation import MiddlewareMixin


class ModificationMiddleware(MiddlewareMixin):

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        # Code that is executed in each request before the view is called
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        ...

    def process_response(self, request, response):
        # This code is executed just after the view is called
        return response

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        return exception

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response
