import os
import subprocess
import socket
from datetime import datetime

# Commit todo file to repo and possibly push to origin
def save(config):
    cwd = os.getcwd()
    os.chdir(config.repo_path)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"[todo.py] Commit by {socket.gethostname()} at {datetime.now()}"])
    if config.origin is not None: subprocess.run(["git", "push", "origin", "main"])
    os.chdir(cwd)