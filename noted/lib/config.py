import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    filename: str
    repo_path: str
    editor: str
    origin: Optional[str] = None

    def dump(self, filename: str):
        with open(filename, "w") as f:
            for field in self.__dataclass_fields__.keys():
                value = getattr(self, field)
                if value is not None: f.write(f"{field}={value}\n")

    def from_file(filename: str):
        if not os.path.exists(filename): raise Exception(f"ERROR: tried to import Config from file {filename} which could not be found")
        c: Config = Config(filename="", editor="", repo_path="")
        with open(filename, "r") as f: lines = f.read().splitlines()
        for line in lines:
            stmt: list[str] = line.strip().split("=")
            if len(stmt) != 2: raise Exception(f"ERROR: in Config file '{filename}': Could not parse field '{line}'")
            field, value = stmt
            if field not in Config.__dataclass_fields__.keys(): raise Exception(f"ERROR: in Config file '{filename}': Invalid config '{field}'")
            setattr(c, field, value.strip())
        return c