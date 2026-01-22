class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_actuve = is_active

    def activate(self):
        self.is_active = True
        print(f"{self.username} foydalanuvchisi faollashtirildi")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} foydalanuvchisi bloklandi")

u01 = User('Abdujalol', 'Abu@gmail.com', True)

u01.activate()
u01.deactivate()