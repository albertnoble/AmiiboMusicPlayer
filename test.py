import pygame

pygame.mixer.init()
pygame.mixer.music.load('music/Assassins Creed Origins - Winds of Cyrene.mp3')
pygame.mixer.music.play()
print('Start Music')
while pygame.mixer.music.get_busy() == True:
    s = input()
    if s == 'end':
        pygame.mixer.music.stop()
    elif s == 'test2':
        pygame.mixer.music.load('music/test2.mp3')
        pygame.mixer.music.play()
    elif s == 'kk song':
        pygame.mixer.music.load('music/KKWestern2.mid')
        pygame.mixer.music.play()
    continue

print('exit music')