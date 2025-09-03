import os
import json
from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Config:
    editor: str
    repo_path: str
    files: Dict[str, str]
    origin: Optional[str] = None

    @staticmethod
    def from_file(filename: str) -> "Config":
        c = Config(editor="", repo_path="", files={})
        filename = os.path.expanduser(filename)
        possible_configs = list(Config.__dataclass_fields__.keys())
        if not os.path.exists(filename): raise Exception(f"Tried to import Config from file {filename} which could not be found")
        with open(filename, "r") as f: lines = f.read().splitlines()
        for i, line in enumerate(lines):
            stmt: list[str] = line.strip().split("=")
            if len(stmt) != 2: raise Exception(f"In Config file '{filename}': Could not parse field '{line}'")
            field, value = stmt

            if field not in possible_configs: raise Exception(f"'{filename}:{i+1}': Invalid option '{field}'. Available options are: {possible_configs}")
            if field == "files":
                c.files = json.loads(value.__str__().replace("\'", "\""))
            else:
                if value == "": setattr(c, field, None)
                else: setattr(c, field, value.strip())
        return c
    
    def dump(self, filename: str):
        with open(filename, "w") as f:
            for field in self.__dataclass_fields__.keys():
                value = getattr(self, field)
                if value is not None: f.write(f"{field}={value}\n")
                else: f.write(f"{field}=\n")
