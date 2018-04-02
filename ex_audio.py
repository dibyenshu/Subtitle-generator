#Script to extract audio from video 
#in flac format at 16kHz sample rate
from subprocess import call

source = "G:/SIH/test.mp4"
destination = "G:/SIH/audio.flac"

cmd = "ffmpeg -i "
cmd += source
cmd += " -f flac -ac 1 -ar 16000 -vn "
cmd += destination

#cmd = 'start'
#cmd=ffmpeg -i video.mp4 -f flac -ac 1 -ar 16000 -vn audio.mp3

call(cmd,shell=True)	#extracts the audio