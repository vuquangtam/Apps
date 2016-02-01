import pygame, random, os

BLOCK_WIDTH = 40
BLOCK_HEIGHT = 40

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 600
BLOCK_X_MAX = int(WINDOW_WIDTH / BLOCK_WIDTH)
BLOCK_Y_MAX = int(WINDOW_HEIGHT / BLOCK_HEIGHT)

LENGHT_OF_SNAKE = 5
START_POSITION_X = 10
START_POSITION_Y = 10
SNAKE_SPEED = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

folder = "data"
head_sprite = pygame.image.load(os.path.join(folder, "head_sprite.png")).convert_alpha()
head_sprite = pygame.transform.scale(head_sprite, (BLOCK_WIDTH, BLOCK_HEIGHT))
apple_sprite = pygame.image.load(os.path.join(folder, "apple.png")).convert_alpha()
apple_sprite = pygame.transform.scale(apple_sprite, (BLOCK_WIDTH, BLOCK_HEIGHT))
background = pygame.image.load(os.path.join(folder, "background.jpg")).convert()
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))


class Block(pygame.sprite.Sprite):
    previous_part = None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((int(BLOCK_WIDTH), int(BLOCK_HEIGHT))).convert()
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, YELLOW, (BLOCK_WIDTH // 2, BLOCK_HEIGHT // 2), BLOCK_WIDTH // 2, 0)

        self.rect = self.image.get_rect()
        self.oldx = self.rect.x
        self.oldy = self.rect.y

    def update(self):
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        self.rect.x, self.rect.y = self.previous_part.oldpos() 

    def oldpos(self):
        return self.oldx, self.oldy

class Head(Block):
    def __init__(self):
        Block.__init__(self)

        self.image = pygame.Surface((int(BLOCK_WIDTH), int(BLOCK_HEIGHT)))
        self.image.blit(head_sprite, (0, 0))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
                                
        self.dx = SNAKE_SPEED
        self.dy = 0
    def update(self):
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.dx = 0
            if self.dy != SNAKE_SPEED:
                self.dy = -SNAKE_SPEED
        elif key[pygame.K_DOWN]:
            self.dx = 0
            if self.dy != -SNAKE_SPEED:
                self.dy = SNAKE_SPEED
        elif key[pygame.K_LEFT]:
            self.dy = 0
            if self.dx != SNAKE_SPEED:
                self.dx = -SNAKE_SPEED
        elif key[pygame.K_RIGHT]:    
            self.dy = 0
            if self.dx != -SNAKE_SPEED:
                self.dx = SNAKE_SPEED
        self.rect.x += int(self.dx) * BLOCK_WIDTH
        self.rect.y += int(self.dy) * BLOCK_HEIGHT

class Apple(pygame.sprite.Sprite):
    def __init__(self, headOfSnake):
        pygame.sprite.Sprite.__init__(self)

        self.headOfSnake = headOfSnake
        
        self.image = pygame.Surface((int(BLOCK_WIDTH), int(BLOCK_HEIGHT))).convert()
        self.image.blit(apple_sprite, (0, 0))
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x, self.rect.y = random.randint(1, BLOCK_X_MAX - 1), random.randint(1, BLOCK_Y_MAX - 1)
        self.rect.x *= BLOCK_WIDTH
        self.rect.y *= BLOCK_HEIGHT

    def update(self):
        return self.rect.x == self.headOfSnake.rect.x and self.rect.y == self.headOfSnake.rect.y

def drawLine(screen):
    for x in range(0, WINDOW_WIDTH, BLOCK_WIDTH):
        pygame.draw.line(screen, WHITE,(x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, BLOCK_HEIGHT):
        pygame.draw.line(screen, WHITE,(0, y), (WINDOW_WIDTH, y))
def getText(text, color):
    font = pygame.font.SysFont(None, 50)
    textSurf = font.render(text, 1, color)
    return textSurf
        
clock = pygame.time.Clock()

level = 8

snake = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()
snake_list = []

head = Head()
head.rect.x = (START_POSITION_X + LENGHT_OF_SNAKE) * BLOCK_WIDTH
head.rect.y = START_POSITION_Y * BLOCK_HEIGHT
all_sprite.add(head)
previous = head
snake_list.append(head)
apple = Apple(head)
for x in range(START_POSITION_X + LENGHT_OF_SNAKE - 1, START_POSITION_X, -1):
    block = Block()
    block.rect.x = x * BLOCK_WIDTH
    block.rect.y = START_POSITION_Y * BLOCK_HEIGHT
    block.previous_part = previous
    previous = block
    snake.add(block)
    all_sprite.add(block)
    snake_list.append(block)
all_sprite.add(apple)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for block in snake_list:
        block.update()
    if apple.update():
        apple.reset()
        tail = snake_list[-1]
        block = Block()
        block.previous_part = tail
        block.update()
        snake.add(block)
        all_sprite.add(block)
        snake_list.append(block)
        print len(snake_list)
    if len(pygame.sprite.spritecollide(head, snake, False)):
        pygame.quit()
    if head.rect.x < 0 : head.rect.x = BLOCK_X_MAX * BLOCK_WIDTH
    elif head.rect.x > BLOCK_X_MAX * BLOCK_WIDTH : head.rect.x = 0
    
    if head.rect.y < 0 : head.rect.y = BLOCK_Y_MAX * BLOCK_HEIGHT
    elif head.rect.y > BLOCK_Y_MAX * BLOCK_HEIGHT : head.rect.y = 0
       
    screen.blit(background, (0,0))
    drawLine(screen)
    all_sprite.draw(screen)
    screen.blit(getText('Score : %s'%(len(snake_list) - LENGHT_OF_SNAKE), BLUE), (10, 10))
    pygame.display.flip()
    clock.tick(level)
    

    
