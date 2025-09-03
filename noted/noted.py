import os
import subprocess
from argparse import ArgumentParser

from .lib.config import Config
from .lib.setup import setup
from .lib.save import save

argp = ArgumentParser()
argp.add_argument("file_cmd", help="Alias of the file you want to open", nargs="?", default="default")
argp.add_argument("--config", required=False, action="store_true", help="Open config file with `nano`")
argp.add_argument("--save", required=False, action="store_true", help="Save changes: commit and push repo if origin is set")

rc_path = os.path.expanduser("~/.notedrc")

def main():
    args = argp.parse_args()

    if not os.path.isfile(rc_path):
        config = Config(files={"default": "todo.md"}, editor="code", repo_path=os.path.expanduser("~/.notes"))
        config.dump(rc_path)
    else:
        config = Config.from_file(rc_path)
    
    if args.config: os.execv("/bin/nano", [f'nano', rc_path])
    elif args.save: save(config)
    else:
        setup(config)
        if args.file_cmd not in config.files:
            print(f"ERROR: file {args.file_cmd} is unknown; available files are: {config.files}")
            exit(1)
        if config.editor is None:
            print(f"ERROR: user did not provide editor for opening notes.")
            exit(1)

        editor_path = subprocess.run(["which", f"{config.editor}"], capture_output=True, text=True).stdout.strip()
        if not os.path.isfile(editor_path):
            print(f"ERROR: editor {config.editor} does not seem to exist in your system. We did `which {config.editor}` and we could not find it.")
            exit(1)

        os.execv(editor_path, [f'{config.editor}', f'{config.repo_path}/{config.files[args.file_cmd]}'])

if __name__ == "__main__":
    main()