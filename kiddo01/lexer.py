class Kiddo01Lexer:
    def __init__(self, code):
        self.code = code

    def tokenize(self):
        return self.code.split()
