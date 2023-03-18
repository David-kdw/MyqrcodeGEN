!pip install pyqrcode

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 

txt = input('Bonjour! Cet outil vous permet de générer un code QR pour le contenu de votre choix. Veuillez entrer votre texte : ')
  
# Generate QR code 

code = pyqrcode.create(txt) 

# Create and save the png file naming "myqr.png" 

code.svg("kdwqrcode.svg", scale = 8, module_color='brown', background='0xFFFFFF')