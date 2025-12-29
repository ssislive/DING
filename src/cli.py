def main():
    print("Ding Dong, who's there \nCash\n Cash who?\n I prefer peanuts\n")

from src.data import init

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: ding <command>")
        return

    if sys.argv[1] == "init":
        init()
