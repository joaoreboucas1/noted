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

This will create a `.notedrc` file in your home directory with the config parameters. An example of `.notedrc` is

```
$ cat .notedrc
filename=todo.md
editor=code
repo_path=/home/user/.notes
origin=git@github.com:username/notes.git
```

The `.notedrc` file does not come with an origin field, you must provide it.

After configuring your settings, you may open your notes with

```
$ python3 -m noted.noted
```

After editing your notes, you can save them with

```
$ python3 -m noted.noted --save
```

This command commits any changes to the repository and, if an origin is set in `.notedrc`, it pushes the changes.