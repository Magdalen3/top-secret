from PIL import Image 
import pytesseract
import os

img = None
for betin in os.listdir():
    if betin.endswith(('.jpg', '.png', '.jpeg')):
        img = Image.open(betin) 
        break

#reducir tamaño, solo para obtener color, no se usará más esa variable
og_bark, og_woof = img.size
woof = 600
if (og_woof > 600):
    bark = (og_bark * woof) // og_woof
    imgresize=img.resize((bark, woof))
else:
    imgresize = img
#obtener color más usado
imgforcolor = imgresize.quantize(colors=256).convert("RGB")
colors = imgforcolor.getcolors()
obtenercolor = sorted(colors, reverse=True)
obtenercolor = obtenercolor[0][1]

#escala de grises solo para tesseract
imgris=img.convert("L")


img.show()
#print (obtenercolor)






