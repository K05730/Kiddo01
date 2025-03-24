class Kiddo01Teacher:
    def teach(self, concept):
        lessons = {
            "variables": "A variable stores a value. Example: x = 10",
            "loops": "A loop repeats a block of code. Example: loop x less 5:"
        }
        return lessons.get(concept, "Concept not found")
