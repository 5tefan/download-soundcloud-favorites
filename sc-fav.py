import urllib
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error, TIT2, TPE1
from progressbar import FileTransferSpeed, Percentage, ProgressBar
from soundcloud import Client

# Authentification
client = Client(client_id='YOUR_CLIENT_ID',
                client_secret='YOU_CLIENT_SECRET',
                username='EMAIL OR USERNAME',
                password='PASS')

# Welcome
print 'Hello %s' % client.get('/me').username

# Directory to download songs to
download_location = 'music/'

# Make music directory if needed
if not os.path.exists(download_location):
    os.makedirs(download_location)

def progress(count, blockSize, totalSize):
    """ count : number of blocks downloaded ; blockSize : size of a single block (8192) ; total size of the file. urlretrieve update the content constantly"""
    total = totalSize//blockSize 		#  number of blocks it will take to download the entire file
    percent = int(100*count//total)     #  current percentage downloaded
    pbar.update(percent)   				#  update the progress bar by 1% if reached

# Get the favorites and go!
favorites = client.get('/me/favorites', limit=1000)
for i, track in enumerate(favorites):
    title = track.title
    artist=track.user["username"]  
    try: 
        cover = track.artwork_url.replace("large","t500x500")   #  high-res
    except AttributeError:
        cover = track.artwork_url #  lowres

    stream_url = client.get(track.stream_url, allow_redirects=False)
    url = stream_url.location.replace('https', 'http')
    filename = os.path.join(download_location, title.replace("/", "") + '.mp3')
    widgets = ['Downloading  ', title ,': ',Percentage(), FileTransferSpeed(), '  ( %s / %s )' % (i, len(favorites))]
    pbar = ProgressBar(widgets=widgets).start()
    urllib.urlretrieve(url, filename, reporthook=progress) #  Downloads, reports the progress to the progress function
    
    # Adding tags
    mp3_file = MP3(filename, ID3=ID3)
    try:
        mp3_file.add_tags()
    except error:
        pass
    # Cover
    if cover is not None:
		mp3_file.tags.add(
			APIC(
				encoding=3,			#  3 is for utf-8
				mime='image/png', 	#  image/jpeg or image/png
				type=3, 			#  3 is for the cover image
				desc=u'Cover',
				data = urllib.urlopen(cover).read()   
			)
		)
    # Title
    mp3_file.tags.add( TIT2(encoding=3, text = title) )
    # Artist
    mp3_file.tags.add( TPE1(encoding=3, text = artist) )
    mp3_file.save()
    
