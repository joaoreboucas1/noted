import os
import subprocess
from argparse import ArgumentParser

from lib.config import Config
from lib.setup import setup
from lib.save import save

argp = ArgumentParser()
argp.add_argument("--config", required=False, action="store_true", help="Open config file with `nano`")
argp.add_argument("--save", required=False, action="store_true", help="Save changes: commit and push repo if origin is set.")

root = "."
repo = "repo"

def main():
    args = argp.parse_args()

    if ".todorc" not in os.listdir():
        config = Config(filename="todo.md", editor="code")
        config.dump(f"{root}/.todorc")
    else:
        config = Config.from_file(f"{root}/.todorc")
    
    if args.config: os.execv("/bin/nano", [f'nano', f'.todorc'])
    elif args.save:
        save(root, repo, config)
    else:
        setup(root, repo, config)
        editor_path = subprocess.run(["which", f"{config.editor}"], capture_output=True, text=True).stdout.strip()
        os.execv(editor_path, [f'{config.editor}', f'{root}/{repo}/{config.filename}'])

if __name__ == "__main__":
    main()