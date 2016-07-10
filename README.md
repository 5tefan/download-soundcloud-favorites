# Soundcloud favorites

Python script to automatically download up to 1000 of your most recently liked songs from Soundcloud.

## Features

* Embeds cover picture, title, artist, and tags
* Progress indicated with speed and percent completion

## Requirement

* [Mutagen](https://bitbucket.org/lazka/mutagen/downloads) for mp3
* [ProgressBar](https://pypi.python.org/pypi/progressbar) to display progress
* [Soundcloud](https://github.com/soundcloud/soundcloud-python) interface
* A registered [Soundcloud app](http://soundcloud.com/you/apps/new) (for authentification)

## Usage

Copy the required info from [Soundcloud](https://soundcloud.com/you/apps/) to `sc-fav.py`.

Execute `python sc-fav.py` and songs will start downloading to the music/ directory.

