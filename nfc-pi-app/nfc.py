"""
==============================================
NFC
==============================================
Course:     Web Of Things (WOT)
Option:     New Media Development
Department: Graphic and Digital Media
College:    Artevelde University College Ghent
----------------------------------------------
Authors:
    - Philippe De Pauw - Waterschoot
----------------------------------------------
Resources:
    - https://www.element14.com/community/community/raspberry-pi/blog/2017/07/10/sense-hat-color-chooser
    - https://firebase.google.com/docs/admin/setup
==============================================
"""

# Standard Python imports
import logging
import time

# Mifare imports
import nxppy

# Firebase imports
import firebase_admin
from firebase_admin import credentials as fb_credentials
from firebase_admin import db as fb_db

# Mifare setup
mifare = nxppy.Mifare()

# Add firebase authentication credentials
fb_cred = fb_credentials.Certificate('../../../settings/nmd-cms-37ed0a5f6bfc.json')
fb_db_app = firebase_admin.initialize_app(fb_cred,{'databaseURL':'https://nmd-cms.firebaseio.com'})

# Define root of the firebase database
fb_db_root = fb_db.reference()

# Navigate to the right object
checkins_ref = fb_db_root.child('checkins')
if(checkins_ref.get() == None):
    checkins_ref.set({})

# Thread
while True:
    try:
        uid = mifare.select()
        print("Detected NFC Tag UID: %r" %uid)
        
        # Check the latest state of uid in firebase database
        checkins_snapshot = checkins_ref.order_by_child('mifare_uid').equal_to(uid).limit_to_last(1).get()
        checked_in = True
        if(checkins_snapshot == None):
            checked_in = True
        else:
            # o = checkins_snapshot[checkins_snapshot.keys()[0]]
            prev_checked_in = (list(checkins_snapshot.items())[0][1]['checkedin'])
            checked_in = not prev_checked_in
            
        checkin_obj = {
            'mifare_uid': uid,
            'timestamp': round(time.time()*1000),
            'checkedin': checked_in
        }
        new_checkins_ref = checkins_ref.push()
        new_checkins_ref.set(checkin_obj)

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)