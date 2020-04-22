import os
import random
import pygame

from AmiiboDictionary.amiiboDictionary import amiiboDatabase

pygame.mixer.init()
amiibo = input()

if amiibo in amiiboDatabase.keys():
    songName = random.choice(os.listdir("music/"+amiiboDatabase[amiibo]))
    pygame.mixer.music.load("music/"+amiiboDatabase[amiibo]+"/"+songName)
    pygame.mixer.music.play()
else:
    songName = random.choice(os.listdir("music/misc"))
    pygame.mixer.music.load("music/misc/" + songName)
    pygame.mixer.music.play()

print('Start Music')
while pygame.mixer.music.get_busy():
    amiibo = input()
    if amiibo == 'end':
        pygame.mixer.music.stop()
    elif amiibo in amiiboDatabase.keys():
        songName = random.choice(os.listdir("music/" + amiiboDatabase[amiibo]))
        pygame.mixer.music.load("music/" + amiiboDatabase[amiibo] + "/" + songName)
        pygame.mixer.music.play()
    else:
        songName = random.choice(os.listdir("music/misc"))
        pygame.mixer.music.load("music/misc/" + songName)
        pygame.mixer.music.play()
    continue

print('exit music')
