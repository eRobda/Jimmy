from googleapiclient.discovery import build
from pytube import YouTube
import vlc
import threading

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'AIzaSyBMG4f_zmLQ5JSriCHHOcIuhbhXPCY-P70'
def search_video_by_title(title):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        q=title,
        part='snippet',
        maxResults=1
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_url
    else:
        return None

def play_video_in_vlc(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video_url = video.url
    Instance = vlc.Instance('--no-video')
    player = Instance.media_player_new()
    Media = Instance.media_new(video_url)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    return player

def play_music(name):
    video_url = search_video_by_title(name)
    if video_url:
        player = play_video_in_vlc(video_url)
        return player
    else:
        return None

player = None

def playsong(name):
    global player
    player = play_music(name)

def pause():
    global player
    if player:
        player.pause()

def resume():
    global player
    if player:
        player.play()

def stop():
    global player
    if player:
        player.stop()