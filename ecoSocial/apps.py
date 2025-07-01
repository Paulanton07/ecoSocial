from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "ecoSocial"

    def ready(self):
        import_module("ecoSocial.receivers")
