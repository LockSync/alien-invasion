import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

        """子弹类"""

        def __init__(self,ai_settings,screen,ship):
            super(Bullet,self).__init__()
            self.screen = screen
            #创建一个子弹矩形
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

            #设置子弹的位置，从飞船发射
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor

            self.y = float(self.rect.y)


        def update(self):
            """向上移动子弹"""

            #更新表示位置的小数值
            self.y -= self.speed_factor

            #更新表示子弹的rect位置
            self.rect.y = self.y



        def draw_bullet(self):

            """在屏幕上绘制子弹"""
            pygame.draw.rect(self.screen,self.color,self.rect)
            

            
