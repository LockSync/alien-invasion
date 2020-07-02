import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    """初始化游戏创建屏幕对象"""

    pygame.init()
    ai_settings = Settings()
    
    #初始化背景设置
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏统计信息的类
    stats = GameStats(ai_settings)

    #创建记分牌
    sb = ScoreBoard(ai_settings,screen,stats)
    
    ship = Ship(ai_settings,screen)
    #创建子弹编组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    
    #主循环
    while True:
        """任何情况下都需要调用check_events函数，比如需要知道
            玩家是否按了Q键退出游戏，还需要不断更新屏幕，等待玩家是否选择开始新游戏
            时刷新屏幕

            其他函数仅在游戏处于非活动状态时才需要调用，
            因为非活动状态时不需要更新元素的位置


        """
        
        #键盘监听事件
        gf.check_events(ai_settings,screen,stats,play_button,sb,ship,aliens,
                      bullets)
        #游戏开始状态
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)

        #刷新屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,
                        bullets,play_button)
        
run_game()










        
