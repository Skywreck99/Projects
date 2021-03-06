import pygame, sys, random

pygame.init()                                   # Initialize the game
screen = pygame.display.set_mode((576,1024))    # Set the screen size
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.ttf",40)

bg_surface = pygame.image.load("assets/sprites/background-night.png").convert()         # Set up the background
bg_surface = pygame.transform.scale2x(bg_surface)                                       # Scale the background twice

floor_surface = pygame.image.load("assets/sprites/base.png").convert()                  # Set up the floor
floor_surface = pygame.transform.scale2x(floor_surface)                                 # Scale the floor twice
floor_x = 0                                                                             # x-coordinate of the floor

bird_downflap = pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-downflap.png").convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-midflap.png").convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-upflap.png").convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

pipe_surface = pygame.image.load("assets/sprites/pipe-red.png").convert()               # Set up the pipes
pipe_surface = pygame.transform.scale2x(pipe_surface)                                   # Scale the pipes twice
pipe_list = []
SPAWNPIPE = pygame.USEREVENT                                                            # Set up spawned pipes in respect to the user event
pygame.time.set_timer(SPAWNPIPE, 1200)                                                  # Set timer in milliseconds
pipe_height = [400, 600, 800] 

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288, 512))

flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
death_sound = pygame.mixer.Sound('assets/audio/hit.wav')
score_sound = pygame.mixer.Sound('assets/audio/point.wav')
fell_sound = pygame.mixer.Sound('assets/audio/die.wav')
swoosh_sound = pygame.mixer.Sound('assets/audio/swoosh.wav')

# Game Variables
gravity = 0.25      # Arbitrary number
bird_movement = 0
game_active = True    
can_score = True
score = 0
hs = open('high_score.txt', 'r+')
high_score = int(hs.read())

def draw_floor():
    screen.blit(floor_surface, (floor_x, 900))          # Place the first floor at the bottom of the screen
    screen.blit(floor_surface, (floor_x + 576,900))     # Place the second floor at the end of first floor

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos-300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    global can_score

    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            can_score = True
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        if bird_rect.top <= -100:
            swoosh_sound.play()
        else:
            fell_sound.play()

        can_score = True
        return False
    else:
        return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    global hs

    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)), True, (255,255,255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)
    if game_state == "game_over":
        score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (288, 850))
        screen.blit(high_score_surface, high_score_rect)

        hs.seek(0)
        hs.truncate()
        hs.write(str(high_score))

def update_score(score, high_score):
    global hs
    if score > high_score:
        high_score = score
    return high_score

def pipe_score_check():
    global score, can_score

    if pipe_list:
        for pipe in pipe_list:
            if 95 < pipe.centerx < 105 and can_score:
                score += 1
                score_sound.play()
                can_score = False
            if pipe.centerx < 0:
                can_score = True

while True:
    for event in pygame.event.get():                # Get the commands from the keyboard
        if event.type == pygame.QUIT:
            pygame.quit()                           # Quit the game
            sys.exit()                              # Exit the system
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 11
                flap_sound.play()
            
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                score = 0

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
   
    screen.blit(bg_surface, (0,0))                  # Place the background in a specified location on the screen
    if game_active:
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement          # Apply gravity in respect to the movement
        screen.blit(rotated_bird, bird_rect)        # Place the bird on the screen
        game_active = check_collision(pipe_list)    # Checks if the bird collided with the pipe
        
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        
        pipe_score_check()
        score_display("main_game")

    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display("game_over")
    
    floor_x -= 1
    draw_floor()                                    # Draw the floor
                             
    if floor_x <= -576:                             # Manage the smooth trtansition of moving floor
        floor_x = 0

    pygame.display.update()                         # Update the display
    clock.tick(120)                                 # Limit the frame rate per second