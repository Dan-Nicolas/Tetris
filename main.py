import pygame as pg
import sys
from game import Game
from colors import Colors

pg.init()

title_font = pg.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
score_rect = pg.Rect(320, 55, 170, 60)

next_surface = title_font.render("Next", True, Colors.white)
next_rect = pg.Rect(320,195,170,180)

game_over_surface = title_font.render("GAME OVER", True, Colors.white)

WIDTH,HEIGHT = 500,620

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Tetris")

CLOCK = pg.time.Clock()

game = Game()

# used for the blocks falling every 225 ms instead of every 60 times a second
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE, 225)


def main():
    # Set an initial delay value
    move_delay = 175  # milliseconds between moves
    last_move_time = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pg.K_UP and game.game_over == False:
                    game.rotate()

            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        # Get the current time (in milliseconds)
        current_time = pg.time.get_ticks()

        # Check continuously if keys are being held down
        keys = pg.key.get_pressed()

        # Throttle movement by ensuring enough time has passed between moves
        if keys[pg.K_LEFT] and game.game_over == False:
            if current_time - last_move_time > move_delay:
                game.move_left()
                last_move_time = current_time  # Reset the last move time
        if keys[pg.K_RIGHT] and game.game_over == False:
            if current_time - last_move_time > move_delay:
                game.move_right()
                last_move_time = current_time  # Reset the last move time
        if keys[pg.K_DOWN] and game.game_over == False:
            if current_time - last_move_time > move_delay:
                game.move_down()
                game.update_score(0, 1)
                last_move_time = current_time  # Reset the last move time

        screen.fill(Colors.dark_blue)
        score_value = title_font.render(str(game.score), True, Colors.white)
        
        screen.blit(score_surface, (365, 20, 20, 50))
        screen.blit(next_surface, (375, 160, 50, 50))
        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pg.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value, score_value.get_rect(centerx = score_rect.centerx,
                                                      centery = score_rect.centery))
        pg.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)
        pg.display.update()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()