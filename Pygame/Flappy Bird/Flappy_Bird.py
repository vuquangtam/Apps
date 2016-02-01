""" 
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame, random

# Define some colors as global constants
WINDOW_WIDTH = 288
WINDOW_HEIGHT = 511

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)


class SpriteSheet():
    """ Class used to grab images out of a sprite sheet. """    
    # This points to our sprite sheet image
    sprite_sheet = None
    
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        
        # Load the sprite sheet. 
        self.sprite_sheet = pygame.image.load(file_name)    
        
                
    def getImage(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        
        # Create a new blank image
        image = pygame.Surface([width, height]).convert() 
        
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height) )
        
        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)    
        
        # Return the image
        return image
    
class Bird(pygame.sprite.Sprite):
    clock = None
    
    def __init__(self, x, y, sprite):

        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # sprite is tuple of bird's sprites
        self.sprite = sprite

        self.cycleTime = 0
        
        self.birdNum = 0
        
        self.image = self.sprite[self.birdNum]

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.dy = 0
        self.angle = 0
        self.dAngle = 0
        
    def update(self):
        self.gravity()
        self.changeSprite()

    def gravity(self):
        self.dy += 1
        self.dAngle += 0.3
        self.angle -= self.dAngle
        self.angle = max(self.angle, -90)
        self.rect.y += self.dy

        
    def changeSprite(self):
        self.cycleTime += self.clock.get_time() * 0.001
        if self.cycleTime > 0.1:
            if self.dy > 10:
                self.image = pygame.transform.rotate(self.sprite[self.birdNum], self.angle)
            else:
                self.image = self.sprite[self.birdNum]
            self.cycleTime = 0
            self.birdNum = (self.birdNum + 1) % len(self.sprite)

    def jump(self):
        self.dy = 0
        self.angle = 0
        self.dAngle = 0
        self.rect.y -= 50

    def gameOver(self):
        if self.rect.y > WINDOW_HEIGHT - 112:
            self.dy = 0
            self.rect.y = WINDOW_HEIGHT - 112
        else:
            self.gravity()
            self.changeSprite()



class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)
        self.flagScore = True
        self.dx = 5

    def update(self):
        self.rect.x -= self.dx

    def stop(self):
        self.dx = 0
            
class TopPipe(Pipe):
    
    def __init__(self, sprite, height, xstart = WINDOW_WIDTH):
        # Sprite constructor
        Pipe.__init__(self)

        self.image = sprite.subsurface(0, 320 - height, 52, height)

        self.rect = self.image.get_rect()

        self.rect.x = xstart
        self.rect.y = 0

class BottomPipe(Pipe):
    
    def __init__(self, sprite, height, xstart = WINDOW_WIDTH):
        # Sprite constructor
        Pipe.__init__(self)

        self.image = sprite.subsurface(0, 0, 52, height)

        self.rect = self.image.get_rect()

        self.rect.x = xstart
        self.rect.y = WINDOW_HEIGHT - 112 - height

class Land(pygame.sprite.Sprite):
    def __init__(self, sprite):

        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = sprite

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = WINDOW_HEIGHT - 112
        
def main():
    """ Main function for the game. """
    pygame.init()
     
    # Set the width and height of the screen [width,height]
    size = [WINDOW_WIDTH, WINDOW_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #Loop until the user clicks the close button.
    done = False
    
    #Load all sprite
    all_sprite = SpriteSheet('Flappy-Graphics.png')
    day_sprite = all_sprite.getImage(0, 0, 288, 511)
    night_sprite = all_sprite.getImage(288 + 4, 0, 288, 511)
    land_sprite = all_sprite.getImage(288 + 288 + 4 + 4, 0, 288, 112)
    bird_sprite = (all_sprite.getImage(225, 645, 40, 40), all_sprite.getImage(225, 697, 40, 40),all_sprite.getImage(169, 969, 40, 40))
    green_pipe_top_sprite = all_sprite.getImage(112, 646, 52, 320)
    green_pipe_bottom_sprite = all_sprite.getImage(112 + 52 + 4, 646, 52, 320)

    #Create objects
    bird = Bird(70, 150, bird_sprite)
    bird.clock = clock 

    land = Land(land_sprite)
    #Create object's group
    
    all_pipe = pygame.sprite.Group() #Group of pipes
    
    all_object = pygame.sprite.Group() #Group of all object in game
    all_object.add(land)
    all_object.add(bird)
    for x in range(WINDOW_WIDTH * 4 , WINDOW_WIDTH * 3, -WINDOW_WIDTH // 2):
        height_top = random.randint(60, (WINDOW_HEIGHT - 112) // 2)
        height_bottom = (WINDOW_HEIGHT - 112) // 1.5 - height_top
        topPipe = TopPipe(green_pipe_top_sprite, height_top,x)
        bottomPipe = BottomPipe(green_pipe_bottom_sprite,height_bottom, x)
        all_object.add(topPipe)
        all_object.add(bottomPipe)
        all_pipe.add(topPipe)
        all_pipe.add(bottomPipe)
    score = 0
    stop = True
    # -------- Main Program Loop -----------
    while not done:

        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                bird.jump()
        if bird.rect.y > WINDOW_HEIGHT - 112 - 60:
            done = True
        if len(pygame.sprite.spritecollide(bird, all_pipe, False)):
            done = True
            
        for pipe in all_pipe:
            if pipe.flagScore and pipe.rect.x < 70 - 40 and isinstance(pipe, TopPipe):
                pipe.flagScore = False
                score += 1
                print score
            if pipe.rect.x < 0:
                all_pipe.remove(pipe)
            if pipe.rect.x < -52:
                pipe.kill()

        if len(all_pipe) < 4:
            height_top = random.randint(60, (WINDOW_HEIGHT - 112) // 2)
            height_bottom = (WINDOW_HEIGHT - 112) // 1.5 - height_top
            topPipe = TopPipe(green_pipe_top_sprite, height_top)
            bottomPipe = BottomPipe(green_pipe_bottom_sprite,height_bottom)
            all_object.add(topPipe)
            all_object.add(bottomPipe)
            all_pipe.add(topPipe)
            all_pipe.add(bottomPipe)

        all_object.update() 

        screen.blit(day_sprite, (0, 0))

        all_object.draw(screen)
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 30 frames per second
        clock.tick(30)
        
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == "__main__":
    main()
