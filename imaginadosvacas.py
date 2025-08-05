from PIL import Image 
import pytesseract 

woof = 600

with Image.open("betin.jpg") as img:
    og_bark, og_woof = img.size

    #reducir tamaño, solo para obtener color, no se usará más esa variable
    if (og_woof > 600):
        bark = (og_bark * woof) // og_woof
        imgresize=img.resize((bark, woof))
    
    #obtener color más usado
    imgforcolor = imgresize.quantize(colors=256).convert("RGB")
    colors = imgforcolor.getcolors()
    obtenercolor = sorted(colors, reverse=True)
    obtenercolor = obtenercolor[0][1]

    #escala de grises solo para tesseract
    imgris=img.convert("L")


    #img.show()
    #print (obtenercolor)






