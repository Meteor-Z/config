import os
import shutil


def move_zshrc():
    shutil.copy(".zshrc", os.path.expanduser("~/.zshrc"))
    


def main():
    move_zshrc()


if __name__ == "__main__":
    main()