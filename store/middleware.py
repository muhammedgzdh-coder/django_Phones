import time


class RequestTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.perf_counter()

        response = self.get_response(request)

        end_time = time.perf_counter()

        duration = end_time - start_time

        print(f"{request.path} -> {duration:.2f} seconds")

        return response