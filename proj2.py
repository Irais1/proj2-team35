'''import pygame
from pygame.locals import*
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
print "hey I finaly got this working!"
sounds = []
sounds.append(pygame.mixer.music.load('Afraid.wav'))
sounds.append(pygame.mixer.music.load('riverflowsinyou.wav'))
sounds.append(pygame.mixer.music.load('tearinmyheart.wav'))
#sounds.append(pygame.mixer.music.load('final.wav'))
for sound in sounds:
	pygame.mixer.music.play(0)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()'''
import os
from pydub import AudioSegment

song1 =	'GET' /raw_input ("Enter a song: ")
song2 = raw_input ("Enter a song: ")
song3 = raw_input ("Enter a song: ")
sound1 = AudioSegment.from_file(song1)
kick = AudioSegment.from_file(song2)
snare = AudioSegment.from_file(song3)

ms = len(sound1+kick+snare)/20000000000
beat = AudioSegment.silent(duration=ms).overlay(kick).overlay(snare, position=ms/50) * 2

#combined = (sound1.overlay(beat) * 2).fade_in(100).fade_out(100)
combined = (sound1.overlay(beat) * 4).fade_in(10000).fade_out(10000).set_channels(2)
combined.export("combined.mp3", format='mp3')