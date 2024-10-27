#plane.py

import pygame
from GameConfig import *

class Plane(pygame.sprite.Sprite):   # 继承精灵类（用于碰撞检测）
    def __init__(self):
        super().__init__()
        # self.image1 = pygame.image.load(PLANE1_IMG).convert_alpha()  # 获取飞机的实体部分
        self.image1 = pygame.image.load(PLANE1_IMG).convert_alpha()
        self.image2 = pygame.image.load(PLANE2_IMG).convert_alpha()
        # 定义标记飞机实体
        self.mask = pygame.mask.from_surface(self.image1)
        # 获取飞机的尺寸
        self.rect = self.image1.get_rect()
        # 定义飞机放置位置
        self.rect.left = (WIDTH - self.rect.width) //  2
        self.rect.top = HEIGHT - 60 - self.rect.height
        # 定义飞机飞行的速度
        self.speed = 10
        # 定义飞机存活状态
        self.active = True
        # 定义飞机生命
        self.life = 3
        # 飞机销毁图片
        self.destory_images = []
        self.destory_images.extend([
        pygame.image.load(PLANE_DESTORY_IMAGE1).convert_alpha(),
        pygame.image.load(PLANE_DESTORY_IMAGE2).convert_alpha(),
        pygame.image.load(PLANE_DESTORY_IMAGE3).convert_alpha(),
        pygame.image.load(PLANE_DESTORY_IMAGE4).convert_alpha()])
        # 定义飞机无敌状态
        self.invincible = False


    def reset(self):
        """
        我方飞机重置
        :return: None 
        """
        self.active = True
        self.invincible = True
        self.rect.left = (WIDTH - self.rect.width) // 2
        self.rect.top = HEIGHT - self.rect.height - 60
        

    def moveUp(self):
        '''
            向上移动
        :return: None
        '''
        # 判断飞机是否超出屏幕外
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
    
    def moveDown(self):
        '''
            向下移动
        :return: None
        '''
        # 判断飞机是否超出屏幕外
        if self.rect.bottom < HEIGHT - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = HEIGHT - 60
    
    def moveLeft(self):
        '''
            向左移动
        :return: None
        '''
        # 判断飞机是否超出屏幕外
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    
    def moveRight(self):
        '''
            向右移动
        :return: None
        '''
        # 判断飞机是否超出屏幕外
        if self.rect.right < WIDTH:
            self.rect.right += self.speed
        else:
            self.rect.right = WIDTH