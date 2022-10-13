#VERSION:.1.0.1
#AUTHOR: Marshall Burns a.k.a Schooly b

###IMPORTING THE 'PYGRCODE' MODULE###
###IMPORTING THE 'PNG' MODULE###
###IMPORTING THE 'QRCODE' FUNCTION FROM THE 'PYQRCODE MODULE'###

import pyqrcode 
import png 
from pyqrcode import QRCode

###DECLARING THE _GEN() FUNCTION###
def _Gen():
    website = 'https://google.com'
    url = pyqrcode.create(website)
    url.png('Images/exampleQR.png', scale=5)

###CALLING THE _GEN() FUNCTION###
_Gen()
