#!/usr/bin/env python3

"""Rename music files as {artist}-{album}-{title}."""

from os import listdir, rename
from tinytag import TinyTag
import filetype

files = (file for file in listdir())

for file in files:
    try:
        tag = TinyTag.get(file)
        ext = filetype.guess(file).extension
        rename(file, f'{tag.artist} - {tag.album} - {tag.title}.{ext}')
    except Exception:
        pass
