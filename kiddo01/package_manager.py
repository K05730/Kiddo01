import os

class Kiddo01PackageManager:
    def install(self, package_name):
        print(f"Installing {package_name}...")
        os.system(f"pip install {package_name}")
