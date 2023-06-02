from PIL import Image,ImageDraw,ImageFont
import os

def create(text)->Image:
    art = Image.new("RGBA",(512,512))
    draw = ImageDraw.Draw(art)
    fnt = ImageFont.truetype("fonts/Holimount.otf", 90)
    w, h = draw.textsize("Sudeepa Virajitha",font=fnt)
    draw.text(((512-w)/2,(512-h)/2), "Sudeepa Virajitha",font=fnt, fill=(255, 255, 255, 255))
    print(os.listdir("fonts"))
    art.save("images/sign.webp","WEBP")
    return "ok"