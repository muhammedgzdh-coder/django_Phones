from django.apps import AppConfig


class ResultConfig(AppConfig):
    name = 'store'

    def ready(self):
        import store.signals