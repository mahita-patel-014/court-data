# captcha/generate.py
import random
import string

def generate_captcha():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=6))
