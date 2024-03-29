"""
title: pygame
author: Justin
date: 2019-06-14 09:48
"""


import math
import pygame

# Import a library of functions called 'pygame'


# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

# Set the height and width of the screen
size = (1200, 1300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Set Up")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()




# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 10
def draw_stick_figure(screen, x, y):
    #Here is my work!
#Lenny face!
    #face and eyes
    pygame.draw.ellipse(screen, WHITE, [300 + x, 500 + y, 400, 200])
    pygame.draw.arc(screen, BLACK, [340 + x, 510 + y, 100, 170], ((2 / 3) * PI), ((4 / 3) * PI), 15)
    pygame.draw.arc(screen, BLACK, [560 + x, 510 + y, 100, 170], ((5 / 3) * PI), ((1 / 3) * PI), 15)
    pygame.draw.ellipse(screen, BLACK, [400 + x, 520 + y, 50, 50], 10)
    pygame.draw.ellipse(screen, BLACK, [545 + x, 520 + y, 50, 50], 10)
    #eyebrows
    pygame.draw.arc(screen, BLACK, [365 + x, 510 + y, 150, 100], ((1/4) * PI), ((3/4) * PI), 10)
    pygame.draw.arc(screen, BLACK, [505 + x, 510 + y, 150, 100], ((1 / 4) * PI), ((3 / 4) * PI), 10)
    #nose
    pygame.draw.line(screen, BLACK, [505 + x, 540 + y], [505 + x, 580 + y], 15)
    pygame.draw.arc(screen, BLACK, [480 + x, 575 + y, 50, 60], PI, ((1 / 2) * PI), 10)
    #mouth
    pygame.draw.arc(screen, BLACK, [450 + x, 610 + y, 110, 65], PI, (2 * PI), 10)
#Body!
    #torso
    pygame.draw.line(screen, WHITE, [505 + x, 700 + y], [505 + x, 1010 + y], 20)
    #Legs
        #Right
    pygame.draw.arc(screen, WHITE, [400 + x, 1000 + y, 200, 500], ((2) * PI), ((1 / 2) * PI), 20)
        #Left
    pygame.draw.arc(screen, WHITE, [400 + x, 1000 + y, 200, 500], ((1 / 2) * PI), PI, 20)
    #Arms
        #Right
    pygame.draw.arc(screen, WHITE, [300 + x, 700 + y, 400, 300], ((7 / 4) * PI), ((1 / 2) * PI), 20)
        #Left
    pygame.draw.arc(screen, WHITE, [300 + x, 700 + y, 400, 300], ((1 / 2) * PI), ((5/4) * PI), 20)
    #Ball!
    pygame.draw.ellipse(screen, RED, [320 + x, 920 + ball_pos + y, 50, 50])
    
# Loop as long as done == False
while not done:
    ball_pos += ball_change
    if ball_pos > 280:
        ball_change -= 10
    elif ball_pos < 1:
        ball_change -= -10
    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -30
    if keys[pygame.K_RIGHT]:
        x_speed = 30
    if keys[pygame.K_UP]:
        y_speed = -30
    if keys[pygame.K_DOWN]:
        y_speed = 30
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    draw_stick_figure(screen, x_coord, y_coord)





    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("I'm a baller.", True, WHITE)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
Collapse