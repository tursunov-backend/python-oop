class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_actuve = is_active

    def info(self):
        return f"User(username='{self.username}', email='{self.email}', is_active='{self.is_actuve}')"

u01 = User('Abdujalol', 'Abu@gmail.com', True)

print(u01.info())