import pygame
from pygame.locals import *

# Initialize Pygame modules
pygame.init()
pygame.font.init()

# Set up game window and parameters
size = WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")
FPS = 60
FONT = pygame.font.SysFont("comicsans", 50)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (218, 170, 87)

# Function to draw the game grid
# Draws the vertical and horizontal lines to create a 3x3 grid
def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, pygame.Rect(WIDTH // 3 - 5, 0, 10, HEIGHT))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(
        WIDTH // 3 + WIDTH // 3 - 5, 0, 10, HEIGHT))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0, HEIGHT // 3 - 5, WIDTH, 10))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(
        0, HEIGHT // 3 + HEIGHT // 3 - 5, WIDTH, 10))
    pygame.display.update()

# Function to determine which grid box was clicked based on mouse position
def get_box(x, y):
    if 0 <= x <= 195 and 0 <= y <= 195:
        return 1
    elif 200 <= x <= 395 and 0 <= y <= 195:
        return 2
    elif 400 <= x <= 600 and 0 <= y <= 195:
        return 3
    elif 0 <= x <= 195 and 200 <= y <= 395:
        return 4
    elif 200 <= x <= 395 and 200 <= y <= 395:
        return 5
    elif 400 <= x <= 600 and 200 <= y <= 395:
        return 6
    elif 0 <= x <= 195 and 400 <= y <= 600:
        return 7
    elif 200 <= x <= 395 and 400 <= y <= 600:
        return 8
    elif 400 <= x <= 600 and 400 <= y <= 600:
        return 9

# Function to draw 'X' or 'O' based on the player's turn
def draw_box(x_turn, box):
    global q, w, e, r, t, y, u, i, o

    if x_turn:
        color = BLUE
        mark = "X"
    else:
        color = RED
        mark = "O"

    positions = {
        1: (30, 30, 170, 170), 2: (230, 30, 370, 170), 3: (430, 30, 570, 170),
        4: (30, 230, 170, 370), 5: (230, 230, 370, 370), 6: (430, 230, 570, 370),
        7: (30, 430, 170, 570), 8: (230, 430, 370, 570), 9: (430, 430, 570, 570)
    }

    if box in positions:
        x1, y1, x2, y2 = positions[box]
        if x_turn:
            pygame.draw.line(WIN, color, (x1, y1), (x2, y2), 8)
            pygame.draw.line(WIN, color, (x2, y1), (x1, y2), 8)
        else:
            pygame.draw.circle(
                WIN, color, ((x1 + x2) // 2, (y1 + y2) // 2), 75, 8)

    grid_vars = ["q", "w", "e", "r", "t", "y", "u", "i", "o"]
    globals()[grid_vars[box - 1]] = mark

    pygame.display.update()

# Function to check for a winning condition
def check_win():
    if q == w == e and q != " ":
        return True, q
    if r == t == y and r != " ":
        return True, r
    if u == i == o and u != " ":
        return True, u
    if q == r == u and q != " ":
        return True, q
    if w == t == i and w != " ":
        return True, w
    if e == y == o and e != " ":
        return True, e
    if q == t == o and q != " ":
        return True, q
    if e == t == u and e != " ":
        return True, e
    return False, None

# Function to check if the game is a draw
def check_draw():
    if " " not in [q, w, e, r, t, y, u, i, o] and not check_win()[0]:
        return True
    return False

# Main game loop
def main():
    global q, w, e, r, t, y, u, i, o
    clock = pygame.time.Clock()
    run = True

    while run:
        x_turn = True
        used_box = []
        q = w = e = r = t = y = u = i = o = " "
        draw_window()

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return

            mouse_click = pygame.mouse.get_pressed()
            if mouse_click[0]:
                x, y = pygame.mouse.get_pos()
                box = get_box(x, y)
                if box and box not in used_box:
                    draw_box(x_turn, box)
                    x_turn = not x_turn
                    used_box.append(box)

                    if check_win()[0]:
                        winner_text = FONT.render(
                            f"{check_win()[1]} Won!", True, BLACK, GOLD)
                        WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        break
                    elif check_draw():
                        draw_text = FONT.render("Tie!", True, BLACK, GOLD)
                        WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height()))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        break

# Run the game if this file is executed directly
if __name__ == "__main__":
    main()