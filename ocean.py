import pygame
import random
import webbrowser

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ocean Pollution')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

TURTLE_IMAGE = pygame.image.load('/Users/evatyagi/Downloads/turtle.png')
TURTLE = pygame.transform.scale(TURTLE_IMAGE, (135, 100))

OCEAN_IMAGE = pygame.image.load('/Users/evatyagi/Downloads/ocean_bg.jpeg')
OCEAN = pygame.transform.scale(OCEAN_IMAGE, (WIDTH, HEIGHT))

PLASTIC_IMAGE = pygame.image.load('/Users/evatyagi/Downloads/plastic.png')
PLASTIC = pygame.transform.scale(PLASTIC_IMAGE, (120, 80))

ocean_x = 0
ocean_x2 = OCEAN.get_width()

obstacles = []

font = pygame.font.SysFont("comicsansms", 40)

pygame.time.set_timer(pygame.USEREVENT+1, 500) # to increase speed

def handle_movement(keys_pressed, turtle):
    if keys_pressed[pygame.K_UP] and turtle.y - 50 > 0: # up
        turtle.y -= 5

    if keys_pressed[pygame.K_DOWN] and turtle.y + turtle.height < HEIGHT - 5: # down
        turtle.y += 5


def losing():

    message = font.render("You ran out of lives!", 1, RED)
    message2 = font.render("Unfortunately, real turtles only have one.", 1, RED)
    message3 =  font.render("Help save them by reducing ocean pollution.", 1, RED)

    WIN.blit(message, (WIDTH / 2 - message.get_width() / 2, 100))
    WIN.blit(message2, (WIDTH / 2 - message2.get_width() / 2, 250))
    WIN.blit(message3, (WIDTH / 2 - message3.get_width() / 2, 400))

    pygame.display.update()

def main():

    global ocean_x, ocean_x2

    speed = 70

    turtle = pygame.Rect(40, HEIGHT/2, 135, 100)

    clock = pygame.time.Clock()
    run = True

    global lives

    lives = 3

    plastic_x = OCEAN.get_width()
    plastic_y = random.randrange(50, 200)

    plastic_x2 = 1000
    plastic_y2 = random.randrange(200, 350)

    plastic_x3 = 1100
    plastic_y3 = random.randrange(350, 500) 

    plastic = pygame.Rect(plastic_x, plastic_y, 120, 80)
    plastic2 = pygame.Rect(plastic_x2, plastic_y2, 120, 80)
    plastic3 = pygame.Rect(plastic_x3, plastic_y3, 120, 80)

    while run:
                
        WIN.blit(OCEAN, (ocean_x, 0))
        WIN.blit(OCEAN, (ocean_x2, 0))

        WIN.blit(TURTLE, (turtle.x, turtle.y))
        
        WIN.blit(PLASTIC, (plastic.x, plastic.y))
        WIN.blit(PLASTIC, (plastic2.x, plastic2.y))
        WIN.blit(PLASTIC, (plastic3.x, plastic3.y))

        life = font.render("Lives: " + str(lives), True, BLACK)
        WIN.blit(life, (10, 10))
        pygame.display.update()


        ocean_x -= 1.4
        ocean_x2 -= 1.4

        plastic.x -= 1.4
        plastic2.x -= 1.4
        plastic3.x -= 1.4

        if ocean_x < OCEAN.get_width() * -1:
            ocean_x = OCEAN.get_width()
    
        if ocean_x2 < OCEAN.get_width() * -1:
            ocean_x2 = OCEAN.get_width()

        if plastic.x < 0:
            plastic.x = OCEAN.get_width()
            plastic.y = random.randrange(50, 200)

        if plastic2.x < 0:
            plastic2.x = 1000
            plastic2.y = random.randrange(200, 350)

        if plastic3.x < 0:
            plastic3.x= 1100
            plastic3.y = random.randrange(350, 500)

        if turtle.colliderect(plastic):
            plastic.x = 0
            lives -=1 

        if turtle.colliderect(plastic2):
            plastic2.x = 0
            lives -=1 

        if turtle.colliderect(plastic3):
            plastic3.x = 0
            lives -=1 

        if lives == 0:

            WIN.blit(life, (10, 10))
            pygame.display.update()
            
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT+1:
                speed += 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    turtle.y += -15
                elif event.key == pygame.K_DOWN:
                    turtle.y += 15

        clock.tick(speed)  

        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, turtle)

    losing()

    pygame.time.delay(8000)

    pygame.quit()

if __name__ == "__main__":
    main()