"""
Contains the configuration class for the app.
Used to specify app-specific configurations and settings.
"""

from django.apps import AppConfig


class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'
