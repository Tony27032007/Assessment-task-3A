
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore
from firebase_admin import *
cred = credentials.Certificate("/Users/rmit/Documents/Assessment-task-3A/cinema-5819f-firebase-adminsdk-fbsvc-0cd3e60dbc.json")
firebase = firebase_admin.initialize_app(cred, {'projectId': 'cinema-5819f'})
import requests
FIREBASE_API_KEY = "AIzaSyDOFgG6I2VIBc3LeJfUt7AyOd2SHaPHRO4"
db = firestore.client()