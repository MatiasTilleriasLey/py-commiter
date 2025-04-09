from module.git import * 
from module.commit import *
import sys

def main():
    if checkGit():
        if checkWorkingTree() == False:
            trackFiles = input("""[!]There are files that are not in the "Tracked" status.
[?]Would you like us to run the "git add ." command to fix this? [y/n] """).lower()
            if trackFiles == "y":
                gitAdd()
            commitMessageCreator()
    else:
        raise Exception("Git check failed.")
        sys.exit(1)
if __name__ == "__main__":
    main()
