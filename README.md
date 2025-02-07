# Noted

**NOTE:** This app is under development! Make anny suggestions and commplaints in our [GitHub Issues](https://github.com/joaoreboucas1/noted/issues).

A terminal app for managing some notes.

## Installation

The installation is as simple as

```
$ pip install -i https://test.pypi.org/simple/ noted
```

## Usage

The first step is to setup your config profile: the path to the notes repository, the name of the notes file, the editor you want to use and the repo's remote URL. Edit your profile with
 
```
$ python3 -m noted.noted --config
```

This will create a `.notedrc` file in your home directory with the config parameters to beused by the program.

**NOTE:** You may create an alias such as `alias noted='python3 -m noted.noted'` and include it in your `.bashrc` (or equivalent).

An example of `.notedrc` is

```
$ cat .notedrc
filename=todo.md
editor=code
repo_path=/home/user/.notes
origin=git@github.com:username/notes.git
```

The `.notedrc` file does not come with an origin field, you must provide it. By providing an origin field, the program initializes the `repo_path` to a git repo associated with the given `origin` URL.

After configuring your settings, you may open your notes with

```
$ python3 -m noted.noted
```

After editing your notes, you can save them with

```
$ python3 -m noted.noted --save
```

This command commits any changes to the repository and, if an origin is set in `.notedrc`, it pushes the changes to the origin.