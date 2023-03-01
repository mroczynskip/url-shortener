import random
import string

from core.settings import GENERATED_URL_LENGTH


def generate_short_url():
    return "".join(random.choices(string.ascii_letters + string.digits, k=GENERATED_URL_LENGTH))
