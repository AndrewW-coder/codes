import pygame
import random

pygame.init()

white = (255, 255, 255)
gray = (200, 200, 200)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

dis_width = 600
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

dis.fill(white)

clock = pygame.time.Clock()

grid_size = 20

font_style = pygame.font.SysFont("arial", 25)

def score(score):
    value = font_style.render("Score: " + str(score), True, black)
    dis.blit(value, [5, 5]) 

def snake(snake_list):
    for pos in snake_list:
        pygame.draw.rect(dis, green, [pos[0], pos[1], grid_size, grid_size])

def game():
    game_over = False
    game_close = False
    speed = 10

    x = dis_width // grid_size // 2 * grid_size
    y = dis_height // grid_size // 2 * grid_size

    change_x = 0
    change_y = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, dis_width // grid_size) * grid_size
    food_y = random.randrange(0, dis_height // grid_size) * grid_size

    while not game_over:

        while game_close:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.collidepoint(event.pos):
                        pygame.quit()
                        quit()
                    
                    if restart_button.collidepoint(event.pos):
                        game()

            dis.fill(white)

            game_over_text = font_style.render("Game Over! Your Score: " + str(snake_length - 1), True, black)
            dis.blit(game_over_text, [dis_width // 2 - game_over_text.get_width() // 2, dis_height // 2 - 100])

            restart_button = pygame.draw.rect(dis, gray, [dis_width // 2 - 40 - 50, dis_height // 2, 80, 40])
            exit_button = pygame.draw.rect(dis, gray, [dis_width // 2 - 40 + 50, dis_height // 2 , 80, 40])
            
            restart_button_text = font_style.render("Restart", True, black)
            dis.blit(restart_button_text, [restart_button.x + (restart_button.width - restart_button_text.get_width()) / 2, restart_button.y  + (restart_button.height - restart_button_text.get_height()) / 2])
            
            exit_button_text = font_style.render("Exit", True, black)
            dis.blit(exit_button_text, [exit_button.x + (exit_button.width - exit_button_text.get_width()) / 2, exit_button.y  + (exit_button.height - exit_button_text.get_height()) / 2])

            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -grid_size
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = grid_size
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -grid_size
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = grid_size

        x += change_x
        y += change_y
        
        dis.fill(white)

        pygame.draw.rect(dis, red, [food_x, food_y, grid_size, grid_size])

        head = [x, y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        snake(snake_list)
        score(snake_length - 1)
        
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, dis_width // grid_size - 1) * grid_size
            food_y = random.randrange(0, dis_height // grid_size - 1) * grid_size
            speed += 0.1
            snake_length += 1

        clock.tick(speed)

        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

    pygame.quit()
    quit()

game()