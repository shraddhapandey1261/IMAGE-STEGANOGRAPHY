from Stegno import Stegno
from PIL import Image

img = Image.open(r'C:\Users\SHRADDHA PANDEY\Desktop\IMAGE_STEGANOGRAPHY\3791x2494.jpeg').convert('L')
x = Stegno(img)
x.encode(img)
x.decode()