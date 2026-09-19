from django.apps import AppConfig


class ResultConfig(AppConfig):
    name = 'store'
    label = 'result'

    def ready(self):
        import store.signals