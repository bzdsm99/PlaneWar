from GameConfig import *
import pygame as pg
from plane import Plane 
from GameMusic import GameMusic

class ScreenImages():
    def __init__(self):
        self.__icon_img = pg.image.load(ICON_IMAGE)
        self.__bg_img = pg.image.load(BACKGROUND_IMAGE)
        
    @property
    def icon_img(self):
        return self.__icon_img
    @property
    def bg_img(self):
        return self.__bg_img
         
class GameScreenManager(ScreenImages):
    def __init__(self):
        super().__init__()
        self.__screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption("飞机大战")
        pg.display.set_icon(self.icon_img)
        
        self.hero = Plane()
    
    
    def control_plane(self):
        self.__key__pressed = pg.key.get_pressed()
        
        if self.__key__pressed[pg.K_w] or self.__key__pressed[pg.K_UP]:
            self.hero.moveUp()
        elif self.__key__pressed[pg.K_s] or self.__key__pressed[pg.K_DOWN]:
            self.hero.moveDown()
        elif self.__key__pressed[pg.K_a] or self.__key__pressed[pg.K_LEFT]:
            self.hero.moveLeft()
        elif self.__key__pressed[pg.K_d] or self.__key__pressed[pg.K_RIGHT]:
            self.hero.moveRight() 
        
    
     
    @property
    def screen(self):
        return self.__screen
    
    def draw_plane(self):
        self.__screen.blit(self.hero.image1,self.hero.rect)



class GameView(GameMusic):
    pg.init()   #初始化检查
    pg.mixer.init()
    def __init__(self):
        super().__init__()
        self.__manager = GameScreenManager()
        
        self.__bg_y = 0                                             # 初始化背景图片的垂直偏移量
        self.__scroll_speed = 5                                     # 可以根据需要调整滚动速度

    
    
    def main(self):
        bg_copy = self.__manager.bg_img.copy()  # 复制背景图片以避免直接修改原图
        pg.mixer.music.play(-1)
        while(True):
            
            self.__bg_y = (self.__bg_y + self.__scroll_speed) % SCREEN_SIZE[1]      # 计算新的背景位置


            self.__manager.screen.blit(self.__manager.bg_img,dest=(0,0))            # 分别在顶部和底部绘制背景图片，以实现滚动效果
            self.__manager.screen.blit(bg_copy, (0, self.__bg_y - SCREEN_SIZE[1]))  # 顶部
            self.__manager.screen.blit(bg_copy, (0, self.__bg_y))                   # 底部
            
            
            self.__manager.draw_plane()
            self.__manager.control_plane()


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # exit()
                    return     # 更改为return，以便更优雅地退出游戏循环，而不是直接调用exit().使用return可以让解释器有机会执行函数结束时的清理工作，比如关闭文件、释放资源等。直接使用exit()会立即终止程序，可能会跳过必要的清理步骤。调试友好：当程序遇到exit()调用时，会立即终止，不提供进一步调试信息的机会。
            
            
            pg.display.update()
            pg.time.Clock().tick(60)                                # 控制帧率为60fps，可根据需要调整



