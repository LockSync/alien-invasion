import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """初始化飞船并初始化位置"""

    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        #获取ship图像矩形
        self.rect = self.image.get_rect()
        #get the rect of the screen
        self.screen_rect = self.screen.get_rect()


        #place the ship image rect at the bottom and the center of the screen rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



        #在center之中存储小数
        self.center = float(self.rect.centerx)
        #连续左右移动标志
        self.moving_right = False
        self.moving_left = False

        



    def blitme(self):
        """print the ship on the screen"""
        self.screen.blit(self.image,self.rect)



    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


        #更新centerx位置
        self.rect.centerx = self.center


    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        
        
        
        
        

        

        
