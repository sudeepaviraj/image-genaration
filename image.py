from PIL import Image,ImageDraw,ImageFont
import os
from io import BytesIO
import base64
from rembg import remove

def create(text)->Image:
    art = Image.new("RGBA",(512,512))
    draw = ImageDraw.Draw(art)
    fnt = ImageFont.truetype("fonts/Holimount.otf", 180)
    w, h = draw.textsize(text,font=fnt)
    draw.text(((512-w)/2,(512-h)/2), text,font=fnt, fill=(255, 255, 255, 255))
    print(os.listdir("fonts"))
    art.save("images/sign.png","png",lossless=True)
    return "ok"

def sticker(text)->Image:
    art = Image.new("RGBA",(512,512))
    draw = ImageDraw.Draw(art)
    fnt = ImageFont.truetype("fonts/Holimount.otf", 180)
    w, h = draw.textsize(text,font=fnt)
    draw.text(((512-w)/2,(512-h)/2), text,font=fnt, fill=(255, 255, 255, 255))
    print(os.listdir("fonts"))
    art.save("images/sign.png","png",lossless=True)
    return "ok"

def no_bg(image)->Image:
    art = Image.open(BytesIO(base64.b64decode(image)))
    nobg = remove(art)
    nobg.save("images/nobg.png","PNG")
    return "ok"