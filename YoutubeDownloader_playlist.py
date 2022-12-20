from pytube import Playlist
from pytube import YouTube

yt_paylist = Playlist('https://www.youtube.com/watch?v=uRsE5WGiKWo&list=PLgNJO2hghbmjpjt9sa2POi4U0a1-GGTlj')


print(f"downloading : {yt_paylist.title}")

# it will show all url of playlist
# for url in yt_paylist.video_urls:
#    print(url)

# this is show all Videos in playlist and start downloading
for video in yt_paylist.videos:
    vid = video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    vid.download()

print("Successfully")



"========================= this is for YT Channel ============="

'''
 c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
>>> print(f'Downloading videos by: {c.channel_name}')
Downloading videos by: ProgrammingKnowledge
>>> for video in c.videos:
>>>     video.streams.first().download()
'''