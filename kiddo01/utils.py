class Kiddo01Utils:
    @staticmethod
    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
