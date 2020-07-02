import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

"""
game_function存储游戏运行的函数,简化游戏主逻辑
"""
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
            
def fire_bullets(ai_settings,screen,ship,bullets):
    """创建子弹，并将其添加到编组中"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)




def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    
    
def check_events(ai_settings,screen,stats,play_button,sb,ship,aliens,
                      bullets):
    """响应按键和鼠标事件"""

    for event in pygame.event.get():
        if event.type == pygame.K_q:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,
                      bullets,mouse_x,mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,
                      bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    """在玩家单击play按钮时开始游戏"""
    if button_clicked and not stats.game_active:
        ai_settings.initial_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(True)
        #每次单击play按钮时重置游戏
        stats.reset_stats()
        stats.game_active = True

        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        #创建新的外星人和飞船并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
            
            



def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """print the screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    
    #重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    """刷新屏幕"""
    aliens.draw(screen)

    #显示得分
    sb.show_score()
    
    #如果游戏处于非活动状态 ，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

        
    #重新刷新屏幕
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

    
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """#检查是否有子弹击中了外星人
    #如果是，删除相应的子弹和外星人
    #collisons返回一个字典，并添加一个键值对 每个子弹是key每个外星人是value
    #两个实参True告诉Pyagme删除发生碰撞的子弹和外星人
    """
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    #检查collisoions字典是否存在
    if collisions:
        """将消失的每一个外星人都计入分数，防止遗漏

            避免：两颗子弹集中一个外星人，或者一颗子弹击中多个外星人，只算一次分
            每个aliens是一个字典

        """
        for aliens in collisions.values():
            #对于每一个列表，把外星人点数 * 其中包含的外星人数量
            stats.score += ai_settings.alien_points * len(aliens)

            """prep_socre方法"""
            sb.prep_score()
            """每当有外星人被消灭，都需要在更新得分后调用check_hih_score方法"""
        check_high_score(stats,sb)
        
    if(len(aliens) == 0):
        #外星人打完，清空子弹
        bullets.empty()
        
        #加快游戏节奏 
        ai_settings.increase_speed()

        #提高等级

        stats.level += 1
        sb.prep_level()
        #创建新外星人群
        create_fleet(ai_settings,screen,ship,aliens)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""

    alien = Alien(ai_settings,screen)
    #get_number_aliens_x方法
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    #get_number_rows方法
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                 alien.rect.height)

    #创建外星人群
    for row_number in range(number_rows):
        for alien_number  in range(number_aliens_x):
            #create_alien方法
           create_alien(ai_settings,screen,aliens,alien_number,row_number)


def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y  =(ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y /(2 * alien_height))
    return number_rows





def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)



def check_fleet_edges(ai_settings,aliens):
    """检测外星人群是否撞到屏幕边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移动,并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置"""
    #对编组调用update方法，将自动对每个外星人调用方法update
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #检测外星人是否和飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)

        
    #检测是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)


def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """碰撞响应"""
    if stats.ships_left > 0 :
        stats.ships_left -= 1

        sb.prep_ships()

        #清空外星人 子弹列表
        aliens.empty()
        bullets.empty()

        #创建新外星人群，把飞船放置在屏幕底部
        create_fleet(ai_settings,screen,ship,aliens)

        ship.center_ship()
        sleep(0.5)

    else:
        #玩家没有飞船剩余，游戏结束
        stats.game_active = False
        pygame.mouse.set_visible(True)
        


def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """检测外星人是否到屏幕底部
        触底调用ship_hit


    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            break

    
    
    
    
def check_high_score(stats,sb):
    """检查是否产生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        
        
        
    

    
    

