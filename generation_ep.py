import random
import string

class EmailPasswordGenerator:
    def __init__(self):
        self.email = None
        self.password = None

    def generate(self):
        if self.email is None and self.password is None:
            name = ''.join(random.choices(string.ascii_lowercase, k=8))
            domain = "yandex.ru"
            self.email = f"{name}_{random.randint(100, 999)}@{domain}"
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return self.email, self.password
