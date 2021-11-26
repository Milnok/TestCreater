from django.apps import AppConfig


class BaseFrameworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_framework'
