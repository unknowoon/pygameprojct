import pygame
import random
import time
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

rWidth = 1807
rHeight = 1232
Cindex = 4

# map
map_list = [
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]],

[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
[1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]],

[[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]],

[[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
[1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

[[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

[[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
]


def load_image(name):
    image = pygame.image.load(name)
    return image

def toggle_fullscreen():
    global screen
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()

    w, h = screen.get_width(), screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()

    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((w, h), flags ^ FULLSCREEN, bits)
    screen.blit(tmp, (0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0)

    pygame.mouse.set_cursor( * cursor )
    return screen

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)


class Enemy(pygame.sprite.Sprite):
    recycle = 0
    up = 0
    down = 0
    left = 0
    right = 0

    def __init__(self):
        super().__init__()
        self.images = []
        self.images.append(load_image('empty.png'))
        self.images.append(load_image("enemy1.png"))
        self.images.append(load_image('enemy2.png'))
        self.images.append(load_image('enemy3.png'))
        self.images.append(load_image('enemy4.png'))

        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.d = random.randint(1, 4)
        self.dx = random.randrange(1,3)
        self.dy = random.randrange(1,3)
        self.fire = random.randint(1, 3)

    def reset_pos(self):
        self.rect.y = random.randrange(0, 170)
        self.rect.x = random.randrange(0, 220)

    def update(self):
        self.recycle = 0
        if self.d == 1:
            self.up += 1
            self.down = 0
            self.left = 0
            self.right = 0

            self.recycle += 1

            self.image = self.images[self.d]

            self.rect.y -= self.dy

            if self.rect.y < 5:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 3
                self.d = 2

            if map_list[Cindex][(self.rect.y+16)//16-1][(self.rect.x+8)//16] == 0:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 3
                self.d = 2


        if self.d == 2:
            self.down += 1
            self.up = 0
            self.left = 0
            self.right = 0

            self.recycle += 1

            self.image = self.images[self.d]

            self.rect.y += self.dy
            if self.rect.y+16 > 170:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 4
                self.d = 1

            if map_list[Cindex][(self.rect.y)//16+1][(self.rect.x+8)//16] == 0:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 4
                self.d = 1


        if self.d == 3:
            self.left += 1
            self.up = 0
            self.down = 0
            self.right = 0

            self.recycle += 1

            self.image = self.images[self.d]

            self.rect.x -= self.dx

            if self.rect.x < 5:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 1
                self.d = 4

            if map_list[Cindex][(self.rect.y+8)//16][(self.rect.x+16)//16-1] == 0:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 1
                self.d = 4


        if self.d == 4:
            self.right += 1
            self.up = 0
            self.down = 0
            self.left = 0

            self.recycle += 1

            self.image = self.images[self.d]

            self.rect.x += self.dx

            if self.rect.x+16 > 220:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 2
                self.d = 3

            if map_list[Cindex][(self.rect.y+8)//16][(self.rect.x)//16+1] == 0:

                if self.recycle > 10:
                    self.recycle = 0
                    self.d = 2
                self.d = 3




    def next_stage(self):
        if score == 50:
            self.reset_pos()

class Player(Enemy):

    up = 0
    down = 0
    left = 0
    right = 0

    def __init__(self):
        super().__init__()
        self.images = []
        self.images.append(load_image('player1.png'))
        self.images.append(load_image('player2.png'))
        self.images.append(load_image('player3.png'))
        self.images.append(load_image('player4.png'))
        self.images.append(load_image('player5.png'))
        self.images.append(load_image('player6.png'))
        self.images.append(load_image('player7.png'))
        self.images.append(load_image('player8.png'))


        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def playerPos(self):
        self.rect.x = 112
        self.rect.y = 78

    def update(self):
        global rWidth
        global rHeight
        global Cindex

        if pygame.key.get_pressed()[pygame.K_UP] == 1:
            self.up += 1
            self.down = 0
            self.left = 0
            self.right = 0

            self.image = self.images[2]

            if self.rect.y < 0:
                rHeight = rHeight - 176
                self.rect.y = 165
                Cindex -= 3
            if map_list[Cindex][(self.rect.y+16)//16-1][(self.rect.x+8)//16] == 1:

                self.rect.y -= 2


        elif pygame.key.get_pressed()[pygame.K_DOWN] == 1:
            self.down += 1
            self.up = 0
            self.left = 0
            self.right = 0

            self.image = self.images[0]

            if self.rect.y+16 > 170:
                rHeight = rHeight + 176
                self.rect.y = 5
                Cindex += 3
            if map_list[Cindex][(self.rect.y)//16+1][(self.rect.x+8)//16] == 1:

                self.rect.y += 2


        elif pygame.key.get_pressed()[pygame.K_LEFT] == 1:
            self.left += 1
            self.up = 0
            self.down = 0
            self.right = 0

            self.image = self.images[1]

            if self.rect.x < 0:
                rWidth = rWidth - 224
                self.rect.x = 220
                Cindex -= 1
            if map_list[Cindex][(self.rect.y+8)//16][(self.rect.x+16)//16-1] == 1:

                self.rect.x -= 2

        elif pygame.key.get_pressed()[pygame.K_RIGHT] == 1:
            self.right += 1
            self.up = 0
            self.down = 0
            self.left = 0

            self.image = self.images[3]

            if self.rect.x > 200:
                rWidth = rWidth + 224
                Cindex += 1
                self.rect.x = 5

            if map_list[Cindex][(self.rect.y+8)//16][(self.rect.x)//16+1] == 1:

                self.rect.x += 2


        if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
            if len(sword_list) < 2:
                sword_creation = sword(self.up, self.down, self.left, self.right)
                sword_creation.rect.x = player.rect.x + 7
                sword_creation.rect.y = player.rect.y + 4
                sword_list.add(sword_creation)
                all_sprites_list.add(sword_creation)
                if self.up:
                    self.image = self.images[6]
                elif self.down:
                    self.image = self.images[4]
                elif self.left:
                    self.image = self.images[5]
                elif self.right:
                    self.image = self.images[7]


class arrow(Enemy):
    def __init__(self, up, down, left, right):
        super().__init__()
        self.images = []
        self.images.append(load_image("arrow1.png"))
        self.images.append(load_image('arrow2.png'))
        self.images.append(load_image('arrow3.png'))
        self.images.append(load_image('arrow4.png'))


        self.rect = self.image.get_rect()

        self.dx = random.randint(1, 5)

        self.up = up
        self.down = down
        self.right = right
        self.left = left

    def update(self):
        if self.up:
            self.image = self.images[2]
            self.rect.y -= 5
        elif self.down:
            self.image = self.images[0]
            self.rect.y += 5
        elif self.left:
            self.image = self.images[1]
            self.rect.x -= 5
        elif self.right:
            self.image = self.images[3]
            self.rect.x += 5
        else:
            self.rect.y -= 5
        if self.rect.y < -10 or self.rect.x < -10 or self.rect.x > 234 or self.rect.y > 186:
            self.kill()



class sword(Enemy):
    def __init__(self, up, down, left, right):
        super().__init__()
        self.images = []
        self.images.append(load_image("sword1.png"))
        self.images.append(load_image('sword2.png'))
        self.images.append(load_image('sword3.png'))
        self.images.append(load_image('sword4.png'))


        self.rect = self.image.get_rect()

        self.dx = random.randint(1, 5)

        self.up = up
        self.down = down
        self.right = right
        self.left = left

    def update(self):
        if self.up:
            self.image = self.images[2]
            self.rect.y -= 4
        elif self.down:
            self.image = self.images[0]
            self.rect.y += 4
        elif self.left:
            self.image = self.images[1]
            self.rect.x -= 4
        elif self.right:
            self.image = self.images[3]
            self.rect.x += 4
        else:
            self.rect.y -= 4
        if self.rect.y < -10 or self.rect.x < -10 or self.rect.x > 234 or self.rect.y > 186:
            self.kill()

class fireburn(pygame.sprite.Sprite):
    def __init__(self, posx, posy, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.count = 0
        self.changecolor = [(233, 22, 123), (123, 23, 234), (0, 255, 0), (0, 0, 255)]

    def update(self):
        self.count += 1
        if self.count % 30 == 0:
            self.kill()
        if self.count % 10 == 0:
            self.image.fill(self.changecolor[self.count // 10])





pygame.init()
# x = 7, y = 8
screen_width = 224
screen_height = 176
screen = pygame.display.set_mode([screen_width, screen_height])

#sound = pygame.mixer.Sound('bomb.ogg')

player_list = pygame.sprite.Group()
sword_list = pygame.sprite.Group()
arrow_list = pygame.sprite.Group()
fire_burn_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


for i in range(5):
    enemy = Enemy()
    enemy.reset_pos()
    print(map_list[Cindex][(enemy.rect.y)//16][(enemy.rect.x)//16])
    for jj in range(100):
        if map_list[Cindex][(enemy.rect.y)//16][(enemy.rect.x)//16] == 0:
            enemy.reset_pos()
        else:
            continue

    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

player = Player()
player.playerPos()
player_list.add(player)
all_sprites_list.add(player)

clock = pygame.time.Clock()
score = 0

snd_stage = pygame.mixer.Sound("zelda.wav")
snd_stage.play(-1)
_quit = False
while not _quit:

    for e in pygame.event.get():
        if (e.type is KEYDOWN and e.key == K_RETURN):
            toggle_fullscreen()
        if e.type is QUIT:
            _quit = True
        if e.type is KEYDOWN and e.key == K_ESCAPE:
            _quit = True

    background = load_image('overworld.png')


    rRange = pygame.Rect(rWidth, rHeight, 224, 176)


    screen.blit(background, (0, 0), rRange)


    #enemy_hit_list = pygame.sprite.groupcollide(player_list, enemy_list, False, False)
    sword_hit_list = pygame.sprite.groupcollide(enemy_list, sword_list, True, True)
    all_sprites_list.update()

    for sword in sword_hit_list:
        score += 1
        print(score)

    #for enemy in enemy_hit_list:
        #score += 1
        #print(score)
        #sound.play()

        #fire_burn_list.add(fireburn(enemy.rect.x, enemy.rect.y, (255, 0, 0), 40, 40))
        #all_sprites_list.add(fireburn(enemy.rect.x, enemy.rect.y, (255, 0, 0), 40, 40))

        # message_display("You lose")
        # pygame.quit()
        #break
    sword_hit_list = pygame.sprite.groupcollide(enemy_list, sword_list, True, True)

    for hit1, hit2 in sword_hit_list.items():
        score += 1

        fire_burn_list.add(fireburn(hit1.rect.x, hit1.rect.y, (255, 0, 0), 40, 40))
        all_sprites_list.add(fireburn(hit1.rect.x, hit1.rect.y, (255, 0, 0), 40, 40))

    all_sprites_list.draw(screen)

    clock.tick(30)
    pygame.display.flip()
