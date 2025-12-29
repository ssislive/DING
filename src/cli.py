import sys
from src.data import init

def main():
    if len(sys.argv) < 2:
        print("Usage: ding <command>")
        return

    if sys.argv[1] == "init":
        # ding init
        if len(sys.argv) == 2:
            init()
        # ding init <path>
        elif len(sys.argv) == 3:
            init(sys.argv[2])
        else:
            print("Usage: ding init [path]")
