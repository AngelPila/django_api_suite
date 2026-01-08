from datetime import datetime

from firebase_admin import db
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LandingAPI(APIView):
	name = "Landing API"
	collection_name = "landing"
