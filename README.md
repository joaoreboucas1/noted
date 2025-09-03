# Noted

> [!Warning]
> This app is under development! Make any suggestions and commplaints in our [GitHub Issues](https://github.com/joaoreboucas1/noted/issues).

A terminal app for managing some notes.

## Installation

Install `noted` using `pip`

```console
pip install noted-app
```

## Usage

The first step is to setup your config profile: the path to the notes repository, the name of the notes file, the editor you want to use and the repo's remote URL. Edit your profile with

```console
noted --config
```

This will create a `.notedrc` file in your home directory with the config parameters to be used by the program. An example of `.notedrc` is

```
editor=code
repo_path=/home/user/.notes
files={"default": "todo.md", "read": "reading-list.md"}
origin=
```

The options are:
- `editor`: the editor to open the files
- `repo_path`: a directory to store the files
- `files`: a list of commands to open different files. `"default"` refers to the file opened with the command `noted`; in the example above, the command `noted read` opens the file `reading-list.md`
- `origin` (optional): set an SSH or HTTPS origin for the repository. Every time you open a file with noted, it first performs a `git pull`. The command `noted --save` commits and, if `origin` is set, pushes the current version.

After configuring your options, you can open your notes with

```console
noted
```

After editing your notes, you can save them with

```console
noted --save
```

This command commits any changes to the repository and, if an origin is set in `.notedrc`, it pushes the changes to the origin.