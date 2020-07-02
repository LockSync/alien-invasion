class Settings():
    """游戏设置雷"""

    def __init__(self):

        """初始化游戏类"""

        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)


        """玩家命"""
        self.ship_limit = 3

        """子弹设置"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        
    
        #外星人垂直移动速度
        self.fleet_drop_speed = 10


        #加快游戏节奏的参数
        self.speedup_scale = 1.1

        #外星人点数的提高速度
        self.score_scale = 1.5

        

        #初始化飞船 子弹 外星人的横向移动速度
        self.initial_dynamic_settings()

    def initial_dynamic_settings(self):
        """初始化随游戏进行而变化的设置：飞船 子弹 外星人移动速度"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
         #外星人垂直移动速度
        self.fleet_drop_speed = 10

        #飞船群的移动方向 1表示向右 -1表示向左
        self.fleet_direction = 1

        #击落一个外星人的得分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        
        
        
        
        
        
        



        


        


        



        
        
        
        
