import pygame
from game.game_engine import GameEngine

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game engine
engine = GameEngine(WIDTH, HEIGHT)

def choose_replay():
    choosing = True
    while choosing:
        SCREEN.fill(BLACK)
        font = pygame.font.SysFont("Arial", 30)
        msg = [
            "Replay Options:",
            "Press 3 for Best of 3",
            "Press 5 for Best of 5",
            "Press 7 for Best of 7",
            "Press ESC to Exit"
        ]
        for i, line in enumerate(msg):
            text = font.render(line, True, WHITE)
            SCREEN.blit(text, (WIDTH//2 - text.get_width()//2, 150 + i*50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    return 3
                elif event.key == pygame.K_5:
                    return 5
                elif event.key == pygame.K_7:
                    return 7
                elif event.key == pygame.K_ESCAPE:
                    return None

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        if engine.check_game_over(SCREEN):
            winning_score = choose_replay()
            if winning_score:
                engine.winning_score = winning_score
                engine.reset_scores()
            else:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
