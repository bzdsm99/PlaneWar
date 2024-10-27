#GameConfig.py
import os

WIDTH = 480
HEIGHT =852
SCREEN_SIZE = (WIDTH,HEIGHT)
#定义颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

CURRENT_FILE_PATH = os.path.abspath(__file__)      # 当前文件路径
CURRENT_DIR = os.path.dirname(CURRENT_FILE_PATH)   # 获取当前文件所在的目录


BACKGROUND_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "background.png")  #构造背景图片的相对路径
ICON_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "icon.png")              #标题图标

# 飞机大战标题图片
TITLE_IMAGE = "../images/name.png"
# 开始游戏图片
START_IMAGE = "../images/start_nor.png"
# 开始游戏加载动画图片
LOADING_IMAGE1 = "../images/game_loading1.png"
LOADING_IMAGE2 = "../images/game_loading2.png"
LOADING_IMAGE3 = "../images/game_loading3.png"
LOADING_IMAGE4 = "../images/game_loading4.png"

PLANE1_IMG = os.path.join(CURRENT_DIR, "..", "images", "hero1.png")
PLANE2_IMG = os.path.join(CURRENT_DIR, "..", "images", "hero2.png")


# 开始/暂停游戏图片
PAUSE_NOR = "../images/pause_nor.png"
PAUSE_PRESSED = "../images/pause_pressed.png"
RESUME_NOR = "../images/resume_nor.png"
RESUME_PRESSED = "../images/resume_pressed.png"

# 小型敌机图片
SMALL_EMEMY_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "enemy0.png")
# 中型敌机图片
MIDDLE_EMEMY_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "enemy1.png")
# 大型敌机图片
BIG_EMEMY_IMAGE1 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_n1.png")
BIG_EMEMY_IMAGE2 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_n2.png")


# 我方飞机爆炸图片
PLANE_DESTORY_IMAGE1 = os.path.join(CURRENT_DIR, "..", "images", "hero_blowup_n1.png")
PLANE_DESTORY_IMAGE2 = os.path.join(CURRENT_DIR, "..", "images", "hero_blowup_n2.png")
PLANE_DESTORY_IMAGE3 = os.path.join(CURRENT_DIR, "..", "images", "hero_blowup_n3.png")
PLANE_DESTORY_IMAGE4 = os.path.join(CURRENT_DIR, "..", "images", "hero_blowup_n4.png")
# 小型敌机爆炸图片
S_ENEMY_DESTORY_IMAGE1 = os.path.join(CURRENT_DIR, "..", "images", "enemy0_down1.png")
S_ENEMY_DESTORY_IMAGE2 = os.path.join(CURRENT_DIR, "..", "images", "enemy0_down2.png")
S_ENEMY_DESTORY_IMAGE3 = os.path.join(CURRENT_DIR, "..", "images", "enemy0_down3.png")
S_ENEMY_DESTORY_IMAGE4 = os.path.join(CURRENT_DIR, "..", "images", "enemy0_down4.png")
# 中型敌机爆炸图片
M_ENEMY_DESTORY_IMAGE1 = os.path.join(CURRENT_DIR, "..", "images", "enemy1_down1.png")
M_ENEMY_DESTORY_IMAGE2 = os.path.join(CURRENT_DIR, "..", "images", "enemy1_down2.png")
M_ENEMY_DESTORY_IMAGE3 = os.path.join(CURRENT_DIR, "..", "images", "enemy1_down3.png")
M_ENEMY_DESTORY_IMAGE4 = os.path.join(CURRENT_DIR, "..", "images", "enemy1_down4.png")
# 大型敌机爆炸图片
B_ENEMY_DESTORY_IMAGE1 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_down1.png")
B_ENEMY_DESTORY_IMAGE2 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_down2.png")
B_ENEMY_DESTORY_IMAGE3 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_down3.png")
B_ENEMY_DESTORY_IMAGE4 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_down4.png")
B_ENEMY_DESTORY_IMAGE5 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_down5.png")
B_ENEMY_DESTORY_IMAGE6 = os.path.join(CURRENT_DIR, "..", "images", "enemy2_down6.png")

# 普通子弹图片
BUTTLE1_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "bullet1.png")
# 超级子弹图片
BUTTLE2_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "bullet2.png")

# 中型飞机被攻击图片
M_ENEMY_HIT_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "enemy1_hit.png")
# 大型飞机被攻击图片
B_ENEMY_HIT_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "enemy2_hit.png")

# 定义字体
FONT_PATH = os.path.join(CURRENT_DIR, "..", "font", "font.ttf")

# 超级炸弹
BOMB_IMAGE = "../images/bomb.png"

# 补给(超级子弹/超级炸弹)
PROP1_IMAGE = "../images/prop_type_0.png"
PROP2_IMAGE = "../images/prop_type_1.png"

# 普通/超级子弹图片
BUTTLE1_IMAGE = "../images/bullet1.png"
# 超级子弹图片
BUTTLE2_IMAGE = "../images/bullet2.png"

# 我方飞机生命图片
LIFE_IMAGE = "../images/life.png"


# 结束游戏图片
GAMEOVER_IMAGE = "../images/quit_nor.png"
# 重新开始游戏图片
RESTART_IMAGE = "../images/restart_nor.png"

# try:
#     with open(BACKGROUND_IMAGE, 'rb') as f:
#         print("Background image opened successfully.")
# except FileNotFoundError as e:
#     print(f"Error: {e}")