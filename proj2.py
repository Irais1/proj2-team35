# This program takes in three audio files of type wav and mixes them together

from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence
from tkFileDialog import askopenfilename
import Tkinter as tk
import glob as gb

'''def getAudio(song1, song2, song3):
	sound = [
 AudioSegment.from_file(song1),
 AudioSegment.from_file(song2),
 AudioSegment.from_file(song3)
 ]
 	return sound'''
#getting the path of the audio and opening the files
def mixAudio():
    root = tk.Tk()
    root.withdraw()
    
    song1 = askopenfilename()
    song2 = askopenfilename()
    song3 = askopenfilename()
    #opening the audio to be able to use it in the program
    sound = [
 AudioSegment.from_file(song1),
 AudioSegment.from_file(song2),
 AudioSegment.from_file(song3)
 ]
    
    combineds = AudioSegment.empty()# make empty audio file
    ms = 3000
    beat = AudioSegment.silent(duration=ms).overlay(sound[1]).overlay(sound[2],position=ms//2) * 4
    for song in sound:
        combined = (song.overlay(beat) * 2).fade_in(1000).fade_out(1000).reverse
        combined = (song.overlay(beat) * 2).fade_in(1000).fade_out(1000).set_channels(1)
        combineds += combined #combining audio files
    
    hope = AudioSegment.empty()	#three minutes is : 180000ms & 45 seconds is : 45000 = 225000(3:45)
    hope += combineds[:225000] # making 3:45 min long
    hope = hope.fade_in(30)
    hope = hope.fade_out(30)

    hope.export("combined9.wav", format='wav')
    sourcefile_wav = gb.glob("*.wav")
    
    return sourcefile_wav[3]
