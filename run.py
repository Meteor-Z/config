import os
import shutil


def cp_vim():
    shutil.copy("vim/vimrc", os.path.expanduser("~/.vim/vimrc"))


def cp_zshrc():
    shutil.copy(".zshrc", os.path.expanduser("~/.zshrc"))

def main():
    cp_vim()
    cp_zshrc()


if __name__ == "__main__":
    main()
