import os
import subprocess

from .config import Config

# Setup phase that creates the git repo and the .todorc file
def setup(root, repo, config):
    if not os.path.isdir(f"{root}/{repo}"): os.mkdir(f"{root}/{repo}")

    os.chdir(f"{root}/{repo}")

    if not os.path.isdir(f".git"): subprocess.run(["git", "init"])

    if config.origin is not None:
        proc = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        if "origin" not in proc.stdout: subprocess.run(["git", "remote", "add", "origin", f"{config.origin}"])
        subprocess.run(["git", "pull", "origin", "main"])

    subprocess.run(["touch", f"{config.filename}"])

    os.chdir("..")

    return config
