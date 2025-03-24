class Kiddo01Interpreter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.split("\\n")
        for line in lines:
            self.execute(line.strip())

    def execute(self, line):
        if not line:
            return
        parts = line.split(" ")
        command = parts[0]

        if command == "say":
            print(" ".join(parts[1:]))
        elif "=" in parts:
            var_name = parts[0]
            var_value = " ".join(parts[2:])
            self.variables[var_name] = var_value
        else:
            print(f"Unknown command: {line}")
