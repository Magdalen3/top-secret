from PIL import Image 
import pytesseract 

woof = 600

with Image.open("betin.jpg") as img:
    og_bark, og_woof = img.size
    if (og_woof > 600):
        bark = (og_bark * woof) // og_woof
        img=img.resize((bark, woof))
    #img.show()
    img = img.quantize(colors=256)  
    colors = img.getcolors(maxcolors=256)
    img.show()
    #print (colors)






