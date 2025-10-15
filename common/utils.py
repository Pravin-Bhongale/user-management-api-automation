import random, string


def random_username(length=8):
    return "user_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def random_email():
    return random_username() + "@example.com"
