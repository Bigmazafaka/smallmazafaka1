from pygame import *
from random import randint
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.Font(None, 80)
win = font1.render('Player 1 LOSE!', True, (255, 255, 255))
lose = font1.render('Player 2 LOSE!', True, (180, 0, 0))
 
font2 = font.Font(None, 36)
#нам нужны такие картинки:
img_back = "jopa.jpg" #фон игры
img_ball = "sluna.jpg"
img_rocket1 = 'negr1.png'
img_rocket2 = "negr2.png"
 
score = 0 #сбито кораблей
lost = 0 #пропущено кораблей
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
          self.rect.y -= self.speed 
       if keys[K_s] and self.rect.y < win_height - 80:
          self.rect.y += self.speed 

  
#создаём окошко
win_width = 700
win_height = 500
display.set_caption("Pingo-bingo")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
rocket1 = Player(img_rocket1, 5, win_height - 100, 50, 20, 100)
rocket2 = Player(img_rocket2, 600 ,win_height - 100, 50, 20, 100)
ball = GameSprite(img_ball,50,win_height - 400, 50, 30, 30)
#создание группы спрайтов-врагов
#создание группы спрайтов-астероидов ()
 
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
rel_time = False #флаг, отвечающий за перезарядку
num_fire = 0  #переменная для подсчёта выстрелов         
 
while run:
   #событие нажатия на кнопку “Закрыть”
   for e in event.get():
       if e.type == QUIT:
           run = False
        
   #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if finish != True:
       #обновляем фон
       window.blit(background,(0,0))
 
       #производим движения спрайтов
       rocket1.update_l()
       rocket2.update_r()
       ball.rect.x += speed_x
       ball.rect.y += speed_y
       #обновляем их в новом местоположении при каждой итерации цикла
       ball.reset()
       rocket1.reset()
       rocket2.reset()

       if ball.rect.y > win_height-10 or ball.rect.y < 0:
           speed_y *= -1
       if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
           speed_x*=-1 
           ball.speed += 100
       if ball.rect.x < -20:
           finish = True
           window.blit(lose, (200, 200))
       if ball.rect.x > win_width:
           finish = True
           window.blit(win, (200,200))

       #пишем текст на экран
       display.update()
       time.delay(30)