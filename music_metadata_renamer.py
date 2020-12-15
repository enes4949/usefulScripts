#!/usr/bin/env python3

"""Rename music files as {artist}-{album}-{title}."""

from os import listdir, rename
from tinytag import TinyTag, TinyTagException

files = (file for file in listdir())

for file in files:
    try:
        tag = TinyTag.get(file)
        rename(file, f'{tag.artist} - {tag.album} - {tag.title}.flac')
    except Exception:
        pass
