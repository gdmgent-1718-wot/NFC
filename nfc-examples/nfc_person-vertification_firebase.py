# NFC Persons Verification via Firebase
# Developed by Philippe De Pauw - Waterschoot

# Mifare Namespaces
import nxppy


import logging
import time
from datetime import timezone
import sys, pygame

# Firebase Namespaces
import firebase_admin
from firebase_admin import credentials

# Create
firebase_credentials = credentials.Certificate('../../keys/ahs-cms-firebase-adminsdk-eob2s-4d3bff0472.json')
firebase_app = firebase_admin.initialize_app(firebase_credentials)
