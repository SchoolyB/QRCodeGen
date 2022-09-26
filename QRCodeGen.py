# Version 1.0.0

import pyqrcode  # Importing the pyqrcode module
import png  # Importing png module allowing user to save file as a png
from pyqrcode import QRCode

# Decclare the function


def website():
    website = 'https://google.com'
    url = pyqrcode.create(website)
    url.png('Images/exampleQR.png', scale=5)

# Calling the function
website()
