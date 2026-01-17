import os
import shutil
from pathlib import Path


def cp_vim():
    shutil.copy("vim/vimrc", os.path.expanduser("~/.vim/vimrc"))


def my_zshrc_operation():
     # 1. 源文件（以脚本所在目录为基准，避免相对路径坑）
    src = Path(__file__).parent / "zshrc" / ".my_zshrc"
    if not src.exists():
        raise FileNotFoundError(f"Source file not found: {src}")
    home = Path.home()
    # 2. 目标文件：~/.my_zshrc（直接覆盖）
    dst = home / ".my_zshrc"
    shutil.copyfile(src, dst)
    print(f"Copied {src} -> {dst}")

    # 3. 确保 ~/.zshrc source ~/.my_zshrc
    zshrc = home / ".zshrc"

    begin = "# >>> my_zshrc begin >>>"
    end = "# <<< my_zshrc end <<<"

    block = (
        f"{begin}\n"
        f"[ -f ~/.my_zshrc ] && source ~/.my_zshrc\n"
        f"{end}\n"
    )

    content = zshrc.read_text() if zshrc.exists() else ""

    if begin not in content:
        with zshrc.open("a") as f:
            f.write("\n" + block)
        print("Injected source into ~/.zshrc")
    else:
        print("~/.zshrc already configured")
 
    
    
def main():
    cp_vim()
    my_zshrc_operation()


if __name__ == "__main__":
    main()
