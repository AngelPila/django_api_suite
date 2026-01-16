from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
from django.conf import settings
from pathlib import Path

class LandingApiConfig(AppConfig):
    name = "landing_api"

    def ready(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                Path(settings.BASE_DIR) / "secrets" / "landing-18da4-firebase-adminsdk-fbsvc-f0694a2f05.json"
            )
            firebase_admin.initialize_app(cred, {
                "databaseURL": settings.FIREBASE_DATABASE_URL
            })