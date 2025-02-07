import os
import subprocess

from .config import Config

# Setup phase that creates the git repo and the .todorc file
def setup(config):
    cwd = os.getcwd()

    if not os.path.isdir(config.repo_path): os.mkdir(config.repo_path)

    os.chdir(config.repo_path)

    if not os.path.isdir(f".git"): subprocess.run(["git", "init"])

    if config.origin is not None:
        proc = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        if "origin" not in proc.stdout: subprocess.run(["git", "remote", "add", "origin", f"{config.origin}"])
        subprocess.run(["git", "pull", "origin", "main"])

    subprocess.run(["touch", f"{config.filename}"])

    os.chdir(cwd)

    return config
