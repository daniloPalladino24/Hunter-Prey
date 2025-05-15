import pygame

PATH = "Progetto Palladino Danilo-Dedi Vittorio/media/"
    
pygame.init()
pygame.mixer.init()

walkRight = [pygame.image.load(PATH + f'R{i}.png') for i in range(1, 7)]
walkLeft = [pygame.image.load(PATH + f'L{i}.png') for i in range(1, 7)]
DwalkRight = [pygame.image.load(PATH + f'DR{i}.png') for i in range(1, 7)]
DwalkLeft = [pygame.image.load(PATH + f'DL{i}.png') for i in range(1, 7)]
bg = pygame.image.load(PATH + 'bg.png')
charHR = pygame.image.load(PATH + 'RBS.png')
charHL = pygame.image.load(PATH + 'LBS.png')
charDR = pygame.image.load(PATH + 'DRstanding.png')
charDL = pygame.image.load(PATH + 'DLstanding.png')
menu_bg= pygame.image.load(PATH + 'menu_background.png')

pygame.mixer.music.load(PATH + "bgs.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

projectile_sound = pygame.mixer.Sound(PATH + "suono_proiettile.wav")  
projectile_sound.set_volume(0.1)