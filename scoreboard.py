import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    """显示得分的类"""

    """显示最高得分,等级 和余下的飞船数"""

    def __init__(self,ai_settings,screen,stats):
        """初始化涉及得分的属性"""

        self.ai_settings = ai_settings
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()

        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分图像
        self.prep_score()

        #准备最高得分图像
        self.prep_high_score()

        self.prep_level()

        self.prep_ships()

    def prep_score(self):
        """将得分转换为渲染的图像"""
        #第二个实参为负数，round元整到最近的10,100,1000整数倍
        rounded_score = int(round(self.stats.score,-1))

        #初始得分在stats中设置为0
        #把数值转换为字符串时在其中插入逗号
        """{:2f}.format(3.1489221)

            ----》3.14
        """ 
        score_str = "yours: "+"{:,}".format(rounded_score)
        #True开启反锯齿 设置文本 背景颜色
        self.score_image = self.font.render(score_str,True,self.text_color,
                                            self.ai_settings.bg_color)

        #将得分显示在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        #右边 和上部 各20像素
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        

    def prep_high_score(self):
        """把最高得分渲染为图像"""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "highest: " + "{:,}".format(high_score) 
        self.high_score_image = self.font.render(high_score_str,True,
                                                 self.text_color,self.ai_settings.bg_color)

        #把最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def prep_level(self):
        """将等级转化为渲染图象"""
        self.level_image = self.font.render('level: '+str(self.stats.level),True,
                                            self.text_color,self.ai_settings.bg_color)

        #把等级放置在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.bottom = self.score_rect.bottom + 30
        
        
        

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #绘制玩家剩余生命数
        self.ships.draw(self.screen)
        



    def prep_ships(self):
        """用飞船个数显示玩家剩余的生命"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
        
        
