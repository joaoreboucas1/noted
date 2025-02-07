import os
import subprocess
from argparse import ArgumentParser

from .lib.config import Config
from .lib.setup import setup
from .lib.save import save

argp = ArgumentParser()
argp.add_argument("--config", required=False, action="store_true", help="Open config file with `nano`")
argp.add_argument("--save", required=False, action="store_true", help="Save changes: commit and push repo if origin is set.")

rc_path = os.path.expanduser("~/.notedrc")

def main():
    args = argp.parse_args()

    if not os.path.isfile(rc_path):
        config = Config(filename="todo.md", editor="code", repo_path=os.path.expanduser("~/.notes"))
        config.dump(rc_path)
    else:
        config = Config.from_file(rc_path)
    
    if args.config: os.execv("/bin/nano", [f'nano', rc_path])
    elif args.save:
        save(config)
    else:
        setup(config)
        editor_path = subprocess.run(["which", f"{config.editor}"], capture_output=True, text=True).stdout.strip()
        os.execv(editor_path, [f'{config.editor}', f'{config.repo_path}/{config.filename}'])

if __name__ == "__main__":
    main()