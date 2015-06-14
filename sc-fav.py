# -*- coding: utf-8 -*-
import urllib
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error, TIT2, TPE1
from progressbar import FileTransferSpeed,Percentage,ProgressBar
from soundcloud import Client

# Authentification

client = Client(client_id='YOUR_CLIENT_ID',
                client_secret='YOU_CLIENT_SECRET',
                username='EMAIL OR USERNAME',
                password='PASS')

print ('Hello',client.get('/me').username,',','showing your recently favorited songs :')

                           
favorites = client.get('/me/favorites', limit=30)   # shows a list with your last 30 favorited songs
for track in favorites:
    a=str(1+favorites.index(track))+'.'
    title = track.title
    artist = track.user["username"]    
    print(a,title,' by ',username)
    
print()
n = int(input('How many songs would you like to download ?'))
print()
numbers = input('Songs to be excluded: ').split(",")

def progress(count, blockSize, totalSize):
    """ count : number of blocks downloaded ; blockSize : size of a single block (8192) ; total size of the file. urlretrieve update the content constantly"""
    total = totalSize//blockSize    #    number of blocks it will take to download the entire file
    percent = int(100*count//total)     #   current percentage downloaded
    pbar.update(percent)    #update the progress bar by 1% if reached

i=0
for track in favorites[:n]:
    
    no=favorites.index(track) # Checks if the track is excluded
    if str(no+1) in numbers:
        continue
    #Getting all the data from soundcloud

    title = track.title
    artist=track.user["username"]  
    cover_url = track.artwork_url   #low-res
    cover = cover_url.replace("large","t500x500")   #high-res
    stream_url = client.get(track.stream_url, allow_redirects=False)
    url = stream_url.location.replace('https', 'http')
    format = '.mp3'
    filename= title + format
    i=i+1
    widgets = ['Downloading  ', title ,': ',Percentage(), FileTransferSpeed(),'  (',str(i),'/',str(n-len(numbers)),')',]
    pbar = ProgressBar(widgets=widgets).start()
    urllib.request.urlretrieve(url, filename, reporthook=progress) # Downloads, reports the progress to the progress function
    
    #Adding tags
    file = MP3(filename, ID3=ID3)
    
    try:
        file.add_tags()
    except error:
        pass
    #Cover
    file.tags.add(
        APIC(
            encoding=3, # 3 is for utf-8
            mime='image/png', # image/jpeg or image/png
            type=3, # 3 is for the cover image
            desc=u'Cover',
            data=urllib.request.urlopen(cover).read()   
        )
    )
    #Title
    file.tags.add(
        TIT2(encoding=3, text = title)
        )
    #Artist
    file.tags.add(
        TPE1(encoding=3, text = artist)
        )
    
    file.save()
    
    
