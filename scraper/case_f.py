from captcha.image import ImageCaptcha
import random
import string
import os


def generate_captcha():
    image = ImageCaptcha(width=240, height=80)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    captcha_path = os.path.join('static', 'captcha.png')
    image.write(captcha_text, captcha_path)
    return captcha_text


