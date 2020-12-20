#!/usr/bin/env python3

"""Rename music files as {artist}-{album}-{title}."""

from os import listdir
from os.path import isdir
from shutil import move
from tinytag import TinyTag, TinyTagException
import filetype

files = (file for file in listdir())


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
