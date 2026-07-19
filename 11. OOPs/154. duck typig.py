class AudioPlayer:
    def play(self): print("Playing audio...")

class VideoPlayer:
    def play(self): print("Playing video...")

def start_media(player):
    player.play() # Works for any object with a 'play' method

start_media(AudioPlayer())
start_media(VideoPlayer())