from loginController import LoginController

class MainApp:
    def __init__(self):
        self.controller = LoginController()

    def run(self):
        self.controller.run()

if __name__ == "__main__":
    app = MainApp()
    app.run()
