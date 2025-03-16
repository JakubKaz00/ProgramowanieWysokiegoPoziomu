class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

    def __str__(self):
        return f"{self.producent} {self.model}"