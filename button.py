import pygame.font

class Button():
    """带标签的实心矩形"""
    def __init__(self,ai_settings,screen,msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()


        #设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.botton_color = (0,255,0)
        self.text_color =(255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #创建按钮rect矩形，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将mg渲染为图像，并使其在按钮上居中"""
        #True开启反锯齿功能，让文本边缘更顺滑
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.botton_color)
        
        #文本图像在按钮上居中
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    

    def draw_button(self):
        #绘制一个用颜色填充的按钮
        self.screen.fill(self.botton_color,self.rect)
        #传递图像
        self.screen.blit(self.msg_image,self.msg_image_rect)
