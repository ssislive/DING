import os

DING_DIR = ".ding"

def init(path=None):
    # Case 1: no path given → current directory
    if path is None:
        base_path = os.getcwd()
    else:
        base_path = os.path.abspath(path)

        # Path validation
        if not os.path.exists(base_path):
            print(f"Path does not exist: {base_path}")
            return

        if not os.path.isdir(base_path):
            print(f"Not a directory: {base_path}")
            return

    ding_path = os.path.join(base_path, DING_DIR)

    # Check if already a ding repo
    if os.path.exists(ding_path):
        print("It is a ding repository")
        return

    # Create .ding directory
    os.mkdir(ding_path)
    print(f"Initialised an empty ding repository in {ding_path}")
