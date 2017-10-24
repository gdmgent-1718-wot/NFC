import nxppy
import logging
import time

logging.basicConfig()
mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        print("Detected NFC Tag UID: %r" %uid)

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)

