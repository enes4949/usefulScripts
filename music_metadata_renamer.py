#!/usr/bin/env python3

"""Rename music files as {artist}-{album}-{title}."""

<<<<<<< HEAD
from os import listdir
from os.path import isdir
from shutil import move
from tinytag import TinyTag, TinyTagException
=======
from os import listdir, rename
from tinytag import TinyTag
>>>>>>> 12d74ca6f880efe10b0482a205b9e1f61e5d78e7
import filetype

files = (file for file in listdir())

<<<<<<< HEAD

if __name__ == "__main__":
    for file in files:
        if isdir(file):
            continue
        try:
            tag = TinyTag.get(file)
            ext = filetype.guess(file).extension
            move(
                file, f'{tag.artist} - {tag.album} - {tag.title}.{ext}')
        except FileNotFoundError:
            move(
                file, f'{tag.artist.replace("/","")} - {tag.album.replace("/","")} - {tag.title.replace("/","")}.{ext}')
        except TinyTagException:
            pass
=======
for file in files:
    try:
        tag = TinyTag.get(file)
        ext = filetype.guess(file).extension
        rename(file, f'{tag.artist} - {tag.album} - {tag.title}.{ext}')
    except Exception:
        pass
>>>>>>> 12d74ca6f880efe10b0482a205b9e1f61e5d78e7
