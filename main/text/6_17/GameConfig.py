import os

WIDTH = 480
HEIGHT =852
SCREEN_SIZE = (WIDTH,HEIGHT)



CURRENT_FILE_PATH = os.path.abspath(__file__)      # 当前文件路径
CURRENT_DIR = os.path.dirname(CURRENT_FILE_PATH)   # 获取当前文件所在的目录


BACKGROUND_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "background.png") # 构造背景图片的相对路径
ICON_IMAGE = os.path.join(CURRENT_DIR, "..", "images", "icon.png") #标题图标


PLANE1_IMG = os.path.join(CURRENT_DIR, "..", "images", "hero1.png")
PLANE2_IMG = os.path.join(CURRENT_DIR, "..", "images", "hero2.png")

# try:
#     with open(BACKGROUND_IMAGE, 'rb') as f:
#         print("Background image opened successfully.")
# except FileNotFoundError as e:
#     print(f"Error: {e}")