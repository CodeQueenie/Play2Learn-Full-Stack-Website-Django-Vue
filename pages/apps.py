from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

from django.apps import AppConfig

class GamesConfig(AppConfig):
    name = 'games'
