# TODO App

A terminal app for managing a TODO list.

## Usage

The first step is to setup your config profile: the path to the notes repository, the name of the notes file, the editor you want to use and the repo's remote URL. Edit your profile with
 
```
$ python3 todo.py --config
```

This will create a `.todorc` file with the config parameters. An example of `.todorc` is

```
$ cat .todorc
filename=todo.md
editor=code
origin=git@github.com:username/notes.git
```

After configuring your settings, you may open your notes with

```
$ python3 todo.py
```

After editing your notes, you can save them with

```
$ python3 todo.py --save
```

This command commits any changes to the repository and, if an origin is set in `.todorc`, it pushes the changes.