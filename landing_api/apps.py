from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
from django.conf import settings
import os

class LandingApiConfig(AppConfig):
    name = 'landing_api'

    def ready(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                os.path.join(settings.BASE_DIR, "firebase_key.json")
            )

            firebase_admin.initialize_app(cred, {
                "databaseURL": settings.FIREBASE_DATABASE_URL
            })
