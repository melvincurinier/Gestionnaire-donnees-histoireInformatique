class Controller():
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        print("Controller initiated !")