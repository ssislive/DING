import os

DING_DIR = ".ding"

def init():
    cwd = os.getcwd()
    ding_path = os.path.join(cwd, DING_DIR)

    if os.path.exists(ding_path):
        print("It is a ding repository")
        return

    os.mkdir(ding_path)
    print(f"Initialised an empty ding repository in {ding_path}")
