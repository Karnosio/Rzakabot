import os
import time

from PIL import Image, ImageFont
from pilmoji import Pilmoji
from pilmoji.source import AppleEmojiSource

from utils.database import get_caption


def check_caption(caption: str) -> str:
    if caption is None:
        return get_caption()
    else:
        return caption


def resize_font(string):
    font_size = 35
    if len(string) <= 15:
        font_size = 50
    elif len(string) <= 25:
        font_size = 35
    return font_size


def make_image(file_name: str, text: str = None) -> str:
    if Image.open(f'image/{file_name}'):
        im = Image.open(f'image/{file_name}').convert('RGB')
        fon = Image.open('image/fon.jpg').convert('RGB')

        new_image = im.resize((608, 567))
        fon.paste(new_image, (55, 33))
        if text is not None:
            strings = text.split('\n')
            if len(strings) <= 2:
                if len(strings) == 1:
                    font_size = 35
                    if len(strings[0]) <= 10:
                        font_size = 100
                    elif len(strings[0]) <= 20:
                        font_size = 50
                    font = ImageFont.truetype('times.ttf', font_size, encoding='unic')
                    pilmoji = Pilmoji(fon, source=AppleEmojiSource)
                    w, h = pilmoji.getsize(text=text, font=font)
                    w, h = ((714 - w) / 2, 595 + (150 / 2 - h / 2))
                    pilmoji.text((int(w), int(h)), strings[0], (255, 255, 255), font=font)
                else:
                    max_len = len(max(strings, key=len))

                    strings = [
                        [
                            strings[0].center(max_len),
                            ImageFont.truetype('times.ttf', resize_font(strings[0]), encoding='unic')
                        ],
                        [
                            strings[1].center(max_len),
                            ImageFont.truetype('times.ttf', resize_font(strings[1]), encoding='unic')
                        ]
                    ]

                    pilmoji = Pilmoji(fon, source=AppleEmojiSource)
                    pad = 50
                    for string in strings:
                        w, h = pilmoji.getsize(text=string[0], font=string[1])
                        W, H = ((714 - w) / 2, 595 + (pad - (h / 2)))
                        pilmoji.text((int(W), int(H)), string[0], (255, 255, 255), font=string[1])
                        pad += 50
            else:
                return 'image/error.jpg'
        fon.save('image/' + 'resize' + file_name + '.jpg')

        fon.close()
        im.close()
        os.remove(os.path.join(os.getcwd(), f'image/{file_name}'))
        return 'image/' + 'resize' + file_name + '.jpg'
    else:
        time.sleep(0.1)
        make_image(file_name)
