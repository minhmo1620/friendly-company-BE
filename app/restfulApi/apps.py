from django.apps import AppConfig
from .load_heavy_data import load_model

class RestfulapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restfulApi'
    def ready(self):
        load_model()
