class Kiddo01Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        return [token for token in self.tokens if token]
