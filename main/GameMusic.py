'''
游戏音效
'''
import pygame
import os


CURRENT_FILE_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE_PATH)

def music_path(path:str):
    SOUND_MUSIC = os.path.join(CURRENT_DIR, "..", "sound", path)
    return SOUND_MUSIC


class GameMusic:
    def __init__(self):
        '''
            游戏音效初始化
        :return: None
        '''
        # 载入游戏音乐
        pygame.mixer.music.load(music_path("game_music.ogg"))
        pygame.mixer.music.set_volume(0.2)
        self.bullet_sound = pygame.mixer.Sound(music_path("bullet.wav"))
        self.bullet_sound.set_volume(0.2)
        self.bomb_sound = pygame.mixer.Sound(music_path("use_bomb.wav"))
        self.bomb_sound.set_volume(0.2)
        self.supply_sound = pygame.mixer.Sound(music_path("supply.wav"))  
        self.supply_sound.set_volume(0.8)
        self.get_bomb_sound = pygame.mixer.Sound(music_path("get_bomb.wav"))
        self.get_bomb_sound.set_volume(0.2)
        self.get_bullet_sound = pygame.mixer.Sound(music_path("get_bullet.wav"))
        self.get_bullet_sound.set_volume(0.2)
        self.upgrade_sound = pygame.mixer.Sound(music_path("upgrade.wav"))
        self.upgrade_sound.set_volume(0.2)
        self.enemy3_fly_sound = pygame.mixer.Sound(music_path("enemy3_flying.wav"))
        self.enemy3_fly_sound.set_volume(0.2)
        self.enemy1_down_sound = pygame.mixer.Sound(music_path("enemy1_down.wav"))
        self.enemy1_down_sound.set_volume(0.2)
        self.enemy2_down_sound = pygame.mixer.Sound(music_path("enemy2_down.wav"))
        self.enemy2_down_sound.set_volume(0.2)
        self.enemy3_down_sound = pygame.mixer.Sound(music_path("enemy3_down.wav"))
        self.enemy3_down_sound.set_volume(0.2)
        self.hero_down_sound = pygame.mixer.Sound(music_path("me_down.wav"))
        self.hero_down_sound.set_volume(0.6)