import pygame
import random
import math
from pygame import mixer


# classes
class Player(object):
    def __init__(self, image, X, Y) -> None:
        self.image = image
        self.X = X
        self.Y = Y
    
    def get_image(self):
        return self.image
    
    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y
    
    def move_right(self):
        self.X += 1.7
    
    def move_left(self):
        self.X -= 1.7

    def restrict_movement(self):
        if self.X <= 16:
            self.X = 16
        elif self.X >= 750:
            self.X = 750


class Invader(object):
    def __init__(self, image, X, Y, direction):
        self.image = image
        self.X = X
        self.Y = Y
        self.direction = direction

    def get_image(self):
        return self.image

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def move_X(self):
        self.X += 1.2 * self.direction

    def finished_line(self):
        if self.X >= 735 or self.X <= 0:
            finished = True
        else:
            finished = False
        return finished

    def change_direction(self):
        self.direction *= -1

    def move_down(self):
        self.Y += 50

    def let_X(self, X):
        self.X = X

    def let_Y(self, Y):
        self.Y = Y


class Bullet(object):
    def __init__(self, image, X, Y, state) -> None:
        self.image = image
        self.X = X
        self.Y = Y
        self.state = state

    def get_image(self):
        return self.image

    def get_X(self) -> int:
        return self.X

    def get_Y(self) -> int:
        return self.Y

    def get_state(self) -> str:
        return self.state

    def let_state(self, state) -> None:
        self.state = state

    def let_X(self, X):
        self.X = X

    def get_position(self) -> tuple(int, int):
        return self.X, self.Y

    def set_rest(self):
        self.Y = 600
        self.state = "rest"

    def move(self):
        self.Y -= 3



# game over logic
def show_score(x, y):
    score = font.render("Points: " + str(score_val), True, (255,255,255))
    screen.blit(score, (x , y ))


def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_text, (190, 250))


# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False




# game loop
if __name__ == "__main__":
    # initializing pygame
    pygame.init()

    # creating screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # caption and icon
    pygame.display.set_caption("Welcome to Space Invaders Game by:- styles")


    # Score
    score_val = 0
    scoreX = 5
    scoreY = 5
    font = pygame.font.Font('freesansbold.ttf', 20)

    # Game Over
    game_over_font = pygame.font.Font('freesansbold.ttf', 64)




    # Background Sound
    mixer.music.load('data/background.wav')
    mixer.music.play(-1)


    # player

    playerImage = pygame.image.load('data/spaceship.png')
    player_X = 370
    player_Y = 523
    player_Xchange = 0

    player = Player(playerImage, player_X, player_Y)    


    # Invader
    no_of_invaders = 8
    invaders = []
    for num in range(no_of_invaders):

        invaderImage = pygame.image.load('data/alien.png')
        invader_X = random.randint(64, 737)
        invader_Y = random.randint(30, 180)

        invaders.append(Invader(invaderImage, invader_X, invader_Y))


    # Bullet
    # rest - bullet is not moving
    # fire - bullet is moving
    bulletImage = pygame.image.load('data/bullet.png')
    bullet_X = 0
    bullet_Y = 500
    bullet_Xchange = 0
    bullet_Ychange = 3
    bullet_state = "rest"

    bullet = Bullet(bulletImage, bullet_X, bullet_Y, bullet_state)



    running = True
    while running:

        # RGB
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Controling the player movement from the arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_SPACE:
                    # Fixing the change of direction of bullet
                    if bullet.get_state() is "rest":
                        bullet.let_X(player.get_X())
                        x, y = bullet.get_position()
                        screen.blit(bullet.get_image(), (x, y))
                        bullet_sound = mixer.Sound('data/bullet.wav')
                        bullet_sound.play()
                        bullet.let_state("fire")
            if event.type == pygame.KEYUP:
                pass

        # adding the change in the player position
        for i in range(no_of_invaders):
            invaders[i].move_X()

        # bullet movement
        if bullet.get_Y <= 0:
            bullet.set_rest()

        if bullet.get_state is "fire":
            x, y = bullet.get_position()
            screen.blit(bullet.get_image(), (x, y))
            bullet.move()

        # movement of the invader
        for invader in invaders:
            
            if invader.get_Y() >= 450:
                if abs(player.get_X() - invader.get_X()) < 80:
                    for invader_ in invaders:
                        invader_.let_Y(2000)
                        explosion_sound = mixer.Sound('data/explosion.wav')
                        explosion_sound.play()
                    game_over()
                    break

            if invader.finished_line():
                invader.change_direction()
                invader.move_down()
            # Collision
            collision = isCollision(bullet.get_X(), invader.get_X(), bullet.get_Y(), invader.get_Y())
            if collision:
                score_val += 1
                bullet.let_Y(600)
                bullet.let_state("rest")
                invader.let_X(random.randint(64, 736))
                invader.let_Y(random.randint(30, 200))
                invader.change_direction()

            screen.blit(invader.get_image(), (x, y))


        # restricting the spaceship so that it doesn't go out of screen
        player.restrict_movement()


        screen.blit(player.get_image(), (player.get_X() - 16, player.get_Y() + 10))
        show_score(scoreX, scoreY)
        pygame.display.update()

