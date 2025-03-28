import sys
from kiddo01.interpreter import Kiddo01Interpreter
from kiddo01.package_manager import Kiddo01PackageManager

def main():
    if len(sys.argv) < 2:
        print("Usage: kiddo01 <file.kiddo> or kiddo01 --install <package>")
        return
    
    if sys.argv[1] == "--install":
        if len(sys.argv) < 3:
            print("Usage: kiddo01 --install <package>")
            return
        package_manager = Kiddo01PackageManager()
        package_manager.install(sys.argv[2])
    else:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            code = f.read()
        interpreter = Kiddo01Interpreter()
        interpreter.run(code)

if __name__ == "__main__":
    main()
