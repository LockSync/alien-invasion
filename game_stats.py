class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings

        #最高分
        """
        在任何情况下都不应重置最高分，所以在init中而不是reset_stats中
        """
        #初始化high_score
        self.high_score = 0
        self.reset_stats()

        #游戏一开始处于非活动状态
        self.game_active = False



    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        #每次开始游戏时都重置得分
        self.score = 0
        #游戏等级
        self.level = 1

        
        
        
