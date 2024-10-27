from GameConfig import *
from gameStatus import GameStatus
import pygame as pg
from plane import Plane 
from GameMusic import GameMusic
from GameScreen import *
from GameController import GameController
from bullet import *
import sys
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



class GameView(GameScreen, GameMusic, GameStatus):
    
    def __init__(self):
        pg.init()   #初始化检查
        pg.mixer.init()
        self.__controller = GameController()
        super().__init__()
        self.__manager = GameScreenManager()
        self.__screenManager = GameScreenManage()
        # 实例化游戏状态对象
        self.__status = GameStatus()
        self.__bg_y = 0                                             # 初始化背景图片的垂直偏移量
        self.__scroll_speed = 5                                     # 可以根据需要调整滚动速度

    

    def main(self):
        #self.__screen = pygame.display.set_mode(SCREEN_SIZE)
        # 循环播放背景音乐
        pygame.mixer.music.play(-1)


        # 调用添加子弹方法
        self.__controller.add_bullet1(self.__screenManager.bullet1_number,self.__screenManager.hero.rect.midtop,Bullet1,self.__screenManager.bullet1_list)
        self.__controller.add_enemies_manager(15, 8, 2)
        bg_copy = self.__manager.bg_img.copy()  # 复制背景图片以避免直接修改原图pg.mixer.music.play(-1)

        # 调用添加超级子弹方法
        self.__controller.add_bullet2(self.__screenManager.bullet2_number,self.__screenManager.hero,Bullet2,self.__screenManager.bullet2_list)
       
        
        while(True):
            # 调用滚动屏幕方法
            self.__screenManager.screenRoll()
            # 元素显示绘制
            self.__screenManager.elementDisplayDraw()
            
            self.__bg_y = (self.__bg_y + self.__scroll_speed) % SCREEN_SIZE[1]      # 计算新的背景位置


            self.__manager.screen.blit(self.__manager.bg_img,dest=(0,0))            # 分别在顶部和底部绘制背景图片，以实现滚动效果
            self.__manager.screen.blit(bg_copy, (0, self.__bg_y - SCREEN_SIZE[1]))  # 顶部
            self.__manager.screen.blit(bg_copy, (0, self.__bg_y))                   # 底部
            
            self.__screenManager.enemyDraw(self.__controller.big_enemies,self.__controller.middle_enemies,self.__controller.small_enemies, self.__controller.enemies)
            self.__manager.draw_plane()
            self.__manager.control_plane()
            
            # 绘制子弹
            #self.__gameScreen.bulletDraw(self.__controller.enemies)
            self.__screenManager.bulletDraw(self.__controller.enemies,self.__controller.middle_enemies, self.__controller.big_enemies)

            if self.__screenManager.game_running: # 开始游戏
 
                pygame.time.set_timer(self.__screenManager.SUPPLY_TIMER, 0)
                self.__screenManager.gameStarting()
            else:
                if self.__screenManager.hero.life:
                    if not self.__status.puased_flag:
                        # 绘制子弹
                        self.__screenManager.bulletDraw(self.__controller.enemies,self.__controller.middle_enemies,self.__controller.big_enemies)
                        # 绘制飞机
                        self.__screenManager.planeDraw()
                        # 控制飞机移动
                        self.__screenManager.controlPlaneMove()
                        self.__screenManager.mouseControlPlaneMove()
                        # 绘制敌机
                        self.__screenManager.enemyDraw(self.__controller.big_enemies,self.__controller.middle_enemies,self.__controller.small_enemies, self.__controller.enemies,self.__controller.bloodDraw)
                        # 游戏等级提升
                        self.__controller.game_level_upgrade(self.__screenManager.score,self.upgrade_sound)
                        # 调用暂停不显示的功能
                        self.__screenManager.elementHideDraw()
                        # 绘制补给
                        self.__screenManager.supplyDraw()
                        # 元素显示绘制
                        self.__screenManager.elementDisplayDraw(self.__status.show_image,self.__status.paused_rect)
                        # 游戏结束画面
                    elif self.__screenManager.hero.life == 0:
                        # 调用结束画面
                        self.__screenManager.gameOverDraw(self.main,
                        self.__controller.small_enemies, self.__controller.middle_enemies,
                        self.__controller.big_enemies, self.__controller.enemies)
                        # 设置屏幕的刷新频率
                        self.__screenManager.clock.tick(60)
                        # 更新窗口
                        pygame.display.update()




            if not self.puased_flag:
                # 游戏等级提升
                self.__controller.game_level_upgrade(self.__screenManager.score, self.upgrade_sound)








            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # exit()
                    return     # 更改为return，以便更优雅地退出游戏循环，而不是直接调用exit().使用return可以让解释器有机会执行函数结束时的清理工作，比如关闭文件、释放资源等。直接使用exit()会立即终止程序，可能会跳过必要的清理步骤。调试友好：当程序遇到exit()调用时，会立即终止，不提供进一步调试信息的机会。
            for event in pygame.event.get(): # 遍历事件
                # 判断事件是否为退出
                if event.type == pg.QUIT:
                    pygame.quit() # 关闭游戏
                    sys.exit() # 结束程序
            
                elif event.type == pg.MOUSEBUTTONDOWN: # 判断是否为鼠标点击事件
                    if event.button == 1 and self.__status.paused_rect.collidepoint(event.pos): # 点击左键并在图标内
                        self.__status.puased_flag = not self.__status.puased_flag # 切换暂停状态

                    if self.__status.puased_flag: # 暂停游戏停止所有音效
                        pygame.time.set_timer(self.__screenManager.SUPPLY_TIMER, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else: # 非暂停情况下恢复所有音效
                        pygame.time.set_timer(self.__screenManager.SUPPLY_TIMER, 30 *1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                    





                elif event.type == pg.MOUSEMOTION: # 判断是否为鼠标移动事件
                    if self.__status.paused_rect.collidepoint(event.pos): # 鼠标悬停在图标上
                        if self.__status.puased_flag: # 暂停状态
                            self.__status.show_image =self.__status.resume_pressed_image
                        else:
                            self.__status.show_image =self.__status.pause_pressed_image
                    else: # 鼠标未悬停在图标上
                        if self.__status.puased_flag: # 恢复状态
                            self.__status.show_image = self.__status.resume_nor_image
                        else:
                            self.__status.show_image = self.__status.pause_nor_image






                elif event.type == pg.KEYDOWN: # 判断是否为按键事件
                    if event.key == pg.K_SPACE: # 是否按下空格键
                        if self.__screenManager.bomb_number: # 判断超级炸弹是否还有剩余
                            self.__screenManager.bomb_number -= 1
                            self.__screenManager.bomb_sound.play()
                    # 播放全屏炸弹音效
                    for e in self.__controller.enemies: #遍历所有的敌机对象
                        if e.rect.bottom > 0: # 判断敌机是否进入屏幕内
                            e.active = False # 敌机销毁







                elif event.type == self.__screenManager.SUPPLY_TIMER: # 检测补给事件
                    # 播放补给发放音效
                    self.__screenManager.supply_sound.play()
                    # 随机选择发放补给
                    if random.choice([True, False]):
                        self.__screenManager.bomb_supply.reset()
                    else:
                        self.__screenManager.bullet_supply.reset()





                elif event.type ==self.__screenManager.DOUBLE_BULLET_TIMER: # 超级子弹检测事件
                    self.__screenManager.is_double_bullet = False
                    pygame.time.set_timer(self.__screenManager.DOUBLE_BULLET_TIMER, 0)
                




                elif event.type == self.__screenManager.INVINCIBLE_TIMER: # 我方飞机无敌事件检测
                    self.__screenManager.hero.invincible = False
                    pygame.time.set_timer(self.__screenManager.INVINCIBLE_TIMER, 0)

            





                if not self.__status.puased_flag:
                    # 绘制补给
                    self.__screenManager.supplyDraw()

                    # 控制飞机移动
                    self.__screenManager.controlPlaneMove()
                    # self.__screenManager.mouseControlPlaneMove()
                    # 绘制敌机
                    self.__screenManager.enemyDraw(self.__controller.big_enemies,self.__controller.middle_enemies, self.__controller.small_enemies,self.__controller.enemies, self.__controller.bloodDraw)
                    # 绘制子弹
                    self.__screenManager.bulletDraw(self.__controller.enemies,self.__controller.middle_enemies, self.__controller.big_enemies)
                    # 元素显示绘制
                    self.__screenManager.elementDisplayDraw(self.__status.show_image,self.__status.paused_rect)

                    # 绘制飞机
                    self.__screenManager.planeDraw()

                    # 调用暂停不显示的功能
                    self.__screenManager.elementHideDraw()
                    # 设置屏幕的刷新频率
                    self.__screenManager.clock.tick(60)
                    



                if self.__screenManager.hero.life:
                    if not self.__status.puased_flag:
                        # 元素显示绘制
                        self.__screenManager.elementDisplayDraw(self.__status.show_image,
                        self.__status.paused_rect)
                    # 游戏结束画面
                    elif self.__screenManager.hero.life == 0:
                        # 调用结束画面
                        self.__screenManager.gameOverDraw(self.main,
                        self.__controller.small_enemies, self.__controller.middle_enemies,
                        self.__controller.big_enemies, self.__controller.enemies)
                        # 设置屏幕的刷新频率
                        self.__screenManager.clock.tick(60)
                        # 更新窗口
                        pygame.display.update()
                        print("Game Over")







                # 更新窗口
                pg.display.update()
            

            pg.time.Clock().tick(60)                                # 控制帧率为60fps，可根据需要调整



