from loginModel import LoginModel
from loginScreen import Login

class LoginController:
    def __init__(self):
        self.model = LoginModel()
        self.view = Login(self)

    def authenticate(self, username, password):
        return self.model.authenticate(username, password)

    def run(self):
        self.view.mainloop()