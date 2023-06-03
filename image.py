from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
import base64
from rembg import remove
from youtubesearchpython import VideosSearch
import json
import subprocess


def create(text) -> Image:
    art = Image.new("RGBA", (512, 512))
    draw = ImageDraw.Draw(art)
    fnt = ImageFont.truetype("fonts/Holimount.otf", 180)
    w, h = draw.textsize(text, font=fnt)
    draw.text(((512-w)/2, (512-h)/2), text,
              font=fnt, fill=(255, 255, 255, 255))
    print(os.listdir("fonts"))
    art.save("images/sign.png", "png", lossless=True)
    return "ok"


def sticker(text) -> Image:
    art = Image.new("RGBA", (512, 512))
    draw = ImageDraw.Draw(art)
    fnt = ImageFont.truetype("fonts/Holimount.otf", 180)
    w, h = draw.textsize(text, font=fnt)
    draw.text(((512-w)/2, (512-h)/2), text,
              font=fnt, fill=(255, 255, 255, 255))
    print(os.listdir("fonts"))
    art.save("images/sign.png", "png", lossless=True)
    return "ok"


def no_bg(image) -> Image:
    art = Image.open(BytesIO(base64.b64decode(image)))
    nobg = remove(art)
    nobg.save("images/nobg.png", "PNG")
    return "ok"


def music(title):
    videosSearch = VideosSearch(title, limit=1)
    link = videosSearch.result()["result"][0]["link"]
    filename = subprocess.check_output(f'yt-dlp {link} -f ba --print filename -o music/output.%(ext)s')
    filename = filename.decode("utf-8").strip()
    os.system(f"yt-dlp {link} -f ba -o music/output.%(ext)s")
    os.system(f"ffmpeg -y -i {filename} -b:a 128k -c:a libopus music/output.opus")
    os.system(f"del {filename}")
    return "ok"

music("prathihari")