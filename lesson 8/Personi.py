class Personi:

    def __init__(self, emri,vitilindjes,gjinia):
        self.emri=emri
        self.vitilindjes=vitilindjes
        self.gjinia=gjinia

    def prezantimi(self):
        print(f"une jam: {self.emri}, kam lindur ne vitin: {self.vitilindjes}")

    def sayHi(self):
        print(f"pershendetje nga: {self.emri}")