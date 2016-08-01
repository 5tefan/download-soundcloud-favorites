# Download Soundcloud favorites

Python 2.7 script to automatically download up to 1000 of your most recently <3 songs from Soundcloud.

## Features

* Embeds cover picture, title, artist, and tags
* Progress indicated with speed and percent completion

## Requirements

* [Mutagen](https://github.com/quodlibet/mutagen),  `pip install mutagen` for mp3
* [ProgressBar](https://pypi.python.org/pypi/progressbar), `pip install progressbar` to display progress
* [Soundcloud](https://github.com/soundcloud/soundcloud-python), `pip install soundcloud` soundcloud api
* A registered [Soundcloud app](http://soundcloud.com/you/apps/new) (for authentification)

Install all dependencies at once with `pip install mutagen progressbar soundcloud`

## Usage

Copy the required info from [Soundcloud](https://soundcloud.com/you/apps/) to `sc-fav.py`.

Execute `python sc-fav.py` and songs will start downloading to the ./music/ directory.

