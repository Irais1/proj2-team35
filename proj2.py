import pygame
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
			sys.exit()