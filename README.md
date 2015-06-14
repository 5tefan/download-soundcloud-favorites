# Soundcloud favorites
Python scripte to automatically download your recently liked songs from Soundcloud, with embedded picture, title and artist tag.

Shows a list of your recently liked songs, you can then exclude some of them if you want, then proceed to download (with speed and percentage showing) the song, retrieve the cover picture, artist and title and apply the tags to the file.

## Requirement

* [Mutagen](https://bitbucket.org/lazka/mutagen/downloads)
* [ProgressBar](https://pypi.python.org/pypi/progressbar)
* [Soundcloud](https://github.com/soundcloud/soundcloud-python)
* A registered [Soundcloud app](http://soundcloud.com/you/apps/new) (for authentification)

## Usage
Fill the required field for authentification, found [here](https://soundcloud.com/you/apps/) on your registered app. After the list of songs shows up, enter the number of sound you'd like to download (10 for the first 10 songs). To exclude any song, enter the numbers separated by comas
